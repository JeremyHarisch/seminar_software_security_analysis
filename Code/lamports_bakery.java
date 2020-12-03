import java.util.Arrays; 

public class Bakery extends Thread {

	public int id;
	public static final int countGoal = 500;
	public static final int numberOfThreads = 2;
	public static volatile int count = 0;

	private static volatile boolean[] choosing = new boolean[numberOfThreads];
																				 
	private static volatile int[] ticket = new int[numberOfThreads];
	

	public Bakery(int id) {
		this.id = id;
	}

	public void run() {
		int scale = 2;

		for (int i = 0; i < countGoal; i++) {

			lock(id);
			// Critical-Section-Start
			count = count + 1;
			System.out.println("Thread-ID: " + id + " Count: " + count);
			// To create a realstic time buffer, since trade section is empty
			try {
				sleep((int) (Math.random() * scale));
			} catch (InterruptedException e) {}
			// Critical-Section-End
			unlock(id);			
		}
	}

	/*
	 * Main algorithm of Bakery algorithm
	 */
	public void lock(int id) {
		choosing[id] = true;

		ticket[id] = Arrays.stream(ticket).max().getAsInt() + 1;
		choosing[id] = false;

		for (int j = 0; j < numberOfThreads; j++) {

			if (j == id)
				continue;

			while (choosing[j]) { } // Waiting until other thread stops fethcing new ticket
			while (ticket[j] != 0 && (ticket[id] > ticket[j] || (ticket[id] == ticket[j] && id > j))) { } // Waiting for other thread to choose a new ticket						 
		} 
	}

	private void unlock(int id) {
		ticket[id] = 0;
	}

	public static void main(String[] args) {

		Bakery[] threads = new Bakery[numberOfThreads];

		for (int i = 0; i < threads.length; i++) {
			threads[i] = new Bakery(i);
			threads[i].start();
		}

		for (int i = 0; i < threads.length; i++) {
			try {
				threads[i].join();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}

		System.out.println("\nCount is: " + count);
		System.out.println("\nExpected: " + (countGoal * numberOfThreads));
	} 
}

/*
@Attribution:
The original Code was taken from https://github.com/LefterisXris/Lamport-s-Bakery-Algorithm-Java/blob/master/Bakery.java
On some parts it was modified, because of performance or regarding to the paper {TODO: paper link einfügen}
*/