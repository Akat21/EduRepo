package pl.edu.zut.wo.wzorce.cafe.składniki;

import pl.edu.zut.wo.wzorce.cafe.napoje.Napój;

public class Czekolada extends SkładnikDekorator{

	Napój napój;
	
	public Czekolada(Napój nap) { napój = nap;}

	@Override
	public String pobierzOpis() {
	
		return napój.pobierzOpis() + " Składnik: Czekolada.";
	}

	public double koszt() {
		return napój.koszt() + 0.20 ; 
	}
	
	
}
