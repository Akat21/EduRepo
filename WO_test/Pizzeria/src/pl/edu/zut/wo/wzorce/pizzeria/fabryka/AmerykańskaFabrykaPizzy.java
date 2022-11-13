package pl.edu.zut.wo.wzorce.pizzeria.fabryka;

import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;

public class AmerykańskaFabrykaPizzy extends ProstaFabrykaPizzy {

	public Pizza utwórzPizza() {
		Pizza pizza = new Pizza();
		return pizza;}
}
