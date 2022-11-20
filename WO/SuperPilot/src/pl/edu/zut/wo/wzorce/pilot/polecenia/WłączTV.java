package pl.edu.zut.wo.wzorce.pilot.polecenia;

import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class WłączTV implements Polecenie {
    TV tv;

    public WłączTV(TV tv){
        super();
        this.tv = tv;
    }

    public void wykonaj() {
		tv.włącz();
	}

	@Override
	public void wycofaj() {
		tv.wyłącz();
	}    
}
