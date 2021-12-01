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

	var increases int
	for i := 0; i < len(numbers) - 1; i++ {
        if i < 2 {
            continue
        }

        fmt.Printf("%d <? %d\n", numbers[i] + numbers[i-1] + numbers[i-2],numbers[i-1] + numbers[i] + numbers[i+1])

        if numbers[i] + numbers[i-1] + numbers[i-2] < numbers[i-1] + numbers[i] + numbers[i+1] {
            increases++
        }
	}
	fmt.Println(increases)
}
