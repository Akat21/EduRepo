package pl.edu.zut.wo.wzorce.pizzeria.fabryka;

import pl.edu.zut.wo.wzorce.pizzeria.pizza.Ciasto;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Małże;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pepperoni;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Ser;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Sos;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Warzywa;

public interface FabrykaSkładnikówPizzy {

	public Ciasto utwórzCiasto();
	public Sos utwórzSos();
	public Ser utwórzSer();
	public Warzywa[] utwórzWarzywa();
	public Pepperoni utwórzPepperoni();
	public Małże utwórzMałże();
	
}
