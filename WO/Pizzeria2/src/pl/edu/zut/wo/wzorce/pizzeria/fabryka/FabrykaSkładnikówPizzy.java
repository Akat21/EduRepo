package pl.edu.zut.wo.wzorce.pizzeria.fabryka;

import pl.edu.zut.wo.wzorce.pizzeria.składniki.*;

public interface FabrykaSkładnikówPizzy {
	public Ciasto utwórzCiasto(Ciasto obj);

	public Sos utwórzSos(Sos obj);

	public Ser[] utwórzSer(Ser obj[]);

	public Warzywa[] utwórzWarzywa(Warzywa[] obj);

	public Pepperoni utwórzPepperoni(Pepperoni obj);

	public Małże utwórzMałże(Małże obj);
}