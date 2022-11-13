package pl.edu.zut.wo.wzorce.pizzeria.fabryka;

import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public class AmerykańskaFabrykaSkładnikówPizzy implements FabrykaSkładnikówPizzy {
	public Ciasto utwórzCiasto(Ciasto obj) {
		return obj;
	}

	public Sos utwórzSos(Sos obj) {
		return obj;
	}

	public Ser[] utwórzSer(Ser[] obj) {
		return obj;
	}

	public Warzywa[] utwórzWarzywa(Warzywa[] obj) {
		return obj;
	}

	public Pepperoni utwórzPepperoni(Pepperoni obj) {
		return obj;
	}

	public Małże utwórzMałże(Małże obj) {
		return obj;
	}
}
