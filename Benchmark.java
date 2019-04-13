/*
 * https://stackoverflow.com/questions/53452713/why-is-2-i-i-faster-than-2-i-i-in-java
 */

public class Benchmark {
	public static void main(String[] args) {
	    long startTime = System.nanoTime();
	    int n = 0;
	    for (int i = 0; i < 1000000000; i++) {
	        // n += (2 * i) * i;
	        n += 2 * (i * i);
	    }
	    System.out.println((double) (System.nanoTime() - startTime) / 1000000000 + " s");
	    System.out.println("n = " + n);
	}
}