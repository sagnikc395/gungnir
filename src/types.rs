// define the type definitions of our representations of
// Scheme objects

use std::collections::HashMap;

pub type Symbol<'a> = &'a str;

//ref: https://medium.com/@dmitrydoronin/union-types-in-rust-3acf65ed849
pub enum Number {
    Int(i64),
    Float(f64),
}

// scheme atom is a symbol or number
pub enum Atom<'a> {
    Sym(Symbol<'a>),
    Num(Number),
}

// list taken as a generic vector
pub type List<T> = Vec<T>;

//scheme expressions is an atom or list
pub enum Exp<'a> {
    Atom(Atom<'a>),
    List(List<&'a str>),
}

//scheme environment is a mapping of {variable: value}
pub type Env<K, V> = HashMap<K, V>;
