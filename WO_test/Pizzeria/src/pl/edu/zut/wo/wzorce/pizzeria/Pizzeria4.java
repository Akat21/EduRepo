package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.ProstaFabrykaPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.GreckaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.OwoceMorzaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.PepperoniPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SerowaPizza;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.WegetariańskaPizza;

public class Pizzeria4 {
	
	ProstaFabrykaPizzy fabryka;
	
	Pizzeria4(ProstaFabrykaPizzy pfp){fabryka = pfp;}
	
	Pizza zamówPizza(String type) {	
		
		return fabryka.utwórzPizza(type);
	}

}
