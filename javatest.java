import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

class app extends JFrame{
    public static void main(String [] args){
     JFrame frame = InitWindow();
     JPanel starting_panel = StartingPanel();
     frame.add(starting_panel);
    }


    public static JPanel StartingPanel(){
      JPanel panel = new JPanel();
      panel.setLayout(null);

      JButton button1 = new JButton("Click Me");
      button1.setBounds(80,80,150,40);
      button1.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e){
          button1.setText("Clicked");
        }
      });

      JLabel label1 = new JLabel("BUTTONS:");
      label1.setBounds(200,0,150,40);

      panel.add(label1);
      panel.add(button1);
      return panel;
    }

    
    public static JFrame InitWindow(){
      app win = new app();
      win.setTitle("My app");
      win.setSize(500,500);
      win.setLocationRelativeTo(null); //center the window
      win.setVisible(true);
      win.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      win.setResizable(false);
      return win;
    }
}