import java.io.*;
import java.util.*;
import java.math.*;
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section1
public class Solution {
    // using log_10 + 1 ti find number of digits in fibonacci
    public static int dig_fib(int n) {
        double phi = (1+Math.sqrt(5))/2;
        return (int)Math.ceil(n*Math.log10(phi) - 0.5*Math.log10(5));
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        double phi = (1+Math.sqrt(5))/2;
        double neg_phi = (1-Math.sqrt(5))/2;
        // original formula F(n) = (phi^n - neg_phi^n) / (phi - neg_phi)
        // approx.          F(n) = round(phi^n/sqrt(5)) i.e. phi-neg_phi = sqrt(5)
        int[] count = new int[5001];
        count[1] = 1;
        int prev = 1;
        int current = -1;
        for (int i=2;i<28000;i++) {
            current = dig_fib(i);
            if (current != prev) {
                count[current] = i;
                prev = current;
            }
            if (current == 5000) break;
        }


        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(count[n]);
        }
    }
}
