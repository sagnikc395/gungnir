# using direct string split and doing on that

from .types import Expression

class Parser:
    def tokenize(self,chars: str) -> list:
        return chars.replace('(',' ( ').replace(')',' ) ').split()

    def parse(self,program: str) -> Expression:
        '''
            read a expression from a string 
        '''
        return self.read_from_tokens(self.tokenize(program))

    def read_from_tokens(tokens: list) -> Expression:
        pass  
