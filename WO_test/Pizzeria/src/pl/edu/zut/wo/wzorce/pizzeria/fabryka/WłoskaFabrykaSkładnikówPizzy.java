package pl.edu.zut.wo.wzorce.pizzeria.fabryka;

import pl.edu.zut.wo.wzorce.pizzeria.pizza.Cebula;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Ciasto;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.CienkieChrupkieCiasto;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.CzerwonaPapryka;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Czosnek;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Małże;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pepperoni;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Pieczarki;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.PlastryPepperoni;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Ser;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SerReggiano;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Sos;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.SosMarinara;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.Warzywa;
import pl.edu.zut.wo.wzorce.pizzeria.pizza.ŚwieżeMałże;

public class WłoskaFabrykaSkładnikówPizzy implements FabrykaSkładnikówPizzy{

	@Override
	public Ciasto utwórzCiasto() {
	
		return new CienkieChrupkieCiasto();
	}

	@Override
	public Sos utwórzSos() {
	
		return new SosMarinara();
	}

	@Override
	public Ser utwórzSer() {
	
		return new SerReggiano();
	}

	@Override
	public Warzywa[] utwórzWarzywa() {
		Warzywa warzywa[] = { new Czosnek(), new Cebula(),
				new Pieczarki(), new CzerwonaPapryka() };
				return warzywa;
	}

	@Override
	public Pepperoni utwórzPepperoni() {

		return new PlastryPepperoni();
	}

	@Override
	public Małże utwórzMałże() {
	
		return new ŚwieżeMałże();
	}

}
