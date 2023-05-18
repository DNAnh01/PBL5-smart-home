#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>
#include <WiFiClient.h>
#include <FS.h> 
#include <SPIFFS.h>
#include <base64.h>

#define CAMERA_MODEL_AI_THINKER // Has PSRAM
//#define CAMERA_MODEL_TTGO_T_JOURNAL // No PSRAM

#include "camera_pins.h"

const char* ssid = "Tro 55";
const char* password = "xomtro55";
//const char* ssid = "KEM";
//const char* password = "20052002";

IPAddress localIP(192, 168, 1, 10);  // Địa chỉ IP tùy chỉnh
IPAddress gateway(192, 168, 1, 1);  // Địa chỉ gateway
IPAddress subnet(255, 255, 255, 0); // Subnet mask
AsyncWebServer server(80);

String imageFilePath = "/image.jpg";
String server_url = "http://127.0.0.1:8000/camera/get";
String image_url = "http://192.168.1.10/capture";

void startCameraServer();

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  
  // if PSRAM IC present, init with UXGA resolution and higher JPEG quality
  //                      for larger pre-allocated frame buffer.
  if(psramFound()){
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  sensor_t * s = esp_camera_sensor_get();
  // initial sensors are flipped vertically and colors are a bit saturated
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1); // flip it back
    s->set_brightness(s, 1); // up the brightness just a bit
    s->set_saturation(s, -2); // lower the saturation
  }
  // drop down frame size for higher initial frame rate
  s->set_framesize(s, FRAMESIZE_QVGA);

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif
  WiFi.config(localIP, gateway, subnet);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  startCameraServer();

  Serial.print("Camera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");

   camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }
  HTTPClient http;
  http.begin(image_url); // Thay thế bằng URL của ảnh
  int httpCode = http.GET();
  if (httpCode == HTTP_CODE_OK) {
    // Đọc dữ liệu ảnh
    WiFiClient* stream = http.getStreamPtr();
    File imageFile = SPIFFS.open(imageFilePath, "w"); // Mở file ảnh để ghi
    while (stream->available()) {
      imageFile.write(stream->read());
    }
    imageFile.close();
    Serial.println("Đã lưu ảnh vào SPIFFS");
  } else {
    Serial.println("Lỗi khi lấy ảnh từ URL");
    http.end();
    return;
  }
  http.end();

  // Đọc dữ liệu từ file ảnh
  File imageFile = SPIFFS.open(imageFilePath, "r");
  if (!imageFilePath) {
    Serial.println("Không thể mở file ảnh");
    return;
  }
  size_t imageSize = imageFile.size();
  uint8_t* imageData = (uint8_t*)malloc(imageSize);
  if (imageData == NULL) {
    Serial.println("Không đủ bộ nhớ");
    imageFile.close();
    return;
  }
  imageFile.read(imageData, imageSize);
  imageFile.close();

  // Mã hóa dữ liệu thành base64
  String base64Image = base64::encode(imageData, imageSize);

  // Tạo đối tượng JSON
  DynamicJsonDocument jsonDoc(512);
  JsonObject jsonRoot = jsonDoc.to<JsonObject>();

  // Thêm dữ liệu vào đối tượng JSON
  jsonRoot["image_base64"] = base64Image;

  // Chuyển đối tượng JSON thành chuỗi JSON
  String jsonString;
  serializeJson(jsonRoot, jsonString);
  Serial.println("Chuỗi JSON:");
  Serial.println(jsonString);
  // Gửi chuỗi JSON đến web server
  HTTPClient httpPost;
  httpPost.begin(server_url);
  httpPost.addHeader("Content-Type", "application/json");
  int httpResponseCode = httpPost.POST(jsonString);
  http.end();
  esp_camera_fb_return(fb);
}

void loop() {
 
  delay(10000);
}
