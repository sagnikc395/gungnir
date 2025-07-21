from gungnir.parser import Parser

def main():
    program = "(begin (define r 10) (* pi (* r r)))"
    p = Parser().tokenize(program)
    print(p)

    

if __name__ == "__main__":
    main()
