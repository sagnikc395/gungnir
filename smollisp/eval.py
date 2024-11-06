from .types import Exp,Symbol,Number 
from .env import global_env


def eval(x: Exp,env=global_env) -> Exp: # type: ignore
    '''
    evaluate an expr in an env 
    '''
    if isinstance(x,Symbol):
        # variable ref 
        return env[x]
    elif isinstance(x,Number): 
        #constant number
        return x 
    elif x[0] == 'if':
        #conditional 
        (_,test,conseq,alt) = x 
        if eval(test,env):
            exp = conseq
        else:
            exp = alt 
        return eval(exp,env)
    elif x[0] =="define":
        # definition 
        (_,symbol,exp) = x 
        env[symbol] = eval(exp,env)     
    else:
        #procedure call 
        proc = eval(x[0],env)
        args = [eval(arg,env) for arg in x[1:]]
        return proc(*args)

    