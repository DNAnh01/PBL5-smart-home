package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.Notification;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.List;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;

public interface NotificationApi {
    //https://raw.githubusercontent.com/DevTides/DogsApi/master/dogs.json
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    NotificationApi notificationApi = new Retrofit.Builder()
            .baseUrl("https://raw.githubusercontent.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(NotificationApi.class);

    @GET("DevTides/DogsApi/master/dogs.json")
    Call<List<Notification>> getListNotifications();
}
