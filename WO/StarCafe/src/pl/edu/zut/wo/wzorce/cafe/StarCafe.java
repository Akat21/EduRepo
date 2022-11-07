package pl.edu.zut.wo.wzorce.cafe;

import pl.edu.zut.wo.wzorce.cafe.napoje.*;
import pl.edu.zut.wo.wzorce.cafe.składniki.*;

public class StarCafe {
	public static void main(String... params) {
		MocnoPalona napój = new MocnoPalona();
		System.out.println(napój.pobierzOpis() + " " + napój.koszt() + "zł");
		Czekolada czekolada = new Czekolada(napój);
		BitaŚmietana bitaŚmietana = new BitaŚmietana(czekolada);
		System.out.println(bitaŚmietana.pobierzOpis() + " " + bitaŚmietana.koszt() + "zł");
	}
}
