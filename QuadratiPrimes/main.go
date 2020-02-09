package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Soln struct {
	max, a, b int
}

var cache map[int]Soln

func isPrime(n int) bool {
	if n == 0 || n == 1 || n < 0 {
		return false
	}
	sqrt := int(math.Ceil(math.Sqrt(float64(n)))) + 1
	for i := 2; i < sqrt; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func getEqn(a, b int) func(int) int {
	return func(n int) int {
		return n*n + a*n + b
	}
}

func generatePrimes(a, b int) int {
	n := 0
	eqn := getEqn(a, b)
	for isPrime(eqn(n)) {
		n++
	}
	return n
}

func list(n int, all bool) []int {
	if all {
		slice := []int{}
		for i := -n; i <= n; i++ {
			slice = append(slice, i)
		}
		return slice
	}
	return []int{-n, n}
}

func findCoEffs(n int, s Soln) Soln {
	max, max_a, max_b := 0, -1, -1
	if (s != Soln{}) {
		max, max_a, max_b = s.max, s.a, s.b
	}
	for _, i := range list(n, (s == Soln{})) {
		for j := -n; j <= n; j++ {
			m := generatePrimes(i, j)
			if m > max {
				max = m
				max_a = i
				max_b = j
			}
		}
	}
	if (s != Soln{}) {
		for i := -n; i <= n; i++ {
			for _, j := range list(n, false) {
				m := generatePrimes(i, j)
				if m > max {
					max = m
					max_a = i
					max_b = j
				}
			}
		}
	}
	return Soln{max, max_a, max_b}
}

func main() {
	// cache := make(map[int]Soln)
	// // start := time.Now()
	// for i := 42; i <= 2000; i++ {
	// 	s := findCoEffs(i, cache[i-1])
	// 	cache[i] = s
	// }
	// // // fmt.Println("Done...", time.Since(start))
	// reverse_cache := make(map[string][]int)
	// for k, v := range cache {
	// 	_k := strconv.Itoa(v.a) + "_" + strconv.Itoa(v.b)
	// 	reverse_cache[_k] = append(reverse_cache[_k], k)
	// }
	// // // fmt.Println(reverse_cache)
	// solution_map := make(map[string]string)
	// for k, v := range reverse_cache {
	// 	sort.Ints(v)
	// 	solution_map[strconv.Itoa(v[0])+"_"+strconv.Itoa(v[len(v)-1])] = k
	// }
	// // fmt.Printf("%#v", solution_map)

	solution_map := map[string]string{"1033_1096": "-63_1033", "1097_1162": "-65_1097", "113_130": "-17_113", "1163_1230": "-67_1163", "1231_1300": "-69_1231", "1301_1372": "-71_1301", "131_150": "-19_131", "1373_1446": "-73_1373", "1447_1522": "-75_1447", "151_172": "-21_151", "1523_1600": "-77_1523", "1601_2000": "-79_1601", "173_196": "-23_173", "197_222": "-25_197", "223_250": "-27_223", "251_280": "-29_251", "281_312": "-31_281", "313_346": "-33_313", "347_382": "-35_347", "383_420": "-37_383", "421_460": "-39_421", "42_42": "-1_41", "43_46": "-3_43", "461_502": "-41_461", "47_52": "-5_47", "503_546": "-43_503", "53_60": "-7_53", "547_592": "-45_547", "593_640": "-47_593", "61_70": "-9_61", "641_690": "-49_641", "691_742": "-51_691", "71_82": "-11_71", "743_796": "-53_743", "797_852": "-55_797", "83_96": "-13_83", "853_910": "-57_853", "911_970": "-59_911", "971_1032": "-61_971", "97_112": "-15_97"}

	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		N, _ := strconv.Atoi(strings.TrimSpace(scanner.Text()))
		for k, v := range solution_map {
			s := strings.Split(k, "_")
			low, _ := strconv.Atoi(s[0])
			high, _ := strconv.Atoi(s[1])
			if low <= N && N <= high {
				answer := strings.Split(v, "_")
				fmt.Println(answer[0], answer[1])
			}
		}
	}
}
