package com.example.smarthomeapp.View;

import android.app.AlertDialog;
import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.widget.AppCompatButton;
import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;

import android.os.Handler;
import android.os.Vibrator;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.Switch;
import android.widget.TextView;

import com.example.smarthomeapp.API.DeviceApi;
import com.example.smarthomeapp.API.SensorApi;
import com.example.smarthomeapp.Model.Device;
import com.example.smarthomeapp.Model.SensorDetail;
import com.example.smarthomeapp.R;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NavigationMainFragment extends Fragment {

    private TextView tvHumidity, tvGas, tvTemperature;
    private Switch swDoor,swLed,swDC;
    private Handler mHandler;
    private Runnable mRunnable;

    private Handler sensorHandler;
    private Runnable sensorRunnable;
    private Handler deviceHandler;
    private Runnable deviceRunnable;

    private static boolean isNotification = true;

    private View view;

    private LinearLayout btnTemperature, btnGas, btnHumidity;

    private Vibrator vibrator;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        view =  inflater.inflate(R.layout.fragment_navigation_main, container, false);

        tvGas = view.findViewById(R.id.tv_gas);
        tvHumidity = view.findViewById(R.id.tv_humidity);
        tvTemperature = view.findViewById(R.id.tv_temperature);
        swDoor = view.findViewById(R.id.sw_door);
        swLed = view.findViewById(R.id.sw_led);
        swDC = view.findViewById(R.id.sw_dc);
        btnTemperature = view.findViewById(R.id.btn_temperature);
        btnGas = view.findViewById(R.id.btn_gas);
        btnHumidity = view.findViewById(R.id.btn_humidity);

        vibrator = (Vibrator) requireContext().getSystemService(Context.VIBRATOR_SERVICE);

        load();

     /*   mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                load();
                mHandler.postDelayed(mRunnable, 5000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 5000); // Gọi đầu tiên sau 5 giây */

        // Khởi tạo handler và runnable cho sensor
        sensorHandler = new Handler();
        sensorRunnable = new Runnable() {
            @Override
            public void run() {
                loadSensor();
                sensorHandler.postDelayed(this, 3000); // Gọi lại mỗi 3 giây
            }
        };

        // Khởi tạo handler và runnable cho device
        deviceHandler = new Handler();
        deviceRunnable = new Runnable() {
            @Override
            public void run() {
                loadDevice();
                deviceHandler.postDelayed(this, 5000); // Gọi lại mỗi 5 giây
            }
        };

        // Bắt đầu gọi lần đầu tiên sau 3 giây cho sensor và sau 5 giây cho device
        sensorHandler.postDelayed(sensorRunnable, 3000);
        deviceHandler.postDelayed(deviceRunnable, 5000);


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
                updateDevice();
            }
        });
        swLed.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                updateDevice();
            }
        });

        swDC.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                updateDevice();
            }
        });

        return view;
    }


    private void load()
    {
        loadDevice();
        loadSensor();
    }
    private void vibrate() {
        if (vibrator.hasVibrator()) {
            vibrator.vibrate(1000);
        }
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        vibrator.cancel();
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();

        // Hủy bỏ các handler khi Fragment bị hủy
        sensorHandler.removeCallbacks(sensorRunnable);
        deviceHandler.removeCallbacks(deviceRunnable);
    }
    private void loadDevice() {
        DeviceApi.deviceApi.getStatusAll().enqueue(new Callback<Device>() {
            @Override
            public void onResponse(Call<Device> call, Response<Device> response) {
                Device device = response.body();
                if (device != null) {
                    swLed.setChecked(device.getLed_status() == 1);
                    swDoor.setChecked(device.getGatehouse_status() == 1);
                    swDC.setChecked(device.getDc_status() == 1);
                }
            }

            @Override
            public void onFailure(Call<Device> call, Throwable t) {
                Log.d("DEBUG", "Get device failed: " + t.getMessage());
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
                    if(sensor.getGas_sensor_data().equals("1"))
                    {
                        vibrate();
                    }
                }
            }

            @Override
            public void onFailure(Call<SensorDetail> call, Throwable t) {
                Log.d("DEBUG", "fail sensor: " + t.getMessage());
            }
        });
    }

    private void updateDevice()
    {
        int gate = swDoor.isChecked() ? 1 : 0;
        int dc = swDC.isChecked() ? 1 : 0;
        int led = swLed.isChecked() ? 1 : 0;
        Device device = new Device(gate,led,dc);
        DeviceApi.deviceApi.updateAll(device).enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                loadDevice();
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                Log.d("DEBUG", "fail update device: " + t.getMessage());
            }
        });

    }

    private void switchDetailFragment(String sensorName, View view)
    {
        Bundle bundle = new Bundle();
        bundle.putString("myString", sensorName);
        Navigation.findNavController(view).navigate(R.id.action_navigationMainFragment_to_navigationDetailDiagramFragment, bundle);
    }

  /*  private void showWarming() {
        if (isNotification  && !swDC.isChecked() ) {
            vibrate();
            AlertDialog.Builder mDialog = new AlertDialog.Builder(getContext());
            LayoutInflater inflater = LayoutInflater.from(getContext());
            View mView = inflater.inflate(R.layout.dialog_notification, null);
            mDialog.setView(mView);

            AlertDialog dialog = mDialog.create();
            dialog.setCancelable(true);

            AppCompatButton btnNo = mView.findViewById(R.id.btn_no);
            AppCompatButton btnYes = mView.findViewById(R.id.btn_yes);
            CheckBox checkBox = mView.findViewById(R.id.checkBox);

            btnNo.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    dialog.dismiss();
                }
            });

            checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
                @Override
                public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                    isNotification = false;
                    dialog.dismiss();
                }
            });

            btnYes.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    int gate = swDoor.isChecked() ? 1 : 0;
                    int led = swLed.isChecked() ? 1 : 0;
                    Device device = new Device(gate,led,1);
                    DeviceApi.deviceApi.updateAll(device).enqueue(new Callback<ResponseBody>() {
                        @Override
                        public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                            Log.d("DEBUG", "success update device: ");
                        }

                        @Override
                        public void onFailure(Call<ResponseBody> call, Throwable t) {
                            Log.d("DEBUG", "fail update device: " + t.getMessage());
                        }
                    });
                    dialog.dismiss();
                }
            });

            dialog.show();
        }
    }

   */


}