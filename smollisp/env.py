# env is a mapping from variable names to their values 
#eval will use a global env 
# this env can be augmented with user-define variables 

import math 
import operator as op 
from .types import List,Number,Symbol

class Env(dict):
    '''
    an env dict of {'var' : val} pairs ,  with an outer Env.
    '''
    def __init__(self,parms=(),args=(),outer=None):
        self.update(zip(parms,args))
        self.outer = outer  

    def find(self,var):
        '''
        find the innermost Env where var appears.
        ''' 
        if var in self:
            return self 
        else:
            return self.outer.find(var)
        
class Procedure():
    '''user defined lisp procedure'''
    def __init__(self,parms,body,env):
        self.parms,self.body,self.env = parms,body,env 

    def __call__(self,*args):
        return eval(self.body,Env(self.parms,args,self.env))

def standard_env() -> Env:
    env = Env()
    env.update(vars(math))
    env.update({
        '+':op.add, 
        '-':op.sub,
        '*':op.mul,
        '/':op.truediv,
        '>':op.gt,
        '<':op.lt,
        '>=':op.ge,
        '<=':op.le,
        '=':op.eq,
        'abs':abs,
        'append':op.add,
        'apply':lambda proc,args : proc(*args),
        'begin':lambda *x: x[-1],
        'car': lambda x:x[0],
        'cdr': lambda x:x[1:],
        'cons': lambda x,y: [x]+y,
        'eq?': op.is_,
        'expt':pow,
        'equal?':op.eq,
        'length':len,
        'list': lambda *x: List(x),
        'list?': lambda x: isinstance(x,List),
        'map': map, 
        'max': max,
        'min': min,
        'not':op.not_, 
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x,Number),
        'print': print,
        'procedure?': callable,
        'round': round,
        'symbol?':lambda x: isinstance(x,Symbol),
    })
    return env 

global_env = standard_env()