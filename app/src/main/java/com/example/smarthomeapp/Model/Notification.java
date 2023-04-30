package com.example.smarthomeapp.Model;

public class Notification {
    private String timestamp;
    private String description;
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
