package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.*;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.*;


public class AmerykańskaPizzeria extends Pizzeria {
	protected Pizza utwórzPizza(String item) {
		Pizza pizza = null;
		FabrykaSkładnikówPizzy fabrykaSkładników = new AmerykańskaFabrykaSkładnikówPizzy();
		if (item.equals("serowa")) {
			pizza = new SerowaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Amerykańska Pizza Serowa");
		} else if (item.equals("wegetariańska")) {
			pizza = new WegetariańskaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Amerykańska Pizza Wegetariańska");
		} else if (item.equals("owoce morza")) {
			pizza = new OwoceMorzaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Amerykańska Pizza Owoce Morza");
		} else if (item.equals("pepperoni")) {
			pizza = new PepperoniPizza(fabrykaSkładników);
			pizza.ustawNazwa("Amerykańska Pizza Pepperoni");
		}
		return pizza;
	}
}