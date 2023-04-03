package main.java.com.example.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

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
