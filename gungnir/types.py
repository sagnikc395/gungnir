# our representations for the Scheme objects / type system
#
# using pydantic libary since it supports discriminated union for us
#
from pydantic import BaseModel
from typing import  Union

# symbol is implemented as type of string 
class Symbol(BaseModel):
    item_type: str

# int type
class Integer(BaseModel):
    item_type: int

# float type
class Float(BaseModel):
    item_type: float


# number type is a union type
Number = Union[Integer,Float]

# atom is a symbol or number type
Atom = Union[Symbol,Number]

# List type is defined as a list type
class List(BaseModel):
    item_type: list

# an expression is a an atom or list type
Expression = Union[Atom,List]

# environment is a mapping type, so defined as a dict
class Env(BaseModel):
    item_type: dict

    

