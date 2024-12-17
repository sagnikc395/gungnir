//type definitions for our representationfor Scheme objects

type Symbol = string;
type Number = number;
type Atom = Symbol | Number;
type List = typeof Array;
type Exp = Atom | List;
type Env = typeof Map;
