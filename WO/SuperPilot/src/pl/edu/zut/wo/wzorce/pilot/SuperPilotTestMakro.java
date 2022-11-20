package pl.edu.zut.wo.wzorce.pilot;

import pl.edu.zut.wo.wzorce.pilot.polecenia.*;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class SuperPilotTestMakro extends SuperPilot{

    public void main(String[] args){
        SuperPilot superPilot = new SuperPilot();
        Światło salonŚwiatło = new Światło("Salon");
		Światło kuchniaŚwiatło = new Światło("Kuchnia");
        WieżaStereo wieżaStereo = new WieżaStereo(null);
        TV tv = new TV(null);
        Jacuzzi jaccuzi = new Jacuzzi();

        Polecenie salonŚwiatłoWłącz = new PolecenieWłączŚwiatło(salonŚwiatło);
		Polecenie salonŚwiatłoWyłącz = new PolecenieWyłączŚwiatło(salonŚwiatło);
		Polecenie kuchniaŚwiatłoWłącz = new PolecenieWłączŚwiatło(kuchniaŚwiatło);
		Polecenie kuchniaŚwiatłoWyłącz = new PolecenieWyłączŚwiatło(kuchniaŚwiatło);
        Polecenie włączTV = new WłączTV(tv);
        Polecenie wyłączTV = new WyłączTV(tv);
        Polecenie wieżaStereoWłączCD = new WieżaStereoWłączCD(wieżaStereo);
		Polecenie wyłączWieżaStereo = new WyłączWieżaStereo(wieżaStereo);
        Polecenie wieżaStereoWłączDVD = new WieżaStereoWłączDVD(wieżaStereo);

        Polecenie[] włączŚwiatła = {salonŚwiatłoWłącz, kuchniaŚwiatłoWłącz};
        Polecenie[] wyłączŚwiatła = {salonŚwiatłoWyłącz, kuchniaŚwiatłoWyłącz};

        Polecenie[] włączImpreza = {włączTV,  wieżaStereoWłączCD};
        MakroPolecenie włączWszystkieŚwiatła = new MakroPolecenie(włączŚwiatła);
		MakroPolecenie wyłączWszystkieŚwiatła = new MakroPolecenie(wyłączŚwiatła);

        Polecenie[] włączTViWieże = {włączTV, wieżaStereoWłączCD};
        Polecenie[] przełączDVD = {wieżaStereoWłączDVD, wieżaStereoWłączCD};
        MakroPolecenie włączTViWieżeStereo = new MakroPolecenie(włączTViWieże);
        MakroPolecenie przełączNaDVD = new MakroPolecenie(przełączDVD);
        
        superPilot.ustawPolecenie(5, włączWszystkieŚwiatła, wyłączWszystkieŚwiatła);
        
    }
}
