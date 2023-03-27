package com.example;
import java.util.List;
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

        //ADD persons
        for(int i = 0; i < 9; i++){
            Person p = new Person();
            Random rand = new Random();
            
            int age = rand.nextInt(51);
            p.setAge(age);
            p.setFirstName("Jan");
            p.setFamilyName("Kowalski");

            em.getTransaction().begin();
            em.persist(p);
            em.getTransaction().commit();
        }

        //RESULTS 1
        Query q = em.createQuery("SELECT p FROM Person p", Person.class);
        List <Person> people = q.getResultList();
        for(Person prsn : people){
            System.out.println(prsn.getFirstName() + " " + prsn.getFamilyName() + " " + prsn.getAge());
        }
        
        System.out.println("\n");
        
        //RESULTS 2
        q = em.createQuery("SELECT p FROM Person p", Person.class);
        people = q.getResultList();
        for(Person prsn : people){
            if (prsn.getAge() < 18 ){
                prsn.setAge(18);
                em.getTransaction().begin();
                em.persist(prsn);
                em.getTransaction().commit();
            }
            System.out.println(prsn.getFirstName() + " " + prsn.getFamilyName() + " " + prsn.getAge());
        }

        System.out.println("\n");

        //RESULTS 3
        q = em.createQuery("SELECT p FROM Person p WHERE p.age > 25", Person.class);
        people = q.getResultList();
        System.out.println("Number of people over 25 yo: " + people.size());
    }
}
