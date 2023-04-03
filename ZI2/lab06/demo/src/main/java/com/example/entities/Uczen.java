package main.java.com.example.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Uczen {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String imie;
    private String nazwisko;

    @ManyToOne(cascade = CascadeType.ALL)
    private Klasa klasa;

    public Uczen(){

    }

    public Uczen(String imie, String nazwisko){
        this.imie = imie;
        this.nazwisko = nazwisko;
    }

    public Klasa getKlasa(){
        return klasa;
    }

    public void setKlasa(Klasa klasa){
        this.klasa = klasa;
    }

    public void setImie(String imie){
        this.imie = imie;
    }

    public String getImie(){
        return this.imie;
    }

    public void setNazwisko(String nazwisko){
        this.nazwisko = nazwisko;
    }

    public String getNazwisko(){
        return this.nazwisko;
    }
}
