import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

class Baza{
    public static void main(String[] args) throws Exception{
        System.out.println("hello world!");
        Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/zi2", "root", "KakaPL1234");
        Statement statement = conn.createStatement();
        ResultSet rs = statement.executeQuery("select * from tabela");

        while(rs.next()){
            int liczba = rs.getInt("liczba");
            String napis = rs.getString("napis");
            System.out.println(liczba + " " + napis);
        }
    }
}