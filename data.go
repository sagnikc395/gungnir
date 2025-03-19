package main

// repr of the Scheme objects

//gungnir symbol is implemented as a string
type Symbol = string

// gungnir number is implemened as int64 or float64 union

type Number interface {
	integer() int64
	float() float64
}

//gungnir atom is a Symbol or Number union type

type Atom interface {
	sym() Symbol
	num() Number
}

//list is a string slice
type List = []string

// gungnir expression is an Atom of List
type Exp interface {
	atom() Atom
	list() List
}

//env is a mapping / dictionary
type Env = map[string]interface{}
