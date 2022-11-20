package pl.edu.zut.wo.wzorce.pilot.polecenia;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class WyłączJacuzzi implements Polecenie{
    Jacuzzi jacuzzi;

    public WyłączJacuzzi(Jacuzzi jacuzzi){
        super();
        this.jacuzzi = jacuzzi;
    }

    public void wykonaj() {
		jacuzzi.wyłącz();
	}

	@Override
	public void wycofaj() {
		jacuzzi.włączDysze();
	}    
}
