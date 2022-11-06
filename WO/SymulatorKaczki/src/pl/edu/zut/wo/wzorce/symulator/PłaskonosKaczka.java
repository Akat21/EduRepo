package pl.edu.zut.wo.wzorce.symulator;

public class PłaskonosKaczka extends Kaczka {
	public PłaskonosKaczka(){
		latanieInt = new LatamBoMamSkrzydla();
		kwakanieInt = new Kwacz();
	}
	
	public void wyświetl(){
		System.out.println("Wygląda jak płaskonos");
	}
}