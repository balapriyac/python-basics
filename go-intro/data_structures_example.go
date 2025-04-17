// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
	// Declaring and initializing an array
	var colors [3]string
	colors[0] = "Red"
	colors[1] = "Green"
	colors[2] = "Blue"

	fmt.Println(colors)

	// Array literal
	numbers := [5]int{1, 2, 3, 4, 5}
	fmt.Println(numbers)

	// Creating a slice
	fruits := []string{"Apple", "Banana", "Cherry"}
	// Adding elements to a slice
	fruits = append(fruits, "Date")

	// Slicing operations
	//firstTwo := fruits[:2] // ["Apple", "Banana"]
	//lastTwo := fruits[1:3] // ["Banana", "Cherry"]

	// Creating a map
	ages := map[string]int{
		"Alice": 25,
		"Bob":   30,
	}

	// Working with maps
	fmt.Println(ages["Alice"]) // 25
	ages["Charlie"] = 22       // Add a new entry
	ages["Alice"] = 26         // Update an existing entry

	// Check if a key exists
	age, exists := ages["Dave"]
	if exists {
		fmt.Println("Dave's age:", age)
	} else {
		fmt.Println("Dave not in map")
	}

	// Delete an entry
	delete(ages, "Bob")

}
