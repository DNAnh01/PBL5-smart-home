package com.example.smarthomeapp.API;

import com.example.smarthomeapp.Model.DC;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.PUT;

public interface DCApi {
    //https://pbl5-9n8k.onrender.com/dc/update/DCDocumentID
    Gson gson = new GsonBuilder().setDateFormat("yyyy-MM-dd HH:mm:ss").create();
    DCApi DCApi = new Retrofit.Builder()
            .baseUrl("https://pbl5-9n8k.onrender.com/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(DCApi.class);

    @PUT("dc/update/DCDocumentID")
    Call<DC> updateDC(@Body DC dcData);
}
