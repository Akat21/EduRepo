package pl.edu.zut.po.wzorce.czujniki.adapterobiektowy;
import java.lang.Math;

public class AdapterObiektowy implements CzujnikPogodowy{
    private WeatherSensor weatherSensor;

    public AdapterObiektowy(WeatherSensor weatherSensor){
        this.weatherSensor = weatherSensor;
    }

    public double pobierzTemperature(){
        return Math.round(((weatherSensor.readTemp()-32)/1.8) * 100/100.0d);
    }

    public double pobierzCisnienie(){
        return Math.round((weatherSensor.readPressure()*1000) * 100/100.0d);
    }

    public double pobierzWilgotnosc(){
        return weatherSensor.readHumidity() * 100;
    }

}