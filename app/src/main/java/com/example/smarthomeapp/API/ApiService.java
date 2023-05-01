package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.Sensor;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface ApiService {

    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    ApiService apiService = new Retrofit.Builder()
            .baseUrl("https://pbl5-5jdn.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(ApiService.class);

    //Sensor
    //https://pbl5-5jdn.onrender.com/temperature_sensor/get/TemperatureSensorDocumentID
    @GET("temperature_sensor/get/TemperatureSensorDocumentID")
    Call<Sensor> getTemperatureSensor();

    //https://pbl5-5jdn.onrender.com/gas_sensor/get/GasSensorDocumentID
    @GET("gas_sensor/get/GasSensorDocumentID")
    Call<Sensor> getGasSensor();

    //https://pbl5-5jdn.onrender.com/humidity_sensor/get/HumiditySensorDocumentID
    @GET("humidity_sensor/get/HumiditySensorDocumentID")
    Call<Sensor> getHumiditySensor();

    //Device
    //https://pbl5-5jdn.onrender.com/gatehouse/get/GatehouseDocumentID
    @GET("gatehouse/get/GatehouseDocumentID")
    Call<Device> getStatusGate();

    //Notification
}
