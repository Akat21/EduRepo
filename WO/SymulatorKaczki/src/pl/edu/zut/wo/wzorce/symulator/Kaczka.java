package pl.edu.zut.wo.wzorce.symulator;

public class Kaczka extends ModelKaczki{
    LatanieInterfejs latanieInt;
    KwakanieInterfejs kwakanieInt;

    public void ustawKwaczInt(KwakanieInterfejs zachowanie){
        kwakanieInt = zachowanie;
    };

    public void ustawLećInt(LatanieInterfejs zachowanie){
        latanieInt = zachowanie;
    };

    public void wykonajKwacz(){
        kwakanieInt.kwacz();
    };

    public void wykonajLeć(){
        latanieInt.leć();
    };
    
    void pływaj() {
    	System.out.println("Pływam jak kaczka.");
    };

    public void wyświetl() {
        System.out.println("Jestem Kaczką");
    };
    

}
