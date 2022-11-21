package pl.edu.zut.po.wzorce.czujniki.adapterklasowy;
import java.lang.Math;

public class AdapterKlasowy extends WeatherSensor implements CzujnikPogodowy{
    public double pobierzTemperature(){
        return Math.round(((this.readTemp()-32)/1.8) * 100/100.0d);
    }

    public double pobierzCisnienie(){
        return Math.round((this.readPressure()*1000) * 100/100.0d);
    }

    public double pobierzWilgotnosc(){
        return this.readHumidity() * 100;
    }

}
