package pl.edu.zut.wo.wzorce.pizzeria.pizza;

public abstract class Pizza {
	String nazwa;
	Ciasto ciasto;
	Sos sos;
	Warzywa warzywa[];
	Ser ser;
	Pepperoni pepperoni;
	Małże małże;
	public abstract void przygotowanie();
	
	

	public void pieczenie() {
		System.out.println("Pieczenie: 25 minut w temperaturze 180 stopni Celsjusza");
	}

	public void krojenie() {
		System.out.println("Krojenie pizzy na 8 kawałków");
	}

	public void pakowanie() {
		System.out.println("Pakowanie pizzy w oficjalne pudełko naszej sieci Pizzerii.");
	}
	public void ustawNazwa(String nazwa) {
		this.nazwa = nazwa;
		}
		public String pobierzNazwa() {
		return nazwa;
		}
	

}
