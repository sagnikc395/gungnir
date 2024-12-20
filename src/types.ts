//type definitions for our representationfor Scheme objects

export type Symbol = string;
export type Number = number;
export type Atom = Symbol | Number;
export type List = Array<string>;
export type Exp = Atom | List;
export type Env = typeof Map;
