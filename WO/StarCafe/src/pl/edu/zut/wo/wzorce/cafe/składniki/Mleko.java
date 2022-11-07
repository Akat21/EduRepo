package pl.edu.zut.wo.wzorce.cafe.składniki;
import pl.edu.zut.wo.wzorce.cafe.napoje.*;

public class Mleko extends SkładnikDekorator{
    private Napój napój;

    public Mleko(Napój obj){
        this.napój = obj;
    }

    public String pobierzOpis(){
        return napój.pobierzOpis() + " Składnik: Mleko";
    }

    public double koszt(){
        return napój.koszt() + 0.10;
    }
}
