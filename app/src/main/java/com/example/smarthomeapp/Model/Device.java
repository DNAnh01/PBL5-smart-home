package com.example.smarthomeapp.Model;

public class Device {
    /*
    {
  "gatehouse_status": 0,
  "led_status": 1,
  "dc_status": 0,
  "devices_document_ID": "DevicesDocumentID"
}
     */
    private int gatehouse_status;
    private int led_status;
    private int dc_status;

    public Device(int gatehouse_status, int led_status, int dc_status) {
        this.gatehouse_status = gatehouse_status;
        this.led_status = led_status;
        this.dc_status = dc_status;
    }

    public int getGatehouse_status() {
        return gatehouse_status;
    }

    public void setGatehouse_status(int gatehouse_status) {
        this.gatehouse_status = gatehouse_status;
    }

    public int getLed_status() {
        return led_status;
    }

    public void setLed_status(int led_status) {
        this.led_status = led_status;
    }

    public int getDc_status() {
        return dc_status;
    }

    public void setDc_status(int dc_status) {
        this.dc_status = dc_status;
    }
}
