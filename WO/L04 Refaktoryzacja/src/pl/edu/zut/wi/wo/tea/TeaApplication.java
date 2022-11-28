package pl.edu.zut.wi.wo.tea;

public class TeaApplication {

	public static void main(String[] args) {
		System.out.println(String.format("firstMethod=%.2f", ReadingRecord.firstMethod()));
		System.out.println(String.format("secondMethod=%.2f", ReadingRecord.secondMethod()));
		System.out.println(String.format("thirdMethod=%.2f", ReadingRecord.thirdMethod()));
	}
}
