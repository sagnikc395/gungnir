package main

func Car(p Atom) *Atom {
	return &p.Value.Pair.Atom[0]
}

func Cdr(p Atom) *Atom {
	return &p.Value.Pair.Atom[1]
}

func Cons(carVal Atom, cdrVal Atom) Atom {
	p := Atom{
		Type: AtomTypePair,
		Value: AtomValue{
			Pair: &Pair{
				Atom: [2]Atom{carVal, cdrVal},
			},
		},
	}

	return p
}
