import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Triangular {
	public static int MAX = 1000000 + 7;
	public static boolean[] number = new boolean[MAX];
	public static ArrayList<Integer> prime = new ArrayList<Integer>();

	public static int triangularNumber(int n) {
		return (n * (n + 1)) / 2;
	}

	public static void seive() {
		Arrays.fill(number, true);
		for (int i = 2; i < MAX; i++) {
			if (number[i]) {
				for (int j = 2 * i; j < MAX; j += i) {
					number[j] = false;
				}
			}
		}
		for (int i = 2; i < MAX; i++) {
			if (number[i]) {
				prime.add(i);
			}
		}
	}

	public static int factors(long n) {
		int index = 0;
		ArrayList<Integer> temp = new ArrayList<Integer>();
		int times = 1;
		while (n != 1) {
			if (n % prime.get(index) == 0) {
				n /= prime.get(index);
				times++;
			} else {
				index++;
				if (times != 1) {
					temp.add(times);
				}
				times = 1;
			}
			if (n == 1) {
				temp.add(times);
			}
		}
		index = 1;
		for (int time : temp) {
			index *= time;
		}
		return index;
	}

	public static void main(String[] args) throws IOException {
		seive();
		Map<Long, Integer> factor = new HashMap<>();
		for (int i = 1; i < 46341; i++) {
			long key = triangularNumber(i);
			int value = factors(key);
			factor.put(key, value);
		}
		List<Long> keySet = new ArrayList<Long>(factor.keySet());
		keySet.sort(null);
		Map<Integer, Long> solution = new HashMap<>();
		for (int i = 1; i <= 1000; i++) {
			long value = -1;
			for (long j : keySet) {
				if (factor.get(j) > i) {
					value = j;
					break;
				}
			}
			solution.put(i, value);
		}
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			int n = Integer.parseInt(br.readLine());
			System.out.println(solution.get(n));
		}
	}

}
