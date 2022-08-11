import javax.swing.JPanel;
import javax.swing.JFrame;
import javax.swing.BorderFactory;
import java.awt.BorderLayout;
import java.awt.GridLayout;

class test extends JFrame{
    public static void main(String [] args){
      test win = new test();
      win.setSize(500,500);
      win.setVisible(true);
      win.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}