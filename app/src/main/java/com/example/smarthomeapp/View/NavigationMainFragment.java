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
import android.widget.Switch;
import android.widget.TextView;

import com.example.smarthomeapp.API.ApiService;
import com.example.smarthomeapp.API.DeviceApi;
import com.example.smarthomeapp.API.SensorApi;
import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.R;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NavigationMainFragment extends Fragment {

    private TextView tvHumidity, tvGas, tvTemperature;
    private Switch swDoor;
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

        swDoor = view.findViewById(R.id.sw_door);

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                load();
                mHandler.postDelayed(mRunnable, 1000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 1000); // Gọi đầu tiên sau 5 giây

        btnTemperature = view.findViewById(R.id.btn_temperature);
        btnTemperature.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Navigation.findNavController(view).navigate(R.id.action_navigationMainFragment_to_navigationDetailDiagramFragment);
            }
        });
        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        load();
    }

    private void load()
    {
        getSensor();
        getDevice();
    }
    private void getSensor()
    {
        ApiService.apiService.getTemperatureSensor().enqueue(new Callback<Sensor>() {
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
                Log.d("DEBUG", "fail temperature: " + t.getMessage());
            }
        });
        ApiService.apiService.getGasSensor().enqueue(new Callback<Sensor>() {
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
                Log.d("DEBUG", "fail temperature: " + t.getMessage());
            }
        });
        ApiService.apiService.getHumiditySensor().enqueue(new Callback<Sensor>() {
            @Override
            public void onResponse(Call<Sensor> call, Response<Sensor> response) {
                Sensor sensor = response.body();
                if(sensor != null)
                {
                    tvHumidity.setText(sensor.getData());
                }
            }
            @Override
            public void onFailure(Call<Sensor> call, Throwable t) {
                Log.d("DEBUG", "fail temperature: " + t.getMessage());
            }
        });
    }

    private void getDevice()
    {
        ApiService.apiService.getStatusGate().enqueue(new Callback<Device>() {
            @Override
            public void onResponse(Call<Device> call, Response<Device> response) {
                Device device = response.body();
                if(device != null)
                {
                    swDoor.setChecked(device.getStatus());
                }
            }

            @Override
            public void onFailure(Call<Device> call, Throwable t) {
                Log.d("DEBUG", "fail deive gate: " + t.getMessage());
            }
        });
    }
}