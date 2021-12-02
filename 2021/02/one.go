package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
    "strings"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}


func main() {
    filename := os.Args[1]
	fmt.Println(filename)
    horizontal := 0
    vertical := 0

    file, err := os.Open(filename)
    check(err)

	scanner := bufio.NewScanner(file)

    scanner.Split(bufio.ScanLines)

    for scanner.Scan() {
        var data = strings.Split(scanner.Text(), " ")
        var dir = data[0]
		var mag, _ = strconv.Atoi(data[1])

        if dir == "forward"{
            horizontal += mag
        }else if dir == "down" {
            vertical += mag
        }else if dir == "up" {
            vertical -= mag
        }
    }
	file.Close( )
    fmt.Println(vertical * horizontal)

}
