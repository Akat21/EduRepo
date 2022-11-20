package pl.edu.zut.wo.wzorce.pilot.polecenia;

import pl.edu.zut.wo.wzorce.pilot.sterowniki.WentylatorSufitowy;

public class WentylatorSufitowyWyłącz implements Polecenie {
    WentylatorSufitowy wentylatorSufitowy;

    public WentylatorSufitowyWyłącz(WentylatorSufitowy wentylatorSufitowy){
        super();
        this.wentylatorSufitowy = wentylatorSufitowy;
    }

    public void wykonaj() {
		wentylatorSufitowy.off();
	}

	@Override
	public void wycofaj() {
		wentylatorSufitowy.szybko();
	}
}
