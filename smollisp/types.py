## types for the object 
Symbol = str #  symbol is implemented as a Python str 
Number = (int,float) #number is int / float 
Atom = (Symbol,Number) # atom is an symbol or number 
List = list # list is implemented as a python list 
Exp = (Atom,List) # expression if an Atom or List 
Env = dict # env is a mapping of {variable:value}
