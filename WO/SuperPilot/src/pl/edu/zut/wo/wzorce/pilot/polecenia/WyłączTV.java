package pl.edu.zut.wo.wzorce.pilot.polecenia;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class WyłączTV implements Polecenie {
    TV tv;

    public WyłączTV(TV tv){
        super();
        this.tv = tv;
    }

    public void wykonaj() {
		tv.wyłącz();
	}

	@Override
	public void wycofaj() {
		tv.włącz();
	}    
}
