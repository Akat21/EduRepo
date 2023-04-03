package com.example;

import java.util.List;
import java.util.ArrayList;
import java.util.Random;

import com.example.entities.Klasa;
import com.example.entities.Nauczyciel;
import com.example.entities.Przedmiot;
// import com.example.entities.Przedmiot;
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

        //KLASA PIERWSZA
        Klasa k1 = new Klasa();
        k1.setNazwa("UFC");
        k1.setPoziom(3);

        //KLASA DRUGA
        Klasa k2 = new Klasa();
        k2.setNazwa("KSW");
        k2.setPoziom(4);

        //UCZNIOWIE

        Uczen u1 = new Uczen("Khabib", "Nurmagomedov");
        u1.setKlasa(k1);
        Uczen u2 = new Uczen("Mamhed", "Khalidov");
        u2.setKlasa(k2);
        Uczen u3 = new Uczen("Connor", "McGregor");
        u3.setKlasa(k1);
        Uczen u4 = new Uczen("Jon", "Jones");
        u4.setKlasa(k1);
        Uczen u5 = new Uczen("Roberto", "Soldic");
        u5.setKlasa(k2);
        
        k1.setPrzedmioty(new ArrayList<Przedmiot>());
        k2.setPrzedmioty(new ArrayList<Przedmiot>());
        k1.setUczniowie(new ArrayList<Uczen>());
        k2.setUczniowie(new ArrayList<Uczen>());
        k1.getUczniowie().add(u1);
        k2.getUczniowie().add(u2);
        k1.getUczniowie().add(u3);
        k1.getUczniowie().add(u4);
        k2.getUczniowie().add(u5);

        //NAUCZYCIELE
        Nauczyciel w1 = new Nauczyciel("Dana", "White");
        Nauczyciel w2 = new Nauczyciel("Martin", "Lewandowski");

        w1.setKlasa(k1);
        w2.setKlasa(k2);
        k1.setWychowawca(w1);
        k2.setWychowawca(w2);

        //PRZEDMIOTY
        Przedmiot p1 = new Przedmiot("MMA");
        Przedmiot p2 = new Przedmiot("Boks");
        Przedmiot p3 = new Przedmiot("K1");
        
        p1.setKlasy(new ArrayList<Klasa>());
        p2.setKlasy(new ArrayList<Klasa>());
        p3.setKlasy(new ArrayList<Klasa>());

        p1.getKlasy().add(k1);
        p2.getKlasy().add(k1);
        p3.getKlasy().add(k2);

        k1.getPrzedmioty().add(p1);
        k1.getPrzedmioty().add(p2);
        k2.getPrzedmioty().add(p3);

        w1.setPrzedmioty(new ArrayList<Przedmiot>());
        w2.setPrzedmioty(new ArrayList<Przedmiot>());

        p1.setNauczyciel(w1);
        p2.setNauczyciel(w2);
        p3.setNauczyciel(w2);

        w1.getPrzedmioty().add(p1);
        w2.getPrzedmioty().add(p2);
        w2.getPrzedmioty().add(p3);

        //TRANSAKCJE
        em.getTransaction().begin();
        em.persist(k1);
        em.persist(k2);
        em.getTransaction().commit();

        Uczen uPrint = em.createQuery("SELECT u1 FROM Uczen u1", Uczen.class).getResultList().get(2);
        for(Przedmiot pPrint: uPrint.getKlasa().getPrzedmioty()){
            System.out.println(uPrint.getImie() + " " + uPrint.getNazwisko() + " "
                            + pPrint.getNazwa() + " "
                            + pPrint.getNauczyciel().getImie() + " "
                            + pPrint.getNauczyciel().getNazwisko());
        }

        Nauczyciel nPrint = em.createQuery("SELECT w1 FROM Nauczyciel w1", Nauczyciel.class).getResultList().get(0);
        for(Przedmiot pPrint1: w1.getPrzedmioty()){
            for(Klasa kPrint: pPrint1.getKlasy()){
                for(Uczen uPrint1: kPrint.getUczniowie()){
                System.out.println(nPrint.getImie() + " " + nPrint.getNazwisko() + " "
                                   + uPrint1.getImie() + " "
                                   + uPrint1.getNazwisko());
                }
            }
        }
        // for(Uczen i: uPrint.getUczniowie()){
        //     System.out.println(i.getImie() + " " + i.getNazwisko());
        // }

        // k1.setPrzedmioty(new ArrayList<Przedmiot>());
        // k2.setPrzedmioty(new ArrayList<Przedmiot>());



        // p1.setKlasy(new ArrayList<Klasa>());
        // p2.setKlasy(new ArrayList<Klasa>());
        // p3.setKlasy(new ArrayList<Klasa>());

        // w1.setPrzedmioty(new ArrayList<Przedmiot>());
        // w1.getPrzedmioty().add(p1);

        // w2.setPrzedmioty(new ArrayList<Przedmiot>());
        // w2.getPrzedmioty().add(p2);
        // w2.getPrzedmioty().add(p3);

        // p1.setNauczyciel(w1);
        // p2.setNauczyciel(w2);
        // p3.setNauczyciel(w2);
        
        // // k1.getPrzedmioty().add(p1);
        // // k1.getPrzedmioty().add(p2);
        // // k2.getPrzedmioty().add(p3);
        
        // p1.getKlasy().add(k1);
        // p2.getKlasy().add(k1);
        // p2.getKlasy().add(k2);

        // em.getTransaction().begin();
        // em.persist(k1);
        // em.persist(k2);
        // em.getTransaction().commit();

        // Klasa k1k1 = em.createQuery("SELECT k1 FROM Klasa k1", Klasa.class).getResultList().get(0);
        // for(Uczen i: k1k1.getUczniowie()){
        //     for (Przedmiot j: i.getKlasa().getPrzedmioty()){
        //         System.out.println(i.getImie() + " " + i.getNazwisko() + " " +  j.getNazwa() 
        //                            + " " + j.getNauczyciel().getImie() + " " + j.getNauczyciel().getNazwisko());
        //     }
        // }
    }
}
