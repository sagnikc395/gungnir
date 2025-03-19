package main

import "strings"

func tokenize(chars string) List {
	return strings.Split(strings.ReplaceAll(strings.ReplaceAll(chars, "(", " ( "), ")", " ) "), "")
}

//read a gungnir expression from a string
// func parse(program string) Exp {
// 	return readFromTokens(tokenize(program))
// }

// //read a expression from a seqeunce of tokens
// func readFromTokens(tokens List) Exp {

// }
