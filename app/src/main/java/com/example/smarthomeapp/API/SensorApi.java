package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Sensor;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface SensorApi {
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    //https://pbl5-5jdn.onrender.com/temperature_sensor/get/TemperatureSensorDocumentID
    //https://pbl5-5jdn.onrender.com/gas_sensor/get/GasSensorDocumentID
    //https://pbl5-5jdn.onrender.com/humidity_sensor/get/HumiditySensorDocumentID
    SensorApi sensorApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-5jdn.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(SensorApi.class);
    //get temperature
    @GET("temperature_sensor/get/TemperatureSensorDocumentID")
    Call<Sensor> getTemperatureSensor();

    @GET("gas_sensor/get/GasSensorDocumentID")
    Call<Sensor> getGasSensor();

    @GET("humidity_sensor/get/HumiditySensorDocumentID")
    Call<Sensor> getHumiditySensor();
}
