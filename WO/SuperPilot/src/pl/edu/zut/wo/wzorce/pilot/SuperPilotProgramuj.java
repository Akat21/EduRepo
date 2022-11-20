package pl.edu.zut.wo.wzorce.pilot;

import pl.edu.zut.wo.wzorce.pilot.polecenia.*;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.DrzwiGarażu;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.WentylatorSufitowy;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.WieżaStereo;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.Światło;

public class SuperPilotProgramuj {
 
	public static void main(String[] args) {
		SuperPilot superPilot = new SuperPilot();
		SuperPilotTestWycofaj superPilotTestWycofaj = new SuperPilotTestWycofaj(superPilot);
 
		Światło salonŚwiatło = new Światło("Salon");
		Światło kuchniaŚwiatło = new Światło("Kuchnia");
		WentylatorSufitowy wentylatorSufitowy = new WentylatorSufitowy("Salon");
		DrzwiGarażu drzwiGarażu = new DrzwiGarażu(null);
		WieżaStereo wieżaStereo = new WieżaStereo(null);
	
		Polecenie salonŚwiatłoWłącz = new PolecenieWłączŚwiatło(salonŚwiatło);
		Polecenie salonŚwiatłoWyłącz = new PolecenieWyłączŚwiatło(salonŚwiatło);
		Polecenie kuchniaŚwiatłoWłącz = new PolecenieWłączŚwiatło(kuchniaŚwiatło);
		Polecenie kuchniaŚwiatłoWyłącz = new PolecenieWyłączŚwiatło(kuchniaŚwiatło);
		Polecenie wentylatorSufitowyWysokieObroty = new WentylatorSufitowyWysokieObroty(wentylatorSufitowy);
		Polecenie wentylatorSufitowyWyłącz = new WentylatorSufitowyWyłącz(wentylatorSufitowy);
		Polecenie otwórzDrzwiGarażowe = new OtwórzDrzwiGarażowe(drzwiGarażu);
		Polecenie zamknijDrzwiGarażowe = new ZamknijDrzwiGarażowe(drzwiGarażu);
		Polecenie wieżaStereoWłączCD = new WieżaStereoWłączCD(wieżaStereo);
		Polecenie wyłączWieżaStereo = new WyłączWieżaStereo(wieżaStereo);

		superPilot.ustawPolecenie(0, salonŚwiatłoWłącz, salonŚwiatłoWyłącz);
		superPilot.ustawPolecenie(1, kuchniaŚwiatłoWłącz, kuchniaŚwiatłoWyłącz);
		superPilot.ustawPolecenie(2, wentylatorSufitowyWysokieObroty, wentylatorSufitowyWyłącz);
		superPilot.ustawPolecenie(3, otwórzDrzwiGarażowe, zamknijDrzwiGarażowe);
		superPilot.ustawPolecenie(4, wieżaStereoWłączCD, wyłączWieżaStereo);

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
		
		superPilot.wciśniętoPrzyciskWłącz(3);
		superPilotTestWycofaj.wciśniętoPrzyciskWycofaj();
		superPilot.wciśniętoPrzyciskWłącz(4);
		superPilotTestWycofaj.wciśniętoPrzyciskWycofaj();
	}
}
