import java.io.*;
import java.util.*;


// Do By 1 / 0 Knapsack
// Found a good algorithms tutorials site http://algorithms.tutorialhorizon.com.


public class PrimeSummations {
    public static boolean[] primes = new boolean[1007];

    public static int[] seive() {
        int[] prime = new int[168];
        primes[0] = !false;
        primes[1] = !false;
        for (int i=2 ;i < 1007; i++) {
            if (!primes[i]) {
                for (int j=i*i ;j < 1007; j += i) {
                    primes[j] = !false;
                }
            }
        }
        int count = 0;
        for (int i=0 ;i<1007; i++) {
            if (!primes[i]) {
                prime[count++] = i;
            }
        }
        // System.out.println("Primes = " + count);
        return prime;
    }
    public static void main(String[] args) {
        int[] primeArray = new int[168];
        primeArray = seive();

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt9br.readLine();
            int digits = n / 2;
            while (digits > 0) {

            }
        }
    }
}
