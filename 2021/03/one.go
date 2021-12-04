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
    filename := os.Args[1]
	fmt.Println(filename)

    file, err := os.Open(filename)
    check(err)

	scanner := bufio.NewScanner(file)

    scanner.Split(bufio.ScanLines)

	var mostCommon [12]int;
	var num_lines = 0
    for scanner.Scan() {
       var data = scanner.Text()
	   for i := 0; i < 12; i++ {
			char := string(data[i])
			var num, _ = strconv.Atoi(char)
			mostCommon[i] += num
		}
		num_lines++
    }
    fmt.Printf("gamma rate: ")
	for i:=0; i < 12; i++ {
        if float64(mostCommon[i]) / float64(num_lines) > 0.5 {
		    fmt.Printf("1")
        } else {
		    fmt.Printf("0")
        }
	}
    fmt.Printf("\nepsilon rate: ")
	for i:=0; i < 12; i++ {
        if float64(mostCommon[i]) / float64(num_lines) < 0.5 {
		    fmt.Printf("1")
        } else {
		    fmt.Printf("0")
        }
	}


	file.Close( )
    fmt.Println(mostCommon)

}
