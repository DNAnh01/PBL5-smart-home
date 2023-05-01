package com.example.smarthomeapp.Model;

import com.google.gson.annotations.SerializedName;

public class Notification {
    @SerializedName("bred_for")
    private String timestamp;
    @SerializedName("breed_group")
    private String description;
    @SerializedName("life_span")
    private String images_encoded;

    public Notification(String timestamp, String description, String images_encoded) {
        this.timestamp = timestamp;
        this.description = description;
        this.images_encoded = images_encoded;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getImages_encoded() {
        return images_encoded;
    }

    public void setImages_encoded(String images_encoded) {
        this.images_encoded = images_encoded;
    }
}
