package pl.edu.zut.wo.wzorce.symulator;

public class MiniSymulatorKaczki {

	public static void main(String[] args) {
		Kaczka dzika = new DzikaKaczka();
		dzika.wyświetl();
		dzika.kwacz();
		dzika.leć();
		Kaczka gumowa = new GumowaKaczka();
		gumowa.wyświetl();
		gumowa.kwacz();
		gumowa.leć();
	}
}
