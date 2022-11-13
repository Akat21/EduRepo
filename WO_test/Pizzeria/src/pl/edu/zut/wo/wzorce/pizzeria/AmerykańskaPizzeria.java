package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.AmerykańskaFabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.fabryka.FabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.fabryka.WłoskaFabrykaSkładnikówPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.AmerykańskaOwoceMorzaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.AmerykańskaPepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.AmerykańskaSerowaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.AmerykańskaWegetariańskaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.OwoceMorzaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.PepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SerowaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WegetariańskaPizza;

public class AmerykańskaPizzeria extends Pizzeria {
	
		@Override
		protected Pizza utwórzPizza(String item) {
			Pizza pizza = null;
			FabrykaSkładnikówPizzy fabrykaSkładników = new AmerykańskaFabrykaSkładnikówPizzy();
			
			if (item.equals("serowa")) {
				pizza = new SerowaPizza(fabrykaSkładników);
				pizza.ustawNazwa("Amerykańska Serowa Pizza");
			
			} else if (item.equals("wegetariańska")) {
				pizza = new WegetariańskaPizza(fabrykaSkładników);
				pizza.ustawNazwa("Amerykańska Wegetariańska Pizza");
			
			} else if (item.equals("owoce morza")) {
				pizza = new OwoceMorzaPizza(fabrykaSkładników);
				pizza.ustawNazwa("Amerykańska Owoce Morza Pizza");
			
			} else if (item.equals("pepperoni")) {
				pizza = new PepperoniPizza(fabrykaSkładników);
				pizza.ustawNazwa("Amerykańska Pepperoni Pizza");
			} 
			return pizza;
			}
 

}
