package pl.edu.zut.wo.wzorce.fabryka_czekolady.singleton.synchro;


public class FabrykaCzekolady {

	public static void main(String... params) {
		CzekoladowyKocioł kocioł = CzekoladowyKocioł.pobierzInstancje();
		kocioł.napełniaj();
		kocioł.gotuj();
		kocioł.opróżniaj();
	}
}
