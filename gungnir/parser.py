# using direct string split and doing on that

from .types import Expression, Atom, Symbol

class Parser:
    def tokenize(self,chars: str) -> list:
        return chars.replace('(',' ( ').replace(')',' ) ').split()

    def parse(self,program: str) -> Expression:
        '''
            read a expression from a string 
        '''
        return self.read_from_tokens(self.tokenize(program))

    def read_from_tokens(self,tokens: list) -> Expression:
        '''
        read an expression from a sequence of tokens.
        '''
        if len(tokens) == 0:
            raise SyntaxError('Unexpected EOF')

        token = tokens.pop(0)
        if token == '(':
            read_till_now = []
            while tokens[0] != ')':
                read_till_now.append(self.read_from_tokens(tokens))
            tokens.pop(0)
            return read_till_now

        elif token == ')':
            raise SyntaxError("unexpected )")
        else:
            return self.atom(token)

    def atom(self,token: str) -> Atom:
        # nubers will become numbers; every other token is a symbol
        try:
            return int(token)        
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return Symbol(token)            
