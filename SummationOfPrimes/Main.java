import java.io.*;
import java.util.*;

public class Main {
    public static int MAX = 1000000;
    public static boolean[] numbers = new boolean[MAX + 7];
    public static ArrayList<Integer> primes = new ArrayList<Integer>();

    public static void seive() {

        for (int i = 2 ; i <= (int)Math.sqrt(MAX) ; i++) {
            if (!numbers[i]) {
                for (long j = i * i ; j <= MAX  && j > 0; j += i) {
                    numbers[(int)j] = true;
                }
            }
        }

        for (int i = 2 ; i < MAX ; i++) {
            if (!numbers[i]) {
                primes.add(i);
            }
        }
        //System.out.println(Arrays.asList(primes).toString());
    }

    public static long solve(int n) {
        long answer = 0;
        for (int i : primes) {
            if (i > n) {
                break;
            }
            // System.out.println(i);
            answer += i;
        }
        return answer;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        seive();
        // System.out.println(primes.size());
        while (t-- > 0) {
            System.out.println(solve(Integer.parseInt(br.readLine())));
        }
    }
}
