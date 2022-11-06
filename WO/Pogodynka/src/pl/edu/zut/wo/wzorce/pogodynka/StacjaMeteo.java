package pl.edu.zut.wo.wzorce.pogodynka;

import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.PrognozaWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.StatystykaWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.WarunkiBieżąceWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.WyświetlIndeksCiepła;

public class StacjaMeteo {

	public static void main(String[] args) {
		DanePogodowe danePogodowe = new DanePogodowe();
		danePogodowe.zarejestrujObserwatora(new WarunkiBieżąceWyświetlanie());
		danePogodowe.zarejestrujObserwatora(new StatystykaWyświetlanie());
		danePogodowe.zarejestrujObserwatora(new PrognozaWyświetlanie());
		danePogodowe.zarejestrujObserwatora(new WyświetlIndeksCiepła());
		danePogodowe.ustawOdczyty(26.6f, 65, 1013.1f);
		//danePogodowe.ustawOdczyty(27.7f, 70, 997.0f);
		//danePogodowe.ustawOdczyty(25.5f, 90, 997.0f);

		
	}
	
}