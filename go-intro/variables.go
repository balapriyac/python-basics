package main

import "fmt"

func main() {
	// Explicit variable declaration with type
	var name string = "Gopher"
	// Type inference with the := operator
	age := 5
	// Constant declaration
	const pi = 3.14159

	fmt.Println(name)
	fmt.Println(age)
	fmt.Println(pi)

}
