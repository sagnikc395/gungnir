
/*
Data defines 4 kinds of object to begin with:

1. Integer -> A number
2. Symbol -> A name consisting of a string of characters.
3. NIL -> Representing "nothing"
4. Pair -> A pair consists of 2 elements, which for historical reasons
are called car and cdr. Both can hold either an integer, a symbol,
NIL or a reference to another pair.
*/

#include "const.h"

struct Atom {
  enum {
    AtomType_Nil,
    AtomType_Pair,
    AtomType_Symbol,
    AtomType_Integer,
  } type;

  union {
    struct Pair *pair;
    const char *symbol;
    long integer;
    
  } value;
};

struct Pair {
  struct Atom atom[2];
};

typedef struct Atom Atom;


static const Atom nil = {AtomType_Nil};


//integers and pointers to strings can be copied around, but we need
// to allocate pairs on the heap
Atom cons(Atom car_val, Atom cdr_val){
  Atom p;
  p.type = AtomType_Pair;
  p.value.pair = malloc(sizeof(struct Pair));

  car(p) = car_val;
  cdr(p) = cdr_val;

  return p;
  
}
