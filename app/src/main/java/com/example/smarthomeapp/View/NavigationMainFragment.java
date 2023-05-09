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
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.Switch;
import android.widget.TextView;

import com.example.smarthomeapp.API.DeviceApi;
import com.example.smarthomeapp.API.SensorApi;
import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.Model.SensorDetail;
import com.example.smarthomeapp.Model.SensorView;
import com.example.smarthomeapp.R;
import com.github.mikephil.charting.data.Entry;

import java.io.Serializable;
import java.lang.reflect.Array;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NavigationMainFragment extends Fragment {

    private TextView tvHumidity, tvGas, tvTemperature;
    private Switch swDoor,swLed;
    private Handler mHandler;
    private Runnable mRunnable;

    private SensorView sensorView;

    private LinearLayout btnTemperature, btnGas, btnHumidity;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_navigation_main, container, false);


        tvGas = view.findViewById(R.id.tv_gas);
        tvHumidity = view.findViewById(R.id.tv_humidity);
        tvTemperature = view.findViewById(R.id.tv_temperature);

        swDoor = view.findViewById(R.id.sw_door);
        swLed = view.findViewById(R.id.sw_led);

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                load();
                mHandler.postDelayed(mRunnable, 10000); // Gọi lại mỗi 10 giây
            }
        };
        mHandler.postDelayed(mRunnable, 10000); // Gọi đầu tiên sau 10 giây

        btnTemperature = view.findViewById(R.id.btn_temperature);
        btnGas = view.findViewById(R.id.btn_gas);
        btnHumidity = view.findViewById(R.id.btn_humidity);
        btnTemperature.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                switchDetailFragment("Temperature",view);
            }
        });

        btnGas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                switchDetailFragment("Gas",view);
            }
        });

        btnHumidity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                switchDetailFragment("Humidity",view);
            }
        });


        swDoor.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                updateDevice(b,"gate");
            }
        });
        swLed.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                updateDevice(b,"led");
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
        loadSensor();
        loadDevice();
    }
    private void loadDevice()
    {
        DeviceApi.deviceApi.getStatusGate().enqueue(new Callback<Device>() {
            @Override
            public void onResponse(Call<Device> call, Response<Device> response) {
                Device device = response.body();
                if(device != null)
                {
                    if(device.getStatus() == 0 )
                    {
                        swDoor.setChecked(false);
                    }
                    else
                    {
                        swDoor.setChecked(true);
                    }
                }
            }

            @Override
            public void onFailure(Call<Device> call, Throwable t) {
                Log.d("DEBUG", "fail deive gate: " + t.getMessage());
            }
        });
        DeviceApi.deviceApi.getStatusLed().enqueue(new Callback<Device>() {
            @Override
            public void onResponse(Call<Device> call, Response<Device> response) {
                Device device = response.body();
                if(device != null)
                {
                    if(device.getStatus() == 0 )
                    {
                        swLed.setChecked(false);
                    }
                    else
                    {
                        swLed.setChecked(true);
                    }
                }
            }

            @Override
            public void onFailure(Call<Device> call, Throwable t) {
                Log.d("DEBUG", "fail device led: " + t.getMessage());
            }
        });
    }
    private void loadSensor()
    {
        SensorApi.sensorApi.getAllSensor().enqueue(new Callback<SensorDetail>() {
            @Override
            public void onResponse(Call<SensorDetail> call, Response<SensorDetail> response) {
                SensorDetail sensor = response.body();
                if(sensor != null)
                {
                    tvGas.setText(sensor.getGas_sensor_data());
                    tvHumidity.setText(sensor.getHumidity_sensor_data());
                    tvTemperature.setText(sensor.getTemperature_sensor_data());
                }
            }

            @Override
            public void onFailure(Call<SensorDetail> call, Throwable t) {
                Log.d("DEBUG", "fail sensor: " + t.getMessage());
            }
        });
    }

    private void updateDevice(Boolean status, String thietbi)
    {
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd");
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");

        String currentDate = dateFormat.format(calendar.getTime());
        String currentTime = timeFormat.format(calendar.getTime());
        String timeNow = currentDate + " " + currentTime;
        int intStatus = status ? 1 : 0;
       // Log.d("DEBUG", "new status gate: " + intStatus);
        if(thietbi == "gate")
        {
            Device deviceData = new Device(intStatus, timeNow);
            DeviceApi.deviceApi.updateGate(deviceData).enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                    // loadDevice();
                    Log.d("DEBUG", "success update gate ");
                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable t) {
                    Log.d("DEBUG", "fail update gate: " + t.getMessage());
                }
            });
        }
        else if(thietbi == "led")
        {
            Device deviceData = new Device(intStatus);
            DeviceApi.deviceApi.updateLed(deviceData).enqueue(new Callback<ResponseBody>() {
                @Override
                public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                    // loadDevice();
                    Log.d("DEBUG", "success update led ");
                }

                @Override
                public void onFailure(Call<ResponseBody> call, Throwable t) {
                    Log.d("DEBUG", "fail update led: " + t.getMessage());
                }
            });
        }


    }

    private void switchDetailFragment(String sensorName, View view)
    {
        Bundle bundle = new Bundle();
        bundle.putString("myString", sensorName);
        Navigation.findNavController(view).navigate(R.id.action_navigationMainFragment_to_navigationDetailDiagramFragment, bundle);
      //  Navigation.findNavController(view).navigate(R.id.action_navigationMainFragment_to_navigationDetailDiagramFragment);
    }

}