package pl.edu.zut.wi.wo.space;

public class Space {
	private Person defaultOwner;

	public void setDefaultOwner(Person defaultOwner){
		this.defaultOwner = defaultOwner;
	}

	public Person getDefaultOwner(){
		return this.defaultOwner;
	}
}
