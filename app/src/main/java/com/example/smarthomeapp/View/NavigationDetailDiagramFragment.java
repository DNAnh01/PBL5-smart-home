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

import android.util.Log;
import android.view.LayoutInflater;
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
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;

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
    private String color, colorText;

    private ImageView imgPic;
    Drawable drawable;

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
            drawable = getResources().getDrawable(R.drawable.temperature);
        }
        else if(sensorName == "Gas")
        {
            color = "#CEF8DF03";
            colorText = "#FF9800";
            drawable = getResources().getDrawable(R.drawable.flame);
        }
        else
        {
            color = "#ABEBF3";
            colorText = "#5FC4F1";
            drawable = getResources().getDrawable(R.drawable.humidity);
        }
        tvSensorName.setTextColor(Color.parseColor(colorText));
        imgPic.setImageDrawable(drawable);
        return view;
    }


    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        tvSensorName.setText(sensorName);
        getListSensor().observe(getViewLifecycleOwner(), new Observer<List<Sensor>>() {
            @Override
            public void onChanged(List<Sensor> sensorList) {
                if (sensorList != null) {
                    drawChart(sensorList);
                    SensorViewAdapter adapter = new SensorViewAdapter(sensorList);
                    rvListSensor.setAdapter(adapter);
                } else {
                    Log.d("DEBUG", " sensorList null");
                }
            }
        });
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

    private void drawChart(List<Sensor> listSensor)
    {
        List<Entry> entries = new ArrayList<>();
        if (listSensor != null) {
            for (int i = 0; i < listSensor.size(); i++) {
                Sensor sensor = listSensor.get(i);
                float x = (float)(i);
                float y = Float.parseFloat(sensor.getData());
                entries.add(new Entry(x, y));
            }
            LineDataSet dataSet = new LineDataSet(entries, "Sensor Data");
            dataSet.setColor(Color.parseColor(color));
            dataSet.setLineWidth(4f);
            dataSet.setDrawCircles(false);  // Tắt hiển thị các điểm dữ liệu
            dataSet.setDrawValues(false);   // Tắt hiển thị các giá trị trên đồ thị
            dataSet.setValueTextSize(10);
            LineData lineData = new LineData(dataSet);

            chart.setData(lineData);

            chart.getXAxis().setDrawAxisLine(false);
            chart.getXAxis().setDrawLabels(false);
            chart.getAxisLeft().setDrawAxisLine(false);
            chart.getAxisLeft().setDrawLabels(false);

            chart.invalidate();
        } else {
            Log.d("DEBUG", "chart fail: list sensor null");
        }

    }
}