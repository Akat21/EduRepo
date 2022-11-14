package pl.edu.zut.wo.wzorce.pilot;

import pl.edu.zut.wo.wzorce.pilot.polecenia.BrakPolecenia;
import pl.edu.zut.wo.wzorce.pilot.polecenia.Polecenie;
import pl.edu.zut.wo.wzorce.pilot.polecenia.PolecenieWłączŚwiatło;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.WentylatorSufitowy;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.Światło;

public class SuperPilotProgramuj {
 
	public static void main(String[] args) {
		SuperPilot superPilot = new SuperPilot();
 
		Światło salonŚwiatło = new Światło("Salon");
		Światło kuchniaŚwiatło = new Światło("Kuchnia");
		WentylatorSufitowy wentylatorSufitowy = new WentylatorSufitowy("Salon");
		
		Polecenie salonŚwiatłoWłącz = new PolecenieWłączŚwiatło(salonŚwiatło);
		
		superPilot.ustawPolecenie(0, salonŚwiatłoWłącz, new BrakPolecenia());
  
		System.out.println(superPilot);
 
		superPilot.wciśniętoPrzyciskWłącz(0);
		superPilot.wciśniętoPrzyciskWycofaj();
		superPilot.wciśniętoPrzyciskWyłącz(0);
		superPilot.wciśniętoPrzyciskWłącz(1);
		superPilot.wciśniętoPrzyciskWyłącz(1);
		superPilot.wciśniętoPrzyciskWłącz(2);
		superPilot.wciśniętoPrzyciskWyłącz(2);
		superPilot.wciśniętoPrzyciskWłącz(3);
		superPilot.wciśniętoPrzyciskWyłącz(3);
		superPilot.wciśniętoPrzyciskWłącz(4);
		superPilot.wciśniętoPrzyciskWyłącz(4);
	}
}
