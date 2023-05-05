package com.example.smarthomeapp.View;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.smarthomeapp.API.ApiService;
import com.example.smarthomeapp.API.NotificationApi;
import com.example.smarthomeapp.Adapter.NotificationAdapter;
import com.example.smarthomeapp.Model.Notification;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.R;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NotificationFragment extends Fragment {

    private RecyclerView rvListNotification;
    private List<Notification> listNotification;

    private Handler mHandler;
    private Runnable mRunnable;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_notification, container, false);

        rvListNotification = view.findViewById(R.id.rv_listNotification);
        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(getActivity());
        rvListNotification.setLayoutManager(linearLayoutManager);

        DividerItemDecoration itemDecoration = new DividerItemDecoration(getActivity(), DividerItemDecoration.VERTICAL);
        rvListNotification.addItemDecoration(itemDecoration);

        listNotification = new ArrayList<>();

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                getNotification();
                mHandler.postDelayed(mRunnable, 1000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 1000); // Gọi đầu tiên sau 5 giây


        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
     //   getListNotifications();
        getNotification();
    }

/*    private void getListNotifications()
    {
        NotificationApi.notificationApi.getListNotifications().enqueue(new Callback<List<Notification>>() {
            @Override
            public void onResponse(Call<List<Notification>> call, Response<List<Notification>> response) {
                listNotification = response.body();
                NotificationAdapter notificationAdapter = new NotificationAdapter(listNotification);
                rvListNotification.setAdapter(notificationAdapter);
                Log.d("DEBUG", "get notification success:" + response.body().toString());
            }

            @Override
            public void onFailure(Call<List<Notification>> call, Throwable t) {
                Log.d("DEBUG", "get notification fail:" + t.getMessage());
            }
        });
    }*/
    private void getNotification()
    {
        ApiService.apiService.getNotification().enqueue(new Callback<Notification>() {
            @Override
            public void onResponse(Call<Notification> call, Response<Notification> response) {
                listNotification = new ArrayList<>();
                Notification notification = response.body();
                if(notification != null)
                {
                    listNotification.add(notification);
                    NotificationAdapter notificationAdapter = new NotificationAdapter(listNotification);
                    rvListNotification.setAdapter(notificationAdapter);
                }
            }

            @Override
            public void onFailure(Call<Notification> call, Throwable t) {
                Log.d("DEBUG", "get notification fail:" + t.getMessage());
            }
        });
    }
}