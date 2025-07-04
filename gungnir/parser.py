# using direct string split and doing on that

class Parser:
    @staticmethod
    def tokenize(chars: str) -> list:
        return chars.replace('(',' ( ').replace(')',' ) ').split()


