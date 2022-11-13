package pl.edu.zut.wo.wzorce.pizzeria.pizza;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public class PepperoniPizza extends Pizza {
	FabrykaSkładnikówPizzy fabrykaSkładników;

	public PepperoniPizza(FabrykaSkładnikówPizzy fabrykaSkładników) {
		this.fabrykaSkładników = fabrykaSkładników;
	}

	@Override
	public void przygotowanie() {
		if (nazwa == "Włoska Pizza Pepperoni"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
		}
		else if(nazwa == "Amerykańska Pizza Pepperoni"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerParmezan(), new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			Warzywa[] warzywka = {new Oregano(), new Bakłażan(), new Szpinak(), new CzarneOliwki()};
			warzywa = fabrykaSkładników.utwórzWarzywa(warzywka);
			pepperoni = fabrykaSkładników.utwórzPepperoni(new Pepperoni());
		} 
	}

}
