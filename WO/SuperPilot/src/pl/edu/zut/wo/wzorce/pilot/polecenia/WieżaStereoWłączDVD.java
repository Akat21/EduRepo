package pl.edu.zut.wo.wzorce.pilot.polecenia;
import pl.edu.zut.wo.wzorce.pilot.sterowniki.*;;

public class WieżaStereoWłączDVD implements Polecenie{
    WieżaStereo wieżaStereo;

    public WieżaStereoWłączDVD(WieżaStereo wieżaStereo){
        super();
        this.wieżaStereo = wieżaStereo;
    }

    public void wykonaj() {
		wieżaStereo.ustawDVD();
	}

	@Override
	public void wycofaj() {
		wieżaStereo.włącz();
	}    
}
