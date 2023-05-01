package com.example.smarthomeapp.Adapter;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
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
        holder.tvDescription.setText(notification.getDescription());
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
        private final TextView tvDescription;
        public NotificationViewHolder(@NonNull View itemView) {
            super(itemView);
            tvTimestamp = itemView.findViewById(R.id.tv_timestamp);
            tvDescription = itemView.findViewById(R.id.tv_description);
        }
    }
}
