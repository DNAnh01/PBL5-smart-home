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
import android.view.MotionEvent;
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

        view.setOnTouchListener(new View.OnTouchListener() {
            private float startY;
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                switch (event.getAction()) {
                    case MotionEvent.ACTION_DOWN:
                        startY = event.getY();
                        break;
                    case MotionEvent.ACTION_UP:
                        float endY = event.getY();
                        float deltaY = endY - startY;

                        if (deltaY > 0) {
                            getListNotifications();
                        }
                        break;
                }
                return true;
            }
        });


        rvListNotification = view.findViewById(R.id.rv_listNotification);
        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(getActivity());
        rvListNotification.setLayoutManager(linearLayoutManager);

        DividerItemDecoration itemDecoration = new DividerItemDecoration(getActivity(), DividerItemDecoration.VERTICAL);
        rvListNotification.addItemDecoration(itemDecoration);

        listNotification = new ArrayList<>();

        getListNotifications();

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                getListNotifications();
                mHandler.postDelayed(mRunnable, 600000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 600000); // Gọi đầu tiên sau 5 giây

        return view;
    }


    public void getListNotifications()
    {
        listNotification = new ArrayList<>();
        NotificationApi.notificationApi.getNotification().enqueue(new Callback<Notification>() {
            @Override
            public void onResponse(Call<Notification> call, Response<Notification> response) {
                notification = response.body();
                listNotification.add(notification);
                notificationAdapter = new NotificationAdapter(listNotification);
                rvListNotification.setAdapter(notificationAdapter);
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