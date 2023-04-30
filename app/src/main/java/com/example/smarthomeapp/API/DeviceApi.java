package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Device;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface DeviceApi {
    //https://pbl5-5jdn.onrender.com/gatehouse/get/GatehouseDocumentID
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    SensorApi sensorApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-5jdn.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(SensorApi.class);

    @GET("gatehouse/get/GatehouseDocumentID")
    Call<Device> getStatusGate();
}
