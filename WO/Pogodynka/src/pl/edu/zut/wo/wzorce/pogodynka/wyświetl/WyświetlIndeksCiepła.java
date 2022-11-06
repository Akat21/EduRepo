package pl.edu.zut.wo.wzorce.pogodynka.wyświetl;

import pl.edu.zut.wo.wzorce.pogodynka.Obserwator;
import pl.edu.zut.wo.wzorce.pogodynka.WyświetlElement;

public class WyświetlIndeksCiepła implements Obserwator, WyświetlElement {
    private float wilgotność;
    private float temperatura;
    private float ciśnienie;
    private float indeksCiepla;


    public void aktualizacja(float temperatura, float wilgotność, float ciśnienie){
        this.temperatura = indeksCiepla;
        this.wilgotność = wilgotność;
        this.ciśnienie = ciśnienie;
        this.indeksCiepla = computeHeatIndex(temperatura, wilgotność);
        wyświetl();
    }

    public void wyświetl(){
        System.out.println("Indeks ciepła: " + indeksCiepla);
    }

    private float computeHeatIndex(float t, float rh) {
        rh /= 100;
		float index = (float)((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) 
		+ (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) 
		+ (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
		(0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * 
		(rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + 
		(0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
		0.000000000843296 * (t * t * rh * rh * rh)) -
		(0.0000000000481975 * (t * t * t * rh * rh * rh)));
		return index;
	}
}
