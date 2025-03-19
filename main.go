package main

import "fmt"

func main() {
	program := "(begin (define r 10) (* pi (* r r)))"
	fmt.Println(len(program))
	fmt.Println(tokenize(program))
	fmt.Println(len(tokenize(program)))

	for _, v := range program {
		fmt.Printf("%v\t",string(v))
	}
}
