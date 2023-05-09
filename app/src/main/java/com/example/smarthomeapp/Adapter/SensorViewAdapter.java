package com.example.smarthomeapp.Adapter;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Base64;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.smarthomeapp.Model.Notification;
import com.example.smarthomeapp.Model.Sensor;
import com.example.smarthomeapp.R;

import java.util.List;

public class SensorViewAdapter extends RecyclerView.Adapter<SensorViewAdapter.SensorViewHolder> {
    private final List<Sensor> listSensor;

    public SensorViewAdapter(List<Sensor> listSensor) {
        this.listSensor = listSensor;
    }

    @NonNull
    @Override
    public SensorViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_sensor, parent, false);
        return new SensorViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull SensorViewHolder holder, int position) {
        Sensor sensor = listSensor.get(position);
        if (sensor == null) {
            return;
        }
        holder.tvTimestamp.setText(sensor.getTimestamp());
        holder.tvData.setText(sensor.getData());
      /*  holder.tvTimestamp.setText(sensor.getTimestamp());
        holder.tvInfo.setText(sensor.getInfo().get(0) + " đã mở cửa!");
        List<String> listImg = sensor.getImageEncodedPred();
        byte[] bytes = Base64.decode(listImg.get(0),Base64.DEFAULT);
        Bitmap bitmap = BitmapFactory.decodeByteArray(bytes,0,bytes.length);
        holder.imgImage.setImageBitmap(bitmap);*/
    }

    @Override
    public int getItemCount() {
        if (listSensor != null) {
            return listSensor.size();
        }
        return 0;
    }

    public static class SensorViewHolder extends RecyclerView.ViewHolder {
        private final TextView tvTimestamp;
        private final TextView tvData;
        public SensorViewHolder(@NonNull View itemView) {
            super(itemView);
            tvTimestamp = itemView.findViewById(R.id.tv_time);
            tvData = itemView.findViewById(R.id.tv_data);
        }
    }
}
