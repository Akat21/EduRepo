package pl.edu.zut.wi.wo.order;

public class OrderCalculator {

	public static double price(Order order) {
		// Cena ko�cowa = cena bazowa � upust + koszt wysy�ki.
		final double getQuantity = order.getQuantity();
		final double getItemPrice = order.getItemPrice();

		final double cena_bazowa = getQuantity * getItemPrice;
		final double upust = Math.max(0, getQuantity - 500) * getItemPrice * 0.05;
		final double koszt_wysyłki = Math.min(getQuantity * getItemPrice * 0.1, 100);

		return cena_bazowa + upust + koszt_wysyłki;
	}
}
