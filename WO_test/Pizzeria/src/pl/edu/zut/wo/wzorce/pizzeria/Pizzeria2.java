package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.pizza.GreckaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.PepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SerowaPizza;

public class Pizzeria2 {
	Pizza zamówPizza(String type) {
		Pizza pizza;
		pizza = utwórzPizza(type);
		pizza.przygotowanie();
		pizza.pieczenie();
		pizza.krojenie();
		pizza.pakowanie();
		return pizza;
	}

	private Pizza utwórzPizza(String type) {
		// TODO Auto-generated method stub
		return null;
	}
}
