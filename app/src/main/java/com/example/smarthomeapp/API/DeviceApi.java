package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Device;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.PUT;

public interface DeviceApi {
    //https://pbl5-5jdn.onrender.com/gatehouse/get/GatehouseDocumentID
    //https://pbl5-5jdn.onrender.com/gatehouse/update/GatehouseDocumentID
    //https://pbl5-5jdn.onrender.com/led/get/LedDocumentID
    //https://pbl5-5jdn.onrender.com/led/update/LedDocumentID

    //https://pbl5-smart-home.onrender.com/docs
    //https://pbl5-9n8k.onrender.com/docs
    //https://pbl5-5jdn.onrender.com/
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    DeviceApi deviceApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-smart-home.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(DeviceApi.class);


    @GET("devices/get/DevicesDocumentID")
    Call<Device> getStatusAll();

    @PUT("devices/update/DevicesDocumentID")
    Call<ResponseBody> updateAll(@Body Device device);
}
