package com.example.entities;

import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;

@Entity
public class Nauczyciel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String imie;
    private String nazwisko;

    @OneToOne(cascade = CascadeType.ALL)
    private Klasa klasa;

    @OneToMany(cascade = CascadeType.ALL, mappedBy="nauczyciel")
    private List <Przedmiot> przedmioty;

    public Nauczyciel(){

    }

    public Nauczyciel(String imie, String nazwisko){
        this.imie = imie;
        this.nazwisko = nazwisko;
    }

    public void setPrzedmioty(List <Przedmiot> przedmioty){
        this.przedmioty = przedmioty;
    }

    public List<Przedmiot> getPrzedmioty(){
        return this.przedmioty;
    }

    public void setKlasa(Klasa klasa){
        this.klasa = klasa;
    }

    public Klasa getKlasa(){
        return this.klasa;
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
