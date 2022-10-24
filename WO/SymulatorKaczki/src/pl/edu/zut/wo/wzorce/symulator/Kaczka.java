package pl.edu.zut.wo.wzorce.symulator;

public class Kaczka{
    LatanieInterfejs latanieInt;
    KwakanieInterfejs kwakanieInt;

    public void wykonajKwacz(){kwakanieInt.kwacz();}
    public void wykonajLeć(){latanieInt.leć();}
    
    void pływaj() {
    	System.out.println("Pływam jak kaczka.");
    }
    void wyświetl() {
        
    }
    

}
