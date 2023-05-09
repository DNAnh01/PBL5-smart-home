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

import com.example.smarthomeapp.API.NotificationApi;
import com.example.smarthomeapp.Adapter.NotificationAdapter;
import com.example.smarthomeapp.Model.Notification;
import com.example.smarthomeapp.Model.NotificationView;
import com.example.smarthomeapp.R;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NotificationFragment extends Fragment {

    private RecyclerView rvListNotification;
    private NotificationView notificationView;
    private List<Notification> listNotification;
    private Handler mHandler;
    private Runnable mRunnable;

    private Notification notification;

    private NotificationAdapter notificationAdapter;

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
    /*    mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                getListNotifications();
                mHandler.postDelayed(mRunnable, 30000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 30000); // Gọi đầu tiên sau 5 giây*/

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        getListNotifications();
    }

    private void getListNotifications()
    {
        Log.d("DEBUG", "show list notification");
        NotificationApi.notificationApi.getNotification().enqueue(new Callback<Notification>() {
            @Override
            public void onResponse(Call<Notification> call, Response<Notification> response) {
                notification = response.body();
                listNotification.add(notification);
                notificationAdapter = new NotificationAdapter(listNotification);
                rvListNotification.setAdapter(notificationAdapter);
                Log.d("DEBUG", "get notification detail success:" + response.body().toString());
            }

            @Override
            public void onFailure(Call<Notification> call, Throwable t) {
                Log.d("DEBUG", "get notification detail fail:" + t.getMessage());
            }
        });
        NotificationApi.notificationApi.getListDetailView().enqueue(new Callback<NotificationView>() {
            @Override
            public void onResponse(Call<NotificationView> call, Response<NotificationView> response) {
                notificationView = response.body();
                if (notificationView != null && notificationView.getInfo_details() != null) {
                    List<Notification> tempList = new ArrayList<>(notificationView.getInfo_details());
                    Collections.reverse(tempList);
                    listNotification.addAll(tempList);
                    NotificationAdapter notificationAdapter = new NotificationAdapter(listNotification);
                    rvListNotification.setAdapter(notificationAdapter);
                    Log.d("DEBUG", "get notification success:" + response.body().toString());
                } else {
                    Log.d("DEBUG", "get notification success: response body or info_details is null");
                }
            }

            @Override
            public void onFailure(Call<NotificationView> call, Throwable t) {
                Log.d("DEBUG", "get notification fail:" + t.getMessage());
            }
        });
    }
}