package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.Model.SensorDetail;
import com.example.smarthomeapp.Model.SensorView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import okhttp3.Response;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface SensorApi {
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    //https://pbl5-5jdn.onrender.com/sensors/get/SensorsDocumentID
    //https://pbl5-5jdn.onrender.com/sensors_view/get/SensorsViewDocumentID
    SensorApi sensorApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-9n8k.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(SensorApi.class);

    @GET("sensors/get/SensorsDocumentID")
    Call<SensorDetail> getAllSensor();
    @GET("sensors_view/get/SensorsViewDocumentID")
    Call<SensorView> getListSensorView();
}