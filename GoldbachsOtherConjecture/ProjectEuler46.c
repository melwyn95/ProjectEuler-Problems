#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define N 5*(100000 + 7)
#define n_primes 41540

int * seive() {
	int N_sqrt = (int) sqrt(N);
	int i, j, k = 0;
	int *number = (int *) calloc(N, sizeof(int *));
	int *primes = (int *) calloc(n_primes, sizeof(int *));
	for (i=2;i<=N_sqrt;i++) {
		if (!number[i]) {
			primes[k++] = i;
			for (j=2*i;j<=N;j+=i) {
				number[j] = 1;
			}
		}
	}
	for (i=N_sqrt+1;i<=N;i++) {
		if (!number[i]) {
			primes[k++] = i;	
		}
	}
	return primes;
}


int main() {
	int *primes = seive();
	int *number = (int *) calloc(N, sizeof(int *));
	int temp = -1, i, j;
	int t, n;
	//time_t start = time(NULL);

	for (i=1;i<n_primes;i++) {
		for (j=1;j<N;j++) {
			temp = primes[i] + (2 * j * j);
			if (temp <= N) {
				++number[temp];
			} else {
				break;
			}
		}
	}

	scanf("%d",&t);
	while (t--) {
		scanf("%d",&n);
		printf ("%d\n", number[n]);
	}

	free(primes);
	free(number);
	return 0;
}
