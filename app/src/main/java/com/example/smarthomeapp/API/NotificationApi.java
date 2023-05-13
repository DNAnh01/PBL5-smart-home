package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Notification;
import com.example.smarthomeapp.Model.NotificationView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.List;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface NotificationApi {
    //https://pbl5-5jdn.onrender.com/notice_details/get/NoticeDetailsDocumentID
    //https://pbl5-5jdn.onrender.com/notice_details_view/get/NoticeDetailsViewDocumentID

    //https://pbl5-smart-home.onrender.com/docs
    //https://pbl5-9n8k.onrender.com/docs
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    NotificationApi notificationApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-5jdn.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(NotificationApi.class);

    @GET("notice_details_view/get/NoticeDetailsViewDocumentID")
    Call<NotificationView> getListDetailView();

    @GET("notice_details/get/NoticeDetailsDocumentID")
    Call<Notification> getNotification();
}
