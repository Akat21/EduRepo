package pl.edu.zut.wo.wzorce.cafe;

import pl.edu.zut.wo.wzorce.cafe.napoje.MocnoPalona;
import pl.edu.zut.wo.wzorce.cafe.składniki.BitaŚmietana;
import pl.edu.zut.wo.wzorce.cafe.składniki.Czekolada;

public class StarCafe {
	public static void main(String... params) {
		MocnoPalona napój = new MocnoPalona();
		System.out.println(napój.pobierzOpis() + " " + napój.koszt() + "zł");
		
		Czekolada czekolada = new Czekolada(napój);
		System.out.println(czekolada.pobierzOpis() + " " + czekolada.koszt() + "zł");
		
		BitaŚmietana bitaŚmietana = new BitaŚmietana(czekolada);
		System.out.println(bitaŚmietana.pobierzOpis() + " " + bitaŚmietana.koszt() + "zł");
		
		
	}
}
