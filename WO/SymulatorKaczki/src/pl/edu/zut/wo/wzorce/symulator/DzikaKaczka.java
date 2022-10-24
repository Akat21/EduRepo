package pl.edu.zut.wo.wzorce.symulator;

public class DzikaKaczka extends Kaczka {
	DzikaKaczka(){
		latanieInt = new LatamBoMamSkrzydla();
		kwakanieInt = new Piszcz();
	}
	public void wyświetl(){
		System.out.println("Wygląda jak dzika kaczka");
	}
}