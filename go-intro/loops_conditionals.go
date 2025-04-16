package main

import "fmt"

func main() {
	// If statement
	score := 85
	if score >= 90 {
		fmt.Println("A grade")
	} else if score >= 80 {
		fmt.Println("B grade")
	} else {
		fmt.Println("Lower grade")
	}

	// Traditional for loop (similar to C-style for loops)
	for i := 0; i < 4; i++ {
		fmt.Println("Count:", i)
	}

	// For as a while loop
	sum := 1
	for sum < 10 {
		sum += sum
		fmt.Println("Sum is now:", sum)
	}

	// Iterating with range
	fruits := []string{"apple", "banana", "cherry"}
	for index, fruit := range fruits {
		fmt.Println(index, fruit)
	}
	// Using _ to ignore the index
	for _, fruit := range fruits {
		fmt.Println(fruit)
	}

}
