package pl.edu.zut.wo.wzorce.pizzeria;

import pl.edu.zut.wo.wzorce.pizzeria.fabryka.ProstaFabrykaPizzy;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pizza;

public class Pizzeria4 {
    private ProstaFabrykaPizzy fabryka;

    public Pizzeria4(ProstaFabrykaPizzy obj){
        this.fabryka = obj;
    }

	Pizza zamówPizza(String type) {
        return fabryka.utwórzPizza(type);
	}

}
