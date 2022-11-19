package pl.edu.zut.wo.wzorce.fabryka_czekolady.singleton.jbloch;

public enum CzekoladowyKocioł {
	INSTANCE;
	private boolean pusty;
	private boolean ugotowany;
	// private static CzekoladowyKocioł unikalnaInstancja = new CzekoladowyKocioł();

	private CzekoladowyKocioł() {
		this.pusty = true;
		this.ugotowany = false;
		System.out.println("Utworzenie instancji Czekoladowego Kotła: " + this);
	}

	public static CzekoladowyKocioł pobierzInstancje(){
		return INSTANCE;
	}

	public void napełniaj() {
		if (jestPusty()) {
			pusty = false;
			ugotowany = false;
			// napełniaj bojler mieszanką mleka i czekolady
			System.out.println("Napełnianie bojlera mieszanką czekolady i mleka");
		}
	}

	public void opróżniaj() {
		if (!jestPusty() && jestUgotowany()) {
			// opróżniaj bojler z ugotowanej mieszanki mleka i czekolady
			System.out.println("Opróżnianie bojlera z ugotowanej mieszanki czekolady i mleka");
			pusty = true;
		}
	}

	public void gotuj() {
		if (!jestPusty() && !jestUgotowany()) {
			// gotuj zawartość kotła
			System.out.println("Gotowanie mieszanki czekolady i mleka");
			ugotowany = true;
		}
	}

	public boolean jestPusty() {
		return pusty;
	}

	public boolean jestUgotowany() {
		return ugotowany;
	}
}