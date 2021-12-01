package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}


func main() {
	var filename = os.Args[1]
	fmt.Println(filename)
	var numbers [] int

    file, err := os.Open(filename)
    check(err)

	scanner := bufio.NewScanner(file)

    scanner.Split(bufio.ScanLines)

    for scanner.Scan() {
		var x, _ = strconv.Atoi(scanner.Text())
        numbers = append(numbers, x)
    }
	file.Close()

	fmt.Println(numbers)

	var increases int
	for i := 0; i < len(numbers); i++ {
        if i == 0 {
            continue
        }

        if numbers[i] > numbers[i-1] {
            increases++
        }
	}
	fmt.Println(increases)
}
