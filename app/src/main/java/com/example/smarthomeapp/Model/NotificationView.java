package com.example.smarthomeapp.Model;

import java.util.List;

public class NotificationView {
    private List<Notification> info_details;

    public NotificationView(List<Notification> info_details) {
        this.info_details = info_details;
    }

    public List<Notification> getInfo_details() {
        return info_details;
    }

    public void setInfo_details(List<Notification> info_details) {
        this.info_details = info_details;
    }
}
