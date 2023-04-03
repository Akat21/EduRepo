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
public class Przedmiot {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nazwa;
    
    @ManyToOne(cascade = CascadeType.ALL)
    private Nauczyciel nauczyciel;

    @ManyToMany(mappedBy="przedmioty")
    private List <Klasa> klasy;

    public Przedmiot(){

    }

    public Przedmiot(String nazwa){
        this.nazwa = nazwa;
    }

    public void setKlasy(List<Klasa> klasy){
        this.klasy = klasy;
    }
    
    public List <Klasa> getKlasy(){
        return this.klasy;
    }

    public Nauczyciel getNauczyciel(){
        return this.nauczyciel;
    }

    public void setNauczyciel(Nauczyciel nauczyciel){
        this.nauczyciel = nauczyciel;
    }

    public void setNazwa(String nazwa){
        this.nazwa = nazwa;
    }

    public String getNazwa(){
        return this.nazwa;
    }
}
