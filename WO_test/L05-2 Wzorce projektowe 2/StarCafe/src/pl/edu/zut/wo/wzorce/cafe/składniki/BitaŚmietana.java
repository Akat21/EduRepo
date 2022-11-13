package pl.edu.zut.wo.wzorce.cafe.składniki;

import pl.edu.zut.wo.wzorce.cafe.napoje.Napój;

public class BitaŚmietana extends SkładnikDekorator {

	Napój napój;
	
	public BitaŚmietana(Napój nap) {napój = nap;}

	@Override
	public String pobierzOpis() {
		
		return napój.pobierzOpis()+ " Składnik: BitaŚmietana.";
	}

	public double koszt() {
		return napój.koszt() + 0.10 ; 
	}
}
