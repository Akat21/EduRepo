package pl.edu.zut.wo.wzorce.cafe.składniki;
import pl.edu.zut.wo.wzorce.cafe.napoje.*;

public class MleczkoSojowe extends SkładnikDekorator{
    private Napój napój;

    public MleczkoSojowe(Napój obj){
        this.napój = obj;
    }

    public String pobierzOpis(){
        return napój.pobierzOpis() + " Składnik: Mleczko sojowe";
    }

    public double koszt(){
        return napój.koszt() +  0.15;
    }
}