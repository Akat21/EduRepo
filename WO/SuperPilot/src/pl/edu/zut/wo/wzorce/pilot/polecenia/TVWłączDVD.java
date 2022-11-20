package pl.edu.zut.wo.wzorce.pilot.polecenia;

import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class TVWłączDVD implements Polecenie {
    TV tv;

    public TVWłączDVD(TV tv){
        super();
        this.tv = tv;
    }

    public void wykonaj() {
		tv.ustawDVD();
	}

	@Override
	public void wycofaj() {
		tv.włącz();
	}    
}
