package main

type AtomType int

const (
	AtomTypeNil AtomType = iota
	AtomTypePair
	AtomTypeSymbol
	AtomTypeInteger
)

type Atom struct {
	Type  AtomType
	Value AtomValue
}

type AtomValue struct {
	Pair    *Pair
	Symbol  string
	Integer int64
}

type Pair struct {
	Atom [2]Atom
}

var nilAtom = Atom{Type: AtomTypeNil}
