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
import com.example.smarthomeapp.R;

import java.util.List;

public class NotificationAdapter extends RecyclerView.Adapter<NotificationAdapter.NotificationViewHolder>{
    private final List<Notification> listNotification;

    public NotificationAdapter(List<Notification> listNotification) {
        this.listNotification = listNotification;
    }

    @NonNull
    @Override
    public NotificationViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_notification,parent,false);
        return new NotificationViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull NotificationViewHolder holder, int position) {
        Notification notification = listNotification.get(position);
        if(notification == null)
        {
            return;
        }
        holder.tvTimestamp.setText(notification.getTimestamp());
        holder.tvInfo.setText(notification.getDescription() + " đã mở cửa!");
        String encodedImage = notification.getImage_encoded_pred();
        if(encodedImage != null && !encodedImage.equals("img_encode_pred") && !encodedImage.equals("")) {
            byte[] bytes = Base64.decode(encodedImage, Base64.DEFAULT);
            Bitmap bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.length);
            holder.imgImage.setImageBitmap(bitmap);
        }
    }

    @Override
    public int getItemCount() {
        if(listNotification != null)
        {
            return listNotification.size();
        }
        return 0;
    }

    public static class NotificationViewHolder extends RecyclerView.ViewHolder{
        private final TextView tvTimestamp;
        private final TextView tvInfo;
        private final ImageView imgImage;
        public NotificationViewHolder(@NonNull View itemView) {
            super(itemView);
            tvTimestamp = itemView.findViewById(R.id.tv_timestamp);
            tvInfo = itemView.findViewById(R.id.tv_info);
            imgImage = itemView.findViewById(R.id.img_image);
        }
    }


}
