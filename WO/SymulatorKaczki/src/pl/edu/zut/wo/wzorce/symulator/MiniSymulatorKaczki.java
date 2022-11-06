package pl.edu.zut.wo.wzorce.symulator;

public class MiniSymulatorKaczki {

	public static void main(String[] args) {
		Kaczka dzika = new DzikaKaczka();
		dzika.wyświetl();
		dzika.wykonajKwacz();
		dzika.wykonajLeć();
		Kaczka gumowa = new GumowaKaczka();
		gumowa.wyświetl();
		gumowa.wykonajKwacz();
		gumowa.wykonajLeć();
		ModelKaczki kaczka = new Kaczka();
		kaczka.wyświetl();
		kaczka.ustawLećInt(new LatamBoMamSkrzydla());
		kaczka.wykonajLeć();
		kaczka.ustawLećInt(new LotZNapędemRakietowym());
		kaczka.wykonajLeć();
	}
}
