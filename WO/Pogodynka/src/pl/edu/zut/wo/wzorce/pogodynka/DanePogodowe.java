package pl.edu.zut.wo.wzorce.pogodynka;

import java.io.BufferedWriter;
import java.util.ArrayList;

public class DanePogodowe implements Podmiot {
	private float temperatura;
	private float wilgotność;
	private float ciśnienie;

	private ArrayList<Obserwator> obserwatorzy = new ArrayList<>();

	public void zarejestrujObserwatora(Obserwator obs){
		obserwatorzy.add(obs);
	}

	public void usuńObserwatora(Obserwator obs){
		obserwatorzy.remove(obs);
	}

	public void powiadomObserwatorów(float temp, float wilg, float cis){
		for (Obserwator o : obserwatorzy){
			o.aktualizacja(temp, wilg, cis);
		}
	}

	public void odczytyZmiana(){
		float temp = pobierzTemperaturę();
		float wilg = pobierzWilgotność();///po co te metody?
		float cis = pobierzCiśnienie();
		powiadomObserwatorów(temp, wilg, cis);
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

	public void ustawOdczyty(float temperatura, float wilgotność, float ciśnienie) {
		this.temperatura = temperatura;
		this.wilgotność = wilgotność;
		this.ciśnienie = ciśnienie;
		odczytyZmiana();
	}
	
}
