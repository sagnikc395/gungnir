//type definitions for our representationfor Scheme objects

export type Symbol = string;
export type Number = number;
export type Atom = Symbol | Number;
export type List = typeof Array;
export type Exp = Atom | List;
export type Env = typeof Map;
