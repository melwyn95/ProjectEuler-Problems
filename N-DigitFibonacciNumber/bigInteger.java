import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static int power(int a, int n) {
        int pow = 1;
        while (n > 0) {
            if (n%2 == 0) {
                a *= a;
                n /= 2;
            } else {
                pow *= a;
                n -= 1;
            }
        }
        return pow;
    }
    public static int[][] expo(int[][] m, int n) {
        int[][] c = new int[][] {{1, 0}, {0, 1}};
        while (n > 0) {
            if (n%2 == 0) {
                m = multiply(m, m);
                n /= 2;
            } else {
                c = multiply(c, m);
                n -= 1;
            }
        }
        return c;
    }
    public static int[][] multiply(int[][] a, int[][] b) {
        int c1 = a[0][0] * b[0][0] + a[0][1] * b[1][0];
        int c2 = a[0][0] * b[0][1] + a[0][1] * b[1][1];
        int c3 = a[1][0] * b[0][0] + a[1][1] * b[1][0];
        int c4 = a[1][0] * b[0][1] + a[1][1] * b[1][1];
        a[0][0] = c1; a[0][1] = c2;
        a[1][0] = c3; a[1][1] = c4;
        return a;
    }
    public static BigInteger[][] multiply(BigInteger[][] a, BigInteger[][] b) {
        BigInteger c1 = a[0][0].multiply(b[0][0]).add(a[0][1].multiply(b[1][0]));
        BigInteger c2 = a[0][0].multiply(b[0][1]).add(a[0][1].multiply(b[1][1]));
        BigInteger c3 = a[1][0].multiply(b[0][0]).add(a[1][1].multiply(b[1][0]));
        BigInteger c4 = a[1][0].multiply(b[0][1]).add(a[1][1].multiply(b[1][1]));
        a[0][0] = c1; a[0][1] = c2;
        a[1][0] = c3; a[1][1] = c4;
        return a;
    }
    public static int digits(BigInteger n) {
        int d = 0;
        while (!n.equals(BigInteger.ZERO)) {
            n = n.divide(BigInteger.TEN);
            d++;
        }
        return d;
    }
    public static int scalableDigits(BigInteger n) {
        double factor = Math.log(2) / Math.log(10);
        int digitCount = (int) (factor * n.bitLength() + 1);
        if (BigInteger.TEN.pow(digitCount - 1).compareTo(n) > 0) {
            return digitCount - 1;
        }
        return digitCount;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        long start = System.currentTimeMillis();
        BigInteger[][] r = multiply(new BigInteger[][] {{new BigInteger("1"), new BigInteger("1")}, {new BigInteger("1"), new BigInteger("0")}}, new BigInteger[][] {{new BigInteger("1"), new BigInteger("1")}, {new BigInteger("1"), new BigInteger("0")}});
        for (int i=0;i<10;i++) {
            r = multiply(r, new BigInteger[][] {{new BigInteger("1"), new BigInteger("1")}, {new BigInteger("1"), new BigInteger("0")}});
            //System.out.println(r[0][1]);
            System.out.println(scalableDigits(r[0][1]));

        }
        System.out.println(System.currentTimeMillis() - start);
    }
}
