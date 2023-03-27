package com.example;
import java.util.Random;

import com.example.entities.Person;

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

        Person p = new Person();
        Random rand = new Random();
        
        Query q = em.createQuery ("SELECT count(x) FROM person x");
        int result = (int) q.getSingleResult ();

        int age = rand.nextInt(51);
        p.setAge(age);
        p.setFirstName("Jan");
        p.setFamilyName("Kowalski");

        Person p1 = new Person();
        
        age = rand.nextInt(51);
        p1.setAge(age);
        p1.setFirstName("Mariusz");
        p1.setFamilyName("Kowalczyk");

        Person p2 = new Person();
        
        age = rand.nextInt(51);
        p2.setAge(age);
        p2.setFirstName("Adam");
        p2.setFamilyName("Nowak");

        em.getTransaction().begin();
        em.persist(p);
        em.persist(p1);
        em.persist(p2);
        em.getTransaction().commit();

        for (int i = 1; i <= result; i++){
            Person p3 = em.find(Person.class, i);
            if (p3.getAge() < 18){
                p3.setAge(18);
                em.getTransaction().begin();
                em.persist(p3);
                em.getTransaction().commit();
            }
            System.out.println(p3.getFirstName() + " " + p3.getFamilyName() + " " + p3.getAge());
        }
    }
}
