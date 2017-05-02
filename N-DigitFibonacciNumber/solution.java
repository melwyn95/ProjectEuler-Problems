import java.io.*;
import java.util.*;

public class Solution {
    // this is where it started: base
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
    // will not use this to solve the problem but it feels good to implement it
    // again. and it feels good to revise .
    // Do check out geekforgeeks excellent site for learing
    // competitive programming..
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
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int[][] c = new int[][] {{1, 1}, {1, 0}};
        while (t-- > 0) {
            //int[][] result = ;
            System.out.println(expo(c, Integer.parseInt(br.readLine()))[0][1]);
        }
        //int[][] c = expo(new int[][]{{1, 1}, {1, 0}}, 10);
        // Try to deal with big integers in this problem to count digits
    }
}
