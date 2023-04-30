package com.example.smarthomeapp.View;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;

import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.example.smarthomeapp.API.SensorApi;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.R;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NavigationMainFragment extends Fragment {

    private TextView tvHumidity, tvGas, tvTemperature;
    private Handler mHandler;
    private Runnable mRunnable;

    private LinearLayout btnTemperature;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_navigation_main, container, false);
        tvGas = view.findViewById(R.id.tv_gas);
        tvHumidity = view.findViewById(R.id.tv_humidity);
        tvTemperature = view.findViewById(R.id.tv_temperature);

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                load();
                mHandler.postDelayed(mRunnable, 5000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 5000); // Gọi đầu tiên sau 5 giây

        btnTemperature = view.findViewById(R.id.btn_temperature);
        btnTemperature.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Navigation.findNavController(view).navigate(R.id.action_navigationMainFragment_to_navigationDetailDiagramFragment);
            }
        });
        return view;
    }

    private void load()
    {
        getTemperatureSensor();
        getGasSensor();
        getHumiditySensor();
    }
    private void getTemperatureSensor()
    {
        SensorApi.sensorApi.getTemperatureSensor().enqueue(new Callback<Sensor>() {
            @Override
            public void onResponse(Call<Sensor> call, Response<Sensor> response) {
                Sensor sensor = response.body();
                if(sensor!= null)
                {
                    tvTemperature.setText(sensor.getData());
                }
            }
            @Override
            public void onFailure(Call<Sensor> call, Throwable t) {
                Log.d("DEBUG", "fail: " + t.getMessage());
            }
        });
    }

    private void getGasSensor()
    {
        SensorApi.sensorApi.getGasSensor().enqueue(new Callback<Sensor>() {
            @Override
            public void onResponse(Call<Sensor> call, Response<Sensor> response) {
                Sensor sensor = response.body();
                if(sensor!= null)
                {
                    tvGas.setText(sensor.getData());
                }
            }
            @Override
            public void onFailure(Call<Sensor> call, Throwable t) {
                Log.d("DEBUG", "fail: " + t.getMessage());
            }
        });
    }

    private void getHumiditySensor()
    {
        SensorApi.sensorApi.getHumiditySensor().enqueue(new Callback<Sensor>() {
            @Override
            public void onResponse(Call<Sensor> call, Response<Sensor> response) {
                Sensor sensor = response.body();
                if(sensor!= null)
                {
                    tvHumidity.setText(sensor.getData());
                }
            }
            @Override
            public void onFailure(Call<Sensor> call, Throwable t) {
                Log.d("DEBUG", "fail: " + t.getMessage());
            }
        });
    }
}