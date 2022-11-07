package pl.edu.zut.wo.wzorce.cafe.składniki;
import pl.edu.zut.wo.wzorce.cafe.napoje.*;

public class BitaŚmietana extends SkładnikDekorator{
    private Napój napój;

    public BitaŚmietana(Napój obj){
        this.napój = obj;
    }

    public String pobierzOpis(){
        return napój.pobierzOpis() + " Składnik: Bita Śmietana";
    }

    public double koszt(){
        return napój.koszt() + 0.10;
    }
}