from smollisp.parsing import tokenize 

def main():
    program = "(begin (define r 10) (* pi (* r r)))"
    print(tokenize(program))

if __name__ == '__main__':
    main()