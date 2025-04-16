package main

import "fmt"

func calculateStats(values []int) (min, max, sum int) {
	if len(values) == 0 {
		return 0, 0, 0
	}

	min = values[0]
	max = values[0]
	sum = 0

	for _, v := range values {
		if v < min {
			min = v
		}
		if v > max {
			max = v
		}
		sum += v
	}

	return // naked return
}

func main() {
	values := []int{5, 8, 2, 10, 3}
	min, max, sum := calculateStats(values)
	fmt.Println("Min:", min)
	fmt.Println("Max:", max)
	fmt.Println("Sum:", sum)
}
