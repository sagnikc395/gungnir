mod types;

fn parse(program: &mut str) -> Vec<&str> {
    todo!()
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
}
