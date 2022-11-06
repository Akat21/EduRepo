package pl.edu.zut.wo.wzorce.symulator;

public class WabikKaczka extends Kaczka {
	public WabikKaczka(){
		latanieInt = new NieLatam();
		kwakanieInt = new Piszcz();
	}
	
	public void wyświetl(){
		System.out.println("Wygląda jak płaskonos");
	}
}