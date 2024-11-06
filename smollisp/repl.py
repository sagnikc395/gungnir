from .eval import eval 
from .parsing import parse
from .types import List

def repl(prompt='smollisp>  '):
    '''repl 
    '''
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(smollispstr(val))

def smollispstr(exp):
    '''
    convert python obj back to lisp readable string.
    '''
    if isinstance(exp,List):
        return '(' + ' '.join(map(smollispstr,exp)) + ')'
    else:
        return str(exp)
    
    