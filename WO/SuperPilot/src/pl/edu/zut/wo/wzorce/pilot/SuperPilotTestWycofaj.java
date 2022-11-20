package pl.edu.zut.wo.wzorce.pilot;

public class SuperPilotTestWycofaj extends SuperPilot{
    SuperPilot superPilot;

    public SuperPilotTestWycofaj(SuperPilot superPilot){
        this.superPilot = superPilot;
    }

    @Override
    public void wciśniętoPrzyciskWycofaj(){
        superPilot.wciśniętoPrzyciskWycofaj();
    }
}
