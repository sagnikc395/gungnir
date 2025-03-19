package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func REPL() {
	scanner := bufio.NewScanner(os.Stdin)
	var buf []string

	fmt.Printf("gungnir version 0.0.1\nPress Ctrl+C to Exit\n")

	for scanner.Scan() {
		fmt.Printf("gungnir > \n")
		buf = append(buf, scanner.Text())
		fmt.Println(strings.Join(buf, ""))
	}

}
