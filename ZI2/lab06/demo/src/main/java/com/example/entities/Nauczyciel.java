package com.example.entities;

import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;

@Entity
public class Nauczyciel {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String imie;
    private String nazwisko;

    @ManyToOne(cascade = CascadeType.ALL)
    private Klasa klasa;

    @ManyToMany(mappedBy="nauczyciele")
    private List <Przedmiot> przedmioty;

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
