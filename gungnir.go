package main

import "fmt"

func main() {
	// Example Usage
	symbolAtom := Atom{Type: AtomTypeSymbol, Value: AtomValue{Symbol: "hello"}}
	integerAtom := Atom{Type: AtomTypeInteger, Value: AtomValue{Integer: 42}}

	pairAtom := Cons(symbolAtom, integerAtom)

	fmt.Println("Pair Type:", pairAtom.Type)
	fmt.Println("Car Type:", Car(pairAtom).Type)
	fmt.Println("Car Symbol:", Car(pairAtom).Value.Symbol)
	fmt.Println("Cdr Type:", Cdr(pairAtom).Type)
	fmt.Println("Cdr Integer:", Cdr(pairAtom).Value.Integer)

	nilPair := Cons(nilAtom, nilAtom)
	fmt.Println("Nil pair car type:", Car(nilPair).Type)
	fmt.Println("Nil pair cdr type:", Cdr(nilPair).Type)
}
