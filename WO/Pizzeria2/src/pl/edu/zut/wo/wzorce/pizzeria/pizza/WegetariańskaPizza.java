package pl.edu.zut.wo.wzorce.pizzeria.pizza;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public class WegetariańskaPizza extends Pizza {
	FabrykaSkładnikówPizzy fabrykaSkładników;

	public WegetariańskaPizza(FabrykaSkładnikówPizzy fabrykaSkładników) {
		this.fabrykaSkładników = fabrykaSkładników;
	}

	@Override
	public void przygotowanie() {
		if (nazwa == "Włoska Pizza Wegetariańska"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			Warzywa[] warzywka = {new Czosnek(), new CzerwonaPapryka()};
			warzywa = fabrykaSkładników.utwórzWarzywa(warzywka);
		}
		else if(nazwa == "Amerykańska Pizza Wegetariańska"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerParmezan(), new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			Warzywa[] warzywka = {new Bakłażan(), new Szpinak(), new CzarneOliwki()};
			warzywa = fabrykaSkładników.utwórzWarzywa(warzywka);
		} 
	}

}
