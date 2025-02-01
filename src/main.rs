use types::{Atom, Exp, Symbol};

mod types;

fn atom(token: &str) -> Atom {
    //try parsing as integer first
    if let Ok(i) = token.parse::<i64>() {
        return Atom::Integer(i);
    }

    //then pasrse as float
    if let Ok(f) = token.parse::<f64>() {
        return Atom::Float(f);
    }
    //else its a symbol
    Atom::Sym(Symbol(token))
}

fn parse(program: &mut str) -> Exp {
    // read a scheme expression from a string
    let mut tokens = tokenize(&program);
    read_from_tokens(&mut tokens)
}

pub fn read_from_tokens<'a>(tokens: &mut Vec<&'a str>) -> Result<Exp<'a>, String> {
    // Check for empty tokens
    if tokens.is_empty() {
        return Err("unexpected EOF".to_string());
    }

    // Pop first token
    let token = tokens.remove(0);

    if token == "(" {
        let mut L = Vec::new();

        // Check for empty list
        while !tokens.is_empty() && tokens[0] != ")" {
            L.push(read_from_tokens(tokens)?);
        }

        // Check if we found the closing parenthesis
        if tokens.is_empty() {
            return Err("missing closing parenthesis".to_string());
        }

        tokens.remove(0); // pop off ')'
        Ok(Exp::List(L))
    } else if token == ")" {
        Err("unexpected ')'".to_string())
    } else {
        Ok(Exp::Atom(atom(token)))
    }
}

fn tokenize(chars: &str) -> Vec<String> {
    //convert a string of characters into a list of tokens

    chars
        .replace("(", " ( ")
        .replace(")", " ) ")
        .split_whitespace()
        .map(String::from)
        .collect()
}

fn main() {
    let program = "(begin (define r 10) (* pi (* r r)))";
    let tokenize_result = tokenize(&program);

    for item in tokenize_result.iter() {
        println!("{}", item);
    }
}
