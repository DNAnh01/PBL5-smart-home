package com.example.smarthomeapp.Model;

public class Device {
    private int status;
    private String timestamp;

    public Device(int status, String timestamp) {
        this.status = status;
        this.timestamp = timestamp;
    }
    public Device(int status)
    {
        this.status = status;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
}
