import type { List } from "./types";

function tokenize(chars: string): List {
  //convert a string of chars into a list of tokens
  return chars
    .replace(/\(/g, " ( ")
    .replace(/\)/g, " ) ")
    .split(/\s+/)
    .filter((token) => token.length > 0);
}

const main = () => {
  const program = "(begin (define r 10) (* pi (* r r)))";
  console.log(tokenize(program));
};

main();
