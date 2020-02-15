package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

// Project Euler #24: Lexicographic permutations

func computeFactorials(N int64) []big.Int {
	fs := make([]big.Int, N+1)
	fs[0] = *big.NewInt(0)
	fs[1] = *big.NewInt(0)
	fs[2] = *big.NewInt(1)
	var i int64
	for i = 3; i <= N; i++ {
		z := big.NewInt(1)
		z.Mul(&fs[i-1], big.NewInt(i-1))
		fs[i] = *z
	}
	return fs
}

func getNumbers(N int) []int {
	ns := make([]int, N)
	for i := 1; i <= N; i++ {
		ns[i-1] = i
	}
	return ns
}

func getNewNumbers(numbers []int, z int) []int {
	n, x := make([]int, len(numbers)-1), 0

	for i := 0; i < len(numbers); i++ {
		if i == z {
			continue
		}
		n[x] = numbers[i]
		x++
	}

	return n
}

func getNextDigitIndex(N, f big.Int) (int, *big.Int) {
	q, m := big.NewInt(0), big.NewInt(0)
	q.DivMod(&N, &f, m)
	if m.Cmp(big.NewInt(1)) >= 0 {
		q.Add(q, big.NewInt(1))
	}
	newNum := big.NewInt(1)
	newNum.Set(q)
	newNum.Sub(newNum, big.NewInt(1))
	newNum.Mul(newNum, &f)
	newNum.Add(newNum, big.NewInt(1))
	newNum.Sub(newNum, big.NewInt(1))
	return int(q.Int64()), (&N).Sub(&N, newNum)
}

func getChar(n int) string {
	return string(96 + n)
}

func solve(N *big.Int, digits int, numbers []int, f []big.Int) string {
	answer, index := "", -1

	for j := digits; j > 1; j-- {
		index, N = getNextDigitIndex(*N, f[j])
		answer += getChar(numbers[index-1])
		numbers = getNewNumbers(numbers, index-1)
	}
	answer += getChar(numbers[0])

	return answer
}

func main() {

	digits := 13

	f := computeFactorials(int64(digits + 1))

	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		T, _ := strconv.Atoi(scanner.Text())
		for T > 0 {
			if scanner.Scan() {
				N := big.NewInt(1)
				N.SetString(scanner.Text(), 10)
				numbers := getNumbers(digits)

				fmt.Println(solve(N, digits, numbers, f))

				T--
			}
		}
	}
}
