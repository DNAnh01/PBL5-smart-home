package com.example.smarthomeapp.Model;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class Notification {
    /*
    {
  "info_details": [
    {
      "description": "",
      "timestamp": "12:34:56",
      "image_encoded_pred": ""
    },
    {
      "description": "",
      "timestamp": "12:40:00",
      "image_encoded_pred": ""
    },
    {
      "description": "description",
      "timestamp": "2023-04-09 12:34:56",
      "image_encoded_pred": "img_encode_pred"
    }
  ],
  "notice_details_view_document_ID": "NoticeDetailsViewDocumentID"
}
     */
    private String description;
    private String timestamp;
    private String image_encoded_pred;

    public Notification(String description, String timestamp, String image_encoded_pred) {
        this.description = description;
        this.timestamp = timestamp;
        this.image_encoded_pred = image_encoded_pred;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public String getImage_encoded_pred() {
        return image_encoded_pred;
    }

    public void setImage_encoded_pred(String image_encoded_pred) {
        this.image_encoded_pred = image_encoded_pred;
    }
}
