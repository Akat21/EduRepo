package pl.edu.zut.wo.wzorce.pilot;

import pl.edu.zut.wo.wzorce.pilot.polecenia.*;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;

public class SuperPilotTestMakro{

    public static void main(String[] args){
        SuperPilot superPilot = new SuperPilot();
        Światło salonŚwiatło = new Światło("Salon");
		Światło kuchniaŚwiatło = new Światło("Kuchnia");
        WieżaStereo wieżaStereo = new WieżaStereo("Salon");
        TV tv = new TV("Salon");
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
        Polecenie tvWłączDVD = new TVWłączDVD(tv);
        Polecenie przygotujJacuzzi = new PrzygotujJacuzzi(jaccuzi);
        Polecenie przyciemnijOświetlenie = new PolecenieŚciemnijŚwiatło(salonŚwiatło);
        Polecenie wyłączJacuzzi = new WyłączJacuzzi(jaccuzi);

        Polecenie[] włączŚwiatła = {salonŚwiatłoWłącz, kuchniaŚwiatłoWłącz};
        Polecenie[] wyłączŚwiatła = {salonŚwiatłoWyłącz, kuchniaŚwiatłoWyłącz};

        MakroPolecenie włączWszystkieŚwiatła = new MakroPolecenie(włączŚwiatła);
		MakroPolecenie wyłączWszystkieŚwiatła = new MakroPolecenie(wyłączŚwiatła);

        Polecenie[] włączTViWieże = {włączTV, wieżaStereoWłączCD};
        Polecenie[] przełączDVD = {wieżaStereoWłączDVD, tvWłączDVD};
        MakroPolecenie włączTViWieżeStereo = new MakroPolecenie(włączTViWieże);
        MakroPolecenie przełączNaDVD = new MakroPolecenie(przełączDVD);

        Polecenie[] włączImpreze = {przyciemnijOświetlenie, włączTViWieżeStereo, przełączNaDVD, przygotujJacuzzi};
        Polecenie[] wyłączImpreze = {salonŚwiatłoWyłącz, wyłączTV, wyłączWieżaStereo, wyłączJacuzzi};

        MakroPolecenie włączImprezę = new MakroPolecenie(włączImpreze);
        MakroPolecenie wyłączImprezę = new MakroPolecenie(wyłączImpreze);
        superPilot.ustawPolecenie(5, włączWszystkieŚwiatła, wyłączWszystkieŚwiatła);
        superPilot.ustawPolecenie(6, włączImprezę, wyłączImprezę);

        superPilot.wciśniętoPrzyciskWłącz(5);
		superPilot.wciśniętoPrzyciskWyłącz(5);
        superPilot.wciśniętoPrzyciskWłącz(6);
		superPilot.wciśniętoPrzyciskWyłącz(6);
    }
}
