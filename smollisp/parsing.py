def tokenize(chars: str) -> list:
    '''
    convert a string of chars into a list of tokens
    '''
    return chars.replace('(',' ( ').replace(')',' ) ').split()

