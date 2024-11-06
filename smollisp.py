from smollisp.parsing import tokenize,parse

def main():
    program = "(begin (define r 10) (* pi (* r r)))"
    print(tokenize(program))
    print(parse(program))

if __name__ == '__main__':
    main()