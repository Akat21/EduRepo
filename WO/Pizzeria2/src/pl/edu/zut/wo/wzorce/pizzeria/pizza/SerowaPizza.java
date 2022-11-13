package pl.edu.zut.wo.wzorce.pizzeria.pizza;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public class SerowaPizza extends Pizza {
	FabrykaSkładnikówPizzy fabrykaSkładników;

	public SerowaPizza(FabrykaSkładnikówPizzy fabrykaSkładników) {
		this.fabrykaSkładników = fabrykaSkładników;
	}

	@Override
	public void przygotowanie() {
		if (nazwa == "Włoska Pizza Serowa"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new GrubeChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
		}
		else if(nazwa == "Amerykańska Pizza Serowa"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerParmezan(), new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			Warzywa[] warzywka = {new Oregano()};
			warzywa = fabrykaSkładników.utwórzWarzywa(warzywka);
		} 
	}

}
