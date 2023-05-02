package com.example.smarthomeapp.Model;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Notification {
    @SerializedName("timestamp")
    private String timestamp;

    @SerializedName("info")
    private List<String> info;

    @SerializedName("image_encoded_pred")
    private List<String> imageEncodedPred;

    public Notification(String timestamp, List<String> info, List<String> imageEncodedPred) {
        this.timestamp = timestamp;
        this.info = info;
        this.imageEncodedPred = imageEncodedPred;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public List<String> getInfo() {
        return info;
    }

    public void setInfo(List<String> info) {
        this.info = info;
    }

    public List<String> getImageEncodedPred() {
        return imageEncodedPred;
    }

    public void setImageEncodedPred(List<String> imageEncodedPred) {
        this.imageEncodedPred = imageEncodedPred;
    }
}
