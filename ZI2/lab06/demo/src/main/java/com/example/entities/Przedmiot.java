package main.java.com.example.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Przedmiot {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nazwa;
    
    @ManyToOne(cascade = CascadeType.ALL)
    private Nauczyciel nauczyciel;

    @ManyToMany(mappedBy="przedmioty")
    private List <Klasa> klasa;

    public void setNazwa(String nazwa){
        this.nazwa = nazwa;
    }

    public String getNazwa(){
        return this.nazwa;
    }
}
