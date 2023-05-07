package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.Notification;
import com.example.smarthomeapp.Model.NotificationView;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.Model.SensorDetail;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface ApiService {
    //https://pbl5-smart-home.onrender.com/
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    ApiService apiService = new Retrofit.Builder()
            .baseUrl("https://pbl5-smart-home.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(ApiService.class);

    //Sensor
    //https://pbl5-5jdn.onrender.com/sensors/get/SensorsDocumentID
    @GET("sensors/get/SensorsDocumentID")
    Call<SensorDetail> getAllSensor();

    //Device
    //https://pbl5-5jdn.onrender.com/gatehouse/get/GatehouseDocumentID
    @GET("gatehouse/get/GatehouseDocumentID")
    Call<Device> getStatusGate();

    //Notification
    //https://pbl5-5jdn.onrender.com/notice_details_view/get/NoticeDetailsViewDocumentID
    @GET("notice_details_view/get/NoticeDetailsViewDocumentID")
    Call<NotificationView> getListDetailView();
    //https://pbl5-5jdn.onrender.com/notice_details/get/NoticeDetailsDocumentID
    @GET("notice_details/get/NoticeDetailsDocumentID")
    Call<Notification> getNotification();
}
