package pl.edu.zut.wo.wzorce.pilot.polecenia;

import pl.edu.zut.wo.wzorce.pilot.sterowniki.Światło;

public class PolecenieŚciemnijŚwiatło implements Polecenie {
	Światło światło;

	public PolecenieŚciemnijŚwiatło(Światło światło) {
		super();
		this.światło = światło;
	}
	
	@Override
	public void wycofaj() {
		światło.wyłącz();
	}

	@Override
	public void wykonaj() {
		światło.ściemnij(5);
		
	}
}
