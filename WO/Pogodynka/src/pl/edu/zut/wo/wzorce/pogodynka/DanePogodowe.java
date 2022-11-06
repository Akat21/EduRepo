package pl.edu.zut.wo.wzorce.pogodynka;

import java.io.BufferedWriter;
import java.util.ArrayList;

import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.PrognozaWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.StatystykaWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.WarunkiBieżąceWyświetlanie;
import pl.edu.zut.wo.wzorce.pogodynka.wyświetl.WyświetlIndeksCiepła;

public class DanePogodowe implements Podmiot {
	private float temperatura;
	private float wilgotność;
	private float ciśnienie;
	private float indeksCiepla;
	private ArrayList<Obserwator> obserwatorzy = new ArrayList<>();
	
	private PrognozaWyświetlanie prognozaWyświetl = new PrognozaWyświetlanie();
	private WarunkiBieżąceWyświetlanie warunkiBieżąceWyświetl = new WarunkiBieżąceWyświetlanie();
	private StatystykaWyświetlanie statystykaWyświetl = new StatystykaWyświetlanie();
	private WyświetlIndeksCiepła indeksCiepłaWyświetl = new WyświetlIndeksCiepła();

	public void zarejestrujObserwatora(Obserwator obs){
		obserwatorzy.add(obs);
	}

	public void usuńObserwatora(Obserwator obs){
		obserwatorzy.remove(obs);
	}

	public void powiadomObserwatorów(){
		prognozaWyświetl.wyświetl();
		warunkiBieżąceWyświetl.wyświetl();
		statystykaWyświetl.wyświetl();
	}

	public void odczytyZmiana(){
		float temp = pobierzTemperaturę();
		float wilgotność = pobierzWilgotność();
		float ciśnienie = pobierzCiśnienie();
		float indeksCiepla = pobierzIndeksCiepla();
		
		warunkiBieżąceWyświetl.aktualizacja(temp, wilgotność, ciśnienie);
		statystykaWyświetl.aktualizacja(temp, wilgotność, ciśnienie);
		prognozaWyświetl.aktualizacja(temp, wilgotność, ciśnienie);
		indeksCiepłaWyświetl.aktualizacja(temp, wilgotność, ciśnienie);
	}

	private float pobierzTemperaturę(){
		return temperatura;
	}

	private float pobierzWilgotność(){
		return wilgotność;
	}

	private float pobierzCiśnienie(){
		return ciśnienie;
	}

	private float pobierzIndeksCiepla(){
		return indeksCiepla;
	}

	public void ustawOdczyty(float temperatura, float wilgotność, float ciśnienie) {
		this.temperatura = temperatura;
		this.wilgotność = wilgotność;
		this.ciśnienie = ciśnienie;
		odczytyZmiana();
	}
	
}
