package main.java.com.example.entities;

import java.util.List;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Klasa {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nazwa;
    private int poziom;

    @OneToMany( mappedBy = "klasa", cascade = CascadeType.ALL)
    private List <Uczen> uczniowie;

    @OneToMany( mappedBy = "klasa",cascade = CascadeType.ALL)
    private Nauczyciel wychowawca;

    @ManyToMany
    private List <Przedmiot> przedmioty;

    public List<Uczen> getUczniowie(){
        return uczniowie;
    }

    public void setUczniowie(List <Uczen> uczniowie){
        this.uczniowie = uczniowie;
    }
    public void setNazwa(String nazwa){
        this.nazwa = nazwa;
    }

    public String getNazwa(){
        return this.nazwa;
    }

    public void setPoziom(int poziom){
        this.poziom = poziom;
    }

    public String getPoziom(){
        return this.poziom;
    }
}
