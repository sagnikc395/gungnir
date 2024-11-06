from smollisp.parsing import tokenize,parse
from smollisp.eval import eval 

def main():
    program = "(begin (define r 10) (* pi (* r r)))"
    print(tokenize(program))
    print(parse(program))
    print(eval(parse(program)))

if __name__ == '__main__':
    main()