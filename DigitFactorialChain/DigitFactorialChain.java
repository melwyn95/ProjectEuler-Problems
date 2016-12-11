import java.io.*;
import java.util.*;
public class DigitFactorialChain {

    public static int factorial(int n) {
        switch (n) {
            case 0: return 1;
            case 1: return 1;
            case 2: return 2;
            case 3: return 6;
            case 4: return 24;
            case 5: return 120;
            case 6: return 720;
            case 7: return 5040;
            case 8: return 40320;
            case 9: return 362880;
            default: return -1;
        }
    }

    public static void main (String[] args) throws IOException{
        int MAX = 1000000 + 7;
        int[] numbers = new int[MAX];
        ArrayList<ArrayList<Integer>> L = new ArrayList<ArrayList<Integer>>();
        for (int i=0 ; i < 61 ; i++) {
            L.add(new ArrayList<Integer>());
        }
        L.get(2).add(0);

        for (int i = 1 ; i < MAX ; i++) {
            ArrayList<Integer> f = new ArrayList<Integer>();
            int n = i;
            int sum = n;
            boolean flag = true;
            while (true) {
                f.add(sum);
                sum = 0;
                while (n > 0) {
                    sum += factorial(n % 10);
                    n /= 10;
                }
                // DP does'nt work for some reason :(
                // if (sum < MAX && numbers[sum] != 0) {
                //     numbers[i] = f.size() + numbers[sum];
                //     L.get(numbers[i]).add(i);
                //     flag = false;
                //     break;
                // }
                // System.out.println(sum);
                if (f.contains(sum)) {
                    break;
                }
                n = sum;
            }
            // System.out.println(Arrays.asList(f).toString());
            if (flag) {
                numbers[i] = f.size();
                L.get(numbers[i]).add(i);
            }
            // if (i == 174 || i == 196)
            //     System.out.println(i + " " + numbers[i]);
        }
        // System.out.println(Arrays.toString(numbers));

        // System.out.println(Arrays.asList(L).toString());

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int l = Integer.parseInt(input[1]);

            ArrayList<Integer> ans = L.get(l);
            String s = "";
            for (int i : ans) {
                if (i <= n) {
                    s += i + " ";
                }
            }
            if (s.length() == 0) {
                System.out.println(-1);
            } else {
                System.out.println(s.trim());
            }

        }

    }
}
