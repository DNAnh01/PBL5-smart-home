package com.example.smarthomeapp.Model;

import java.util.List;

public class SensorView {
    private List<Sensor> gas_sensor;
    private List<Sensor> humidity_sensor;
    private List<Sensor> temperature_sensor;

    public SensorView(List<Sensor> gas_sensor, List<Sensor> humidity_sensor, List<Sensor> temperature_sensor) {
        this.gas_sensor = gas_sensor;
        this.humidity_sensor = humidity_sensor;
        this.temperature_sensor = temperature_sensor;
    }

    public List<Sensor> getGas_sensor() {
        return gas_sensor;
    }

    public void setGas_sensor(List<Sensor> gas_sensor) {
        this.gas_sensor = gas_sensor;
    }

    public List<Sensor> getHumidity_sensor() {
        return humidity_sensor;
    }

    public void setHumidity_sensor(List<Sensor> humidity_sensor) {
        this.humidity_sensor = humidity_sensor;
    }

    public List<Sensor> getTemperature_sensor() {
        return temperature_sensor;
    }

    public void setTemperature_sensor(List<Sensor> temperature_sensor) {
        this.temperature_sensor = temperature_sensor;
    }
}
