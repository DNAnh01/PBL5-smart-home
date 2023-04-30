package com.example.smarthomeapp.Model;

public class Sensor {
    private String timestamp;
    private String data;

    public Sensor(String timestamp, String data) {
        this.timestamp = timestamp;
        this.data = data;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
}
