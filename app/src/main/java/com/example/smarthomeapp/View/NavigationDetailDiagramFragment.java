package com.example.smarthomeapp.View;

import android.graphics.Color;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.example.smarthomeapp.R;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;

import java.util.ArrayList;
import java.util.List;


public class NavigationDetailDiagramFragment extends Fragment {
    private ImageView btnBack;
    private LineChart chart;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_navigation_detail_diagram, container, false);
        btnBack = view.findViewById(R.id.btn_back);
        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Navigation.findNavController(view).navigate(R.id.action_navigationDetailDiagramFragment_to_navigationMainFragment);
            }
        });

        Bundle bundle = getArguments();
        if (bundle != null) {
            List<ArrayList<Entry>> datasets = (List<ArrayList<Entry>>) bundle.getSerializable("datasets");
            if (datasets != null && !datasets.isEmpty()) {
                drawChart(datasets);
            }
        }
        return view;
    }

    private void drawChart(List<ArrayList<Entry>> datasets) {
        LineData lineData = new LineData();

        // Tạo và cấu hình các dòng dữ liệu cho biểu đồ
        for (int i = 0; i < datasets.size(); i++) {
            List<Entry> entries = datasets.get(i);
            LineDataSet lineDataSet = new LineDataSet(entries, "Dataset " + (i + 1));

            // Cấu hình các thuộc tính của dòng dữ liệu
            lineDataSet.setColor(Color.RED);
            lineDataSet.setLineWidth(2f);
            // Cấu hình các thuộc tính khác (nếu cần)

            lineData.addDataSet(lineDataSet);
        }

        // Cấu hình biểu đồ
        chart.setData(lineData);
        // Cấu hình các thuộc tính khác của biểu đồ (nếu cần)

        // Cập nhật giao diện biểu đồ
        chart.invalidate();
    }

}