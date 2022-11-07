package pl.edu.zut.wo.wzorce.cafe.składniki;
import pl.edu.zut.wo.wzorce.cafe.napoje.*;

public class Czekolada extends SkładnikDekorator{
    private Napój napój;

    public Czekolada(Napój obj){
        this.napój = obj;
    }

    public String pobierzOpis(){
        return napój.pobierzOpis() + " Składnik: Czekolada";
    }

    public double koszt(){
        return napój.koszt() + 0.20;
    }
}