package pl.edu.zut.wi.wo.invoice;

import java.time.LocalDate;

public class InvoiceManager {

	public static void printOwing(Invoice invoice) {
		double outstanding = 0;
		margin();
		// Wyliczenie należności.
		outstanding = WyliczenieNależności(invoice, outstanding);
		// Zapisanie daty płatności.
		ZapisanieDatyPłatności(invoice);
		// Wyświetlenie szczegółów.
		Wyświetlenie(invoice, outstanding);
	}

	private static void margin(){
		System.out.println("************************");
		System.out.println("* Rachunek dla klienta *");
		System.out.println("************************");
	}
	private static double WyliczenieNależności(Invoice invoice, double outstanding){
		for (Order o : invoice.getOrders()) {
			outstanding += o.getAmount();
		}
		return outstanding;
	}

	private static void ZapisanieDatyPłatności(Invoice invoice){
		LocalDate today = LocalDate.now();  
		invoice.setDueDate(today.plusDays(30));
	}

	private static void Wyświetlenie(Invoice invoice, double outstanding){
		System.out.println(String.format("nazwa: %s", invoice.getCustomer()));
		System.out.println(String.format("kwota: %.2f", outstanding));
		System.out.println(String.format("płatność do: %s", invoice.getDueDate()));
	}

}
