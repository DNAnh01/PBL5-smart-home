package com.example.smarthomeapp.Model;

public class SensorDetail {
   /* {
        "timestamp": "12:34:56",
            "temperature_sensor_data": 32,
            "humidity_sensor_data": 71,
            "gas_sensor_data": 0
    }
     */
    private String temperature_sensor_data;
    private String humidity_sensor_data;
    private String gas_sensor_data;

    public SensorDetail(String temperature_sensor_data, String humidity_sensor_data, String gas_sensor_data) {
        this.temperature_sensor_data = temperature_sensor_data;
        this.humidity_sensor_data = humidity_sensor_data;
        this.gas_sensor_data = gas_sensor_data;
    }

    public String getTemperature_sensor_data() {
        return temperature_sensor_data;
    }

    public void setTemperature_sensor_data(String temperature_sensor_data) {
        this.temperature_sensor_data = temperature_sensor_data;
    }

    public String getHumidity_sensor_data() {
        return humidity_sensor_data;
    }

    public void setHumidity_sensor_data(String humidity_sensor_data) {
        this.humidity_sensor_data = humidity_sensor_data;
    }

    public String getGas_sensor_data() {
        return gas_sensor_data;
    }

    public void setGas_sensor_data(String gas_sensor_data) {
        this.gas_sensor_data = gas_sensor_data;
    }


}
