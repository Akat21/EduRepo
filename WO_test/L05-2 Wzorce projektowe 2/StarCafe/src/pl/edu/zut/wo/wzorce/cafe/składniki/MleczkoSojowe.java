package pl.edu.zut.wo.wzorce.cafe.składniki;

import pl.edu.zut.wo.wzorce.cafe.napoje.Napój;

public class MleczkoSojowe extends SkładnikDekorator {

	Napój napój;
	
	public MleczkoSojowe(Napój nap) {napój = nap;}
	@Override
	public String pobierzOpis() {
		
		return napój.pobierzOpis()+ " Składnik: Mleczko Sojowe.";
	}

	public double koszt() {
		return napój.koszt() + 0.15 ; 
	}
}
