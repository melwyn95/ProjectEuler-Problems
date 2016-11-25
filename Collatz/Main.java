import java.io.*;
import java.util.*;
public class Main {
    public static int MAX = 5000000 + 7;
    public static long[] longestCollatzSequence = new long[MAX];
    public static long[] collatzSequence = new long[MAX];
    public static long maxCollatzSequenceLength = -1;
    public static long maxCollatz = -1;

    public static long newCountCollatz(long n, long count, long currentN) {
        if (n == 1) {
            return count;
        }
        while (n > 1) {
            if ((n & 1) == 1) {
                count++;
                n = 3 * n + 1;
            } else {
                count++;
                n /= 2;
            }
            if (n < currentN) {
                return longestCollatzSequence[(int)n] + count;
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException{
        longestCollatzSequence[0] = -1;
        collatzSequence[0] = -1;
        long currentCollatzSequenceLength = -1;
        for (int i=1; i < MAX ; i++) {
            currentCollatzSequenceLength = newCountCollatz(i, 0, i);

            if ( maxCollatzSequenceLength <= currentCollatzSequenceLength ) {
                maxCollatzSequenceLength = currentCollatzSequenceLength;
                maxCollatz = i;
                longestCollatzSequence[i] = maxCollatzSequenceLength;
                collatzSequence[i] = maxCollatz;
            } else {
                longestCollatzSequence[i] = currentCollatzSequenceLength;
                collatzSequence[i] = maxCollatz;
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            long n = Integer.parseInt(br.readLine());
            System.out.println(collatzSequence[(int)n]);
        }
    }
}
