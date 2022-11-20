package pl.edu.zut.wo.wzorce.pilot.polecenia;

import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class PrzygotujJacuzzi implements Polecenie {
    Jacuzzi jacuzzi;

    public PrzygotujJacuzzi(Jacuzzi jacuzzi){
        super();
        this.jacuzzi = jacuzzi;
    }

    public void wykonaj() {
		jacuzzi.włączDysze();
	}

	@Override
	public void wycofaj() {
		jacuzzi.wyłączDysze();
	}    
}
