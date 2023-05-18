#include <Servo.h>
#include <ArduinoJson.h>
#include <NTPClient.h>
#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>


// Khai báo chân kết nối với cảm biến DHT11
#define DHTPIN 19       // cảm biến DHT11
#define GAS 18          // cảm biến khí gas
#define SERVO_PIN 21     // động cơ servo
#define LED_PIN 22      // đèn 

// Khai báo đối tượng cảm biến DHT11
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHT11);

Servo myservo;
// Khai báo thông tin mạng WiFi
const char* ssid = "Tro 55";         // Tên mạng WiFi
const char* password = "xomtro55"; // Mật khẩu WiFi
//const char* ssid = "lycoris";
//const char* password = "123456789";

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "vn.pool.ntp.org", 7 * 3600);

// Khai báo địa chỉ 
const char* serverurl_sensor = "https://pbl5-smart-home.onrender.com/sensors/update/SensorsDocumentID"; 
const char* serverurl_thietbi = "https://pbl5-smart-home.onrender.com/devices/get/DevicesDocumentID";
//const char* serverurl_den = "https://pbl5-9n8k.onrender.com/led/get/LedDocumentID";

// chân driver L298N 
int in1=33;
int in2=32;
int in3=35;

void setup() {
  pinMode(LED_PIN,OUTPUT);
  Serial.begin(115200);

  // Kết nối đến mạng WiFi
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode (GAS,INPUT);
  pinMode(LED_PIN, OUTPUT);
  myservo.attach(SERVO_PIN);
  dht.begin();

  timeClient.begin();
  
  while(!timeClient.update()) {
    timeClient.forceUpdate();
  }
}

void loop() {
  // Đọc dữ liệu từ cảm biến DHT11
  int h = dht.readHumidity(); // độ ẩm
  int t = dht.readTemperature(); // nhiệt độ 

  // Kiểm tra lỗi đọc cảm biến
  if (isnan(h) || isnan(t)) {
    Serial.println("Không có giá trị trả về !");
    return;
  }
  int khigas =  abs(digitalRead(GAS)-1);

  // gửi sensor
  HTTPClient httpSensor;
  httpSensor.begin(serverurl_sensor);
  httpSensor.addHeader("Content-Type", "application/json");

  StaticJsonDocument<200> jsonDocSensor;
  jsonDocSensor["timestamp"] = timeClient.getFormattedTime() ;
  jsonDocSensor["temperature_sensor_data"] = t;
  jsonDocSensor["humidity_sensor_data"] = h;
  jsonDocSensor["gas_sensor_data"] = khigas;
  char jsonStringSensor[200];
  serializeJson(jsonDocSensor, jsonStringSensor);
  Serial.println(jsonStringSensor);
  int httpCodeSensor = httpSensor.PUT(jsonStringSensor);

  if (httpCodeSensor == 200) {
    Serial.println("Gửi nhiệt độ thành công");
  } else {
    Serial.println("Gửi nhiệt độ thất bại. Code: " + String(httpCodeSensor));
  }
  httpSensor.end();



// Nhận dữ liệu từ server điều khiển cửa, quạt, đèn
  HTTPClient httpThietBi;
  httpThietBi.begin(serverurl_thietbi);
  int httpCodeThietBi = httpThietBi.GET(); 
  
  if (httpCodeThietBi == HTTP_CODE_OK) {
  String payload = httpThietBi.getString();
  StaticJsonDocument<256> doc; // Tạo một đối tượng JSON tĩnh với kích thước tối đa là 256 byte
  DeserializationError error = deserializeJson(doc, payload);
  if (!error) {
    const int gatehouse_status = doc["gatehouse_status"]; // Lấy giá trị của trường "status"
    if (gatehouse_status == 1) {
      myservo.write(0); // Nếu giá trị là "1" thì mở cửa
      Serial.println("đã mở cửa");
    } else if (gatehouse_status == 0) {
      myservo.write(90); // Nếu giá trị là "0" thì đóng cửa
      Serial.println("đã đóng cửa");
    }
    const int led_status = doc["led_status"]; // Lấy giá trị của trường "status"
    if (led_status == 1) {
      digitalWrite(LED_PIN,HIGH);
      Serial.println("Đèn bật");
    } else if (led_status == 0) {
      digitalWrite(LED_PIN,LOW);
      Serial.println("Đèn tắt");
    }
    const int dc_status = doc["dc_status"]; // Lấy giá trị của trường "status"
    if (dc_status == 1) {
      digitalWrite(in1,LOW);
      digitalWrite(in2,HIGH);
      ledcWrite(in3,150);// analogWrite ko hỗ trợ thay thế bằng ledc
      Serial.println("Quạt bật");
    } else if (dc_status == 0) {
      digitalWrite(in1,LOW);
      digitalWrite(in2,LOW);
      ledcWrite(in3,150);
      Serial.println("Quạt tắt");
    }

  } else {
    Serial.println("Failed to parse JSON");
  }
} else {
  Serial.println("Không lấy được dữ liệu servo");
}
httpThietBi.end(); // Kết thúc yêu cầu HTTP
 
}