package pl.edu.zut.wi.wo.driver;

public class DriverMain {

	public static void main(String[] args) {
		DriverMain dm = new DriverMain();
		Driver driver = new Driver("jan kowalski", 6);
		dm.rate(driver);
	}

	private void rate(Driver driver){
		if (driver.getLateDeliveries() > 5)
			System.out.println("driver: " + driver.getName() + ", rating: 2");	
		else
			System.out.println("driver: " + driver.getName() + ", rating: 1");
	}
}
