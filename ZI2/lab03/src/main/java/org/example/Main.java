package org.example;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

import java.sql.PreparedStatement;

import java.sql.Connection;
import java.sql.ResultSet;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        
        Connection conn; 

        try{
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/zi2", "root", "KakaPL1234");
            System.out.println("Połączono!");
            Statement stmt = conn.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS tabela (id INT NOT NULL AUTO_INCREMENT, napis TEXT, liczba INT, PRIMARY KEY(id))");
            stmt.execute("DELETE FROM tabela");
            stmt.execute("INSERT INTO tabela(napis, liczba) VALUES('someText', 12)");
            stmt.execute("INSERT INTO tabela(napis, liczba) VALUES('someText2', 125)");
            
            String[] arr = new String[] {"jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dzisiec"};
            PreparedStatement ps = conn.prepareStatement("INSERT INTO tabela(napis,liczba) VALUES(?,?)");
            for(String el : arr){
                ps.setString(1, el);
                ps.setInt(2, (int)Math.floor(Math.random() * (200 - 0 + 1) + 0));
                ps.executeUpdate();
            }

            ResultSet rs = stmt.executeQuery("SELECT * FROM tabela");
            while(rs.next()){
                System.out.println(rs.getString("napis") + " " + rs.getInt("liczba"));
            }
        } catch (SQLException ex){
            System.out.println("Error: " + ex.getMessage());
        }

    }
}