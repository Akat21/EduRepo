package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.fabryka.WłoskaFabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.OwoceMorzaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.PepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SerowaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WegetariańskaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WłoskaOwoceMorzaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WłoskaPepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WłoskaSerowaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WłoskaWegetariańskaPizza;

public class WłoskaPizzeria extends Pizzeria {
	
	protected Pizza utwórzPizza(String item) {
		Pizza pizza = null;
		FabrykaSkładnikówPizzy fabrykaSkładników = new WłoskaFabrykaSkładnikówPizzy();
		
		if (item.equals("serowa")) {
			pizza = new SerowaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Włoska Pizza Serowa");
		
		} else if (item.equals("wegetariańska")) {
			pizza = new WegetariańskaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Włoska Pizza Wegetariańska");
		
		} else if (item.equals("owoce morza")) {
			pizza = new OwoceMorzaPizza(fabrykaSkładników);
			pizza.ustawNazwa("Włoska Owoce Morza Pizza");
		
		} else if (item.equals("pepperoni")) {
			pizza = new PepperoniPizza(fabrykaSkładników);
			pizza.ustawNazwa("Włoska Pepperoni Pizza");
		} 
		return pizza;
		}


}
