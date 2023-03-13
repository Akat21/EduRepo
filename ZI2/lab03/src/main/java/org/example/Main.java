package org.example;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Connection;
import java.sql.ResultSet;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        
        
        try{
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/zi2", "root", "KakaPL1234");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM tabela");
            while(rs.next()){
                System.out.println(rs.getString("napis") + " " + rs.getInt("liczba"));
            }
        } catch (SQLException ex){
            System.out.println("Error: " + ex.getMessage());
        }

    }
}