#define car(p) ((p).value.pair -> atom[0])
#define cdr(p) ((p).value.pair -> atom[1])

#define nilp(atom) ((atom).type == AtomType_Nil)
