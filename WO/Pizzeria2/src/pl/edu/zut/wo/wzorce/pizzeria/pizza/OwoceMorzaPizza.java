package pl.edu.zut.wo.wzorce.pizzeria.pizza;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public class OwoceMorzaPizza extends Pizza {
	FabrykaSkładnikówPizzy fabrykaSkładników;

	public OwoceMorzaPizza(FabrykaSkładnikówPizzy fabrykaSkładników) {
		this.fabrykaSkładników = fabrykaSkładników;
	}

	public void przygotowanie() {
		if (nazwa == "Włoska Pizza Owoce Morza"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			małże = fabrykaSkładników.utwórzMałże(new ŚwieżeMałże());
		}
		else if(nazwa == "Amerykańska Pizza Owoce Morza"){
			System.out.println("Przygotowywanie: " + nazwa);
			ciasto = fabrykaSkładników.utwórzCiasto(new CienkieChrupkieCiasto());
			sos = fabrykaSkładników.utwórzSos(new SosPomidorowy());
			Ser[] sery = {new SerParmezan(), new SerMozzarella()};
			ser = fabrykaSkładników.utwórzSer(sery);
			małże = fabrykaSkładników.utwórzMałże(new ŚwieżeMałże());
		} 
	}
}