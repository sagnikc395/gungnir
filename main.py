from gungnir import parser

def main():
    program = "(begin (define r 10) (* pi (* r r)))"
    p = parser.Parser.tokenize(program)
    print(p)

    

if __name__ == "__main__":
    main()
