 #include <stdio.h>
 #include <math.h>
 #include <stdlib.h>
 
 void print_array(int* a, int n) {
 	int i;
	for (i=0;i<n;i++) {
		printf("%d  ", a[i]);
	}
 }
 
 int binary_search(int* a, int x, int l, int h) {
 	//printf ("================= binary_search() ====================\n");
 	if (l <= h) {
 		int m = (l + h) / 2;
 		if (a[m] == x) return 1;
 		if (x < a[m]) return binary_search(a, x, l, m-1);
 		else return binary_search(a, x, m+1, h);
 	}
 	return 0;
 }
 
 int seive (int* primes, int n) {
 	//printf ("============ seive() ============\n");
 	int* numbers = (int *)calloc(sizeof(int*), 1000007);
 	int i = 2, j = 0;
 	for (i=2; i<= (int)sqrt(n) + 1; i++) {
 		if (!numbers[i]) {
 			int p = 2 * i;
 			while (p <= n) {
 				numbers[p] = 1;
 				p += i;
 			}
 		}
 	}
 	for (i=2; i<= n; i++) {
 		if (!numbers[i]) {
 			primes[j++] = i;
		}
 	}
 	return j;
 } 
 
 int digits(int n) {
 	//printf ("================== digits() ================\n");
 	int d = 0;
 	while (n) {
 		d++;
 		n /= 10;
 	}
 	return d;
 }
 
 int power(int n, int x) {
 	//printf ("=========== power() =============\n");
 	int a = 1;
 	int p = n;
 	while (x > 1) {
		if (x&1) {
 			// odd
 			a *= n;
 			x -= 1;
 		} else {
 			// even
 			p *= p;
 			x = x >> 1;
 		}	
	}
	a *= p;
	return a;
 }
 
 int is_circular_prime(int n, int* primes, int number_of_primes) {
 	//printf ("=========== is_circular_prime() ===================\n");
	int number_of_digits = digits(n);
	int d = power(10, number_of_digits-1);
 	int i;
 	for (i=0;i<number_of_digits-1;i++) {
 		n = (n % d) * 10 + (n / d);
 		if (!binary_search(primes, n, 0, number_of_primes)) return 0;
 	}
 	return 1;
 }
 
 int main () {
 	int n = 1000000, i;

	scanf("%d",&n);

 	int* primes = (int *)calloc(sizeof(int*), n/2);
 	int number_of_primes = seive(primes, n);

 	//print_array(primes, 100);	
 	//printf("%d\n", number_of_primes);
 	//printf("%d\n", power(10, 4));
 	//printf("%d\n", is_circular_prime(197, primes, number_of_primes));
 	//printf("%d\n", is_circular_prime(23, primes, number_of_primes));
 	int c = 0;
	long long answer = 0;
	for (i=0;i<number_of_primes;i++) {
		if (is_circular_prime(primes[i], primes, number_of_primes)) {
			//printf ("%d\n", primes[i]);
			c++;
			answer += primes[i];
		}
	}
	//printf("%d\n\n", c);
	printf ("%lld", answer);
	
	return 0;
 }
