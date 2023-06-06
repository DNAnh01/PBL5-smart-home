package com.example.smarthomeapp.View;

import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.Observer;
import androidx.navigation.Navigation;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.smarthomeapp.API.SensorApi;
import com.example.smarthomeapp.Adapter.NotificationAdapter;
import com.example.smarthomeapp.Adapter.SensorViewAdapter;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.Model.SensorView;
import com.example.smarthomeapp.R;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.AxisBase;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.formatter.IAxisValueFormatter;
import com.github.mikephil.charting.formatter.IndexAxisValueFormatter;
import com.github.mikephil.charting.formatter.ValueFormatter;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class NavigationDetailDiagramFragment extends Fragment {
    private ImageView btnBack;
    private LineChart chart;

    private RecyclerView rvListSensor;

    private String sensorName;

    private TextView tvSensorName;
    private String color, colorText, colorCircle;

    private ImageView imgPic;

    private Handler mHandler;
    private Runnable mRunnable;

    Drawable drawable;

    private boolean isViewCreated = false;

    private MutableLiveData<List<Sensor>> sensorListLiveData = new MutableLiveData<>();
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_navigation_detail_diagram, container, false);

        btnBack = view.findViewById(R.id.btn_back);
        chart = view.findViewById(R.id.lineChart);
        tvSensorName = view.findViewById(R.id.tv_sensorName);
        imgPic = view.findViewById(R.id.img_image);
        rvListSensor = view.findViewById(R.id.rv_listSensor);

        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(getActivity());
        rvListSensor.setLayoutManager(linearLayoutManager);

        DividerItemDecoration itemDecoration = new DividerItemDecoration(getActivity(), DividerItemDecoration.VERTICAL);
        rvListSensor.addItemDecoration(itemDecoration);

        mHandler = new Handler();
        mRunnable = new Runnable() {
            @Override
            public void run() {
                init();
                mHandler.postDelayed(mRunnable, 5000); // Gọi lại mỗi 5 giây
            }
        };
        mHandler.postDelayed(mRunnable, 5000); // Gọi đầu tiên sau 5 giây

        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Navigation.findNavController(view).navigate(R.id.action_navigationDetailDiagramFragment_to_navigationMainFragment);
            }
        });

        sensorName = getArguments().getString("myString");
        if(sensorName == "Temperature")
        {
            color = "#F1877F";
            colorText = "#F71505";
            colorCircle = "#5FC4F1";
            drawable = getResources().getDrawable(R.drawable.temperature);
        }
        else if(sensorName == "Gas")
        {
            color = "#CEF8DF03";
            colorText = "#FF9800";
            colorCircle = "#E8A4F3";
            drawable = getResources().getDrawable(R.drawable.flame);
        }
        else
        {
            color = "#69BEE4";
            colorText = "#5FC4F1";
            colorCircle = "#E8673E";
            drawable = getResources().getDrawable(R.drawable.humidity);
        }
        tvSensorName.setTextColor(Color.parseColor(colorText));
        imgPic.setImageDrawable(drawable);
        return view;
    }


    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        isViewCreated = true;
        init();
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        // Hủy bỏ các handler khi Fragment bị hủy
        mHandler.removeCallbacks(mRunnable);
    }

    private void init()
    {
        if (isViewCreated) {
            tvSensorName.setText(sensorName);
            getListSensor().observe(getViewLifecycleOwner(), new Observer<List<Sensor>>() {
                @Override
                public void onChanged(List<Sensor> sensorList) {
                    if (sensorList != null) {
                        // drawChart(sensorList);
                        drawChart(sensorList);
                        SensorViewAdapter adapter = new SensorViewAdapter(sensorList);
                        rvListSensor.setAdapter(adapter);
                    } else {
                        Log.d("DEBUG", " sensorList null");
                    }
                }
            });
        }

    }

    private LiveData<List<Sensor>> getListSensor() {
        SensorApi.sensorApi.getListSensorView().enqueue(new Callback<SensorView>() {
            @Override
            public void onResponse(Call<SensorView> call, Response<SensorView> response) {
                SensorView sensorView = response.body();
                List<Sensor> sensorList = null;

                if (sensorView != null) {
                    if (sensorName.equals("Temperature")) {
                        sensorList = sensorView.getTemperature_sensor();
                    } else if (sensorName.equals("Gas")) {
                        sensorList = sensorView.getGas_sensor();
                    } else {
                        sensorList = sensorView.getHumidity_sensor();
                    }
                }
                sensorListLiveData.postValue(sensorList);
            }

            @Override
            public void onFailure(Call<SensorView> call, Throwable t) {
                Log.d("DEBUG", "Fail getListSensorView " + t.getMessage());
                sensorListLiveData.postValue(null);
            }
        });

        return sensorListLiveData;
    }

    private void drawChart(List<Sensor> listSensor) {
        List<Entry> entries = new ArrayList<>();
        List<String> dates = new ArrayList<>();
        if (listSensor != null) {
            for (int i = 0; i < listSensor.size(); i++) {
                Sensor sensor = listSensor.get(i);
                int data = Integer.parseInt(sensor.getData());
                String date = sensor.getTimestamp();
                entries.add(new Entry(i, data));
                dates.add(date);
            }

            ValueFormatter xAxisValueFormatter = new IndexAxisValueFormatter(dates);

            XAxis xAxis = chart.getXAxis();
            xAxis.setValueFormatter(xAxisValueFormatter);
            xAxis.setLabelRotationAngle(-75f);
            xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
            xAxis.setLabelCount(dates.size(), false);
            xAxis.setTextSize(15); // Cài đặt cỡ chữ
          //  xAxis.setTextColor(Color.parseColor(colorText));

            LineDataSet dataSet = new LineDataSet(entries, "Sensor Data");
            dataSet.setColor(Color.parseColor(color));
            dataSet.setCircleColor(Color.parseColor(colorCircle));
            dataSet.setLineWidth(4f);
            dataSet.setValueTextColor(Color.parseColor(colorText));
            dataSet.setValueFormatter(new ValueFormatter() {
                @Override
                public String getFormattedValue(float value) {
                    return String.format("%.0f", value);
                }
            });
            dataSet.setValueTextSize(15);
            dataSet.setValueTextColor(Color.parseColor(colorCircle));

            LineData lineData = new LineData(dataSet);
            chart.getXAxis().setAxisMinimum(0f);
            chart.getXAxis().setAxisMaximum(entries.size());
            chart.setData(lineData);
            chart.getAxisRight().setDrawLabels(false);
            // chart.getAxisLeft().setDrawLabels(false);

            chart.invalidate();
        } else {
        Log.d("DEBUG", "chart fail: list sensor null");
        }
    }

}