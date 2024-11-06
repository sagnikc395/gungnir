from .types import Exp, Atom, Symbol

def tokenize(chars: str) -> list:
    '''
    convert a string of chars into a list of tokens
    '''
    return chars.replace('(',' ( ').replace(')',' ) ').split()

def parse(program: str) -> Exp: # type: ignore
    '''
    read a lisp expression from a string 
    '''
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp: # type: ignore
    '''
    read an expression from a sequence of tokens 
    '''
    if len(tokens) == 0 :
        raise SyntaxError("unexpected EOF")
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] !=')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L 
    elif token ==')':
        raise SyntaxError("unexpected )")
    else:
        return atom(token)
    
def atom(token: str) -> Atom: # type: ignore
    '''
    numbers are numbers, every other token is a symbol
    '''
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)
        
