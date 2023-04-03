package com.example;

import java.util.List;
import java.util.ArrayList;
import java.util.Random;

import com.example.entities.Klasa;
import com.example.entities.Uczen;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import jakarta.persistence.Query;

public class App 
{
    public static void main( String[] args )
    {
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("mb1");
        EntityManager em = emf.createEntityManager();

        Klasa k1 = new Klasa();
        k1.setNazwa("3B");
        k1.setPoziom(3);

        k1.setUczniowie(new ArrayList<Uczen>());
        Uczen u1 = new Uczen("Khabib", "Nurmagomedov");
        u1.setKlasa(k1);
        Uczen u2 = new Uczen("Mamhed", "Khalidov");
        u2.setKlasa(k1);

        k1.getUczniowie().add(u1);
        k1.getUczniowie().add(u2);

        em.getTransaction().begin();
        em.persist(k1);
        em.getTransaction().commit();

        Klasa k1k1 = em.createQuery("SELECT k1 FROM Klasa k1", Klasa.class).getResultList().get(0);
        for(Uczen i: k1k1.getUczniowie()){
            System.out.println(i.getImie() + i.getNazwisko());
        }
    }
}
