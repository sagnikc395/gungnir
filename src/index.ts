import type { Atom, Exp, List } from "./types";

function tokenize(chars: string): List {
  //convert a string of chars into a list of tokens
  return chars
    .replace(/\(/g, " ( ")
    .replace(/\)/g, " ) ")
    .split(/\s+/)
    .filter((token) => token.length > 0);
}

function parse(program: string): Exp {
  //read a scheme experssion from a string
  return readFromTokens(tokenize(program));
}

function readFromTokens(tokens: List): Exp {
  if (tokens.length === 0) {
    throw new SyntaxError("Unexpected EOF");
  }
  let token = tokens.shift();
  if (token === "(") {
    const list: List = [];
    while (tokens[0] !== ")") {
      list.push(readFromTokens(tokens) as string);
    }
    tokens.shift();
    return list;
  } else if (token === ")") {
    throw new SyntaxError("unexpected )");
  } else {
    return atom(token!);
  }
}

function atom(token: string): Atom {
  // numbers become numbers, other token is a symbol
  const intval = parseInt(token);
  if (!isNaN(intval) && intval.toString() === token) {
    return intval;
  }

  //parsing as float
  const floatval = parseFloat(token);
  if (!isNaN(floatval) && floatval.toString() === token) {
    return floatval;
  }
  //return as symbol
  return token;
}

const program = "(begin (define r 10) (* pi (* r r)))";
console.log(tokenize(program));
