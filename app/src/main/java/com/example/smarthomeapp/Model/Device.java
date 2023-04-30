package com.example.smarthomeapp.Model;

public class Device {
    private Boolean status;

    public Device(Boolean status) {
        this.status = status;
    }

    public Boolean getStatus() {
        return status;
    }

    public void setStatus(Boolean status) {
        this.status = status;
    }
}
