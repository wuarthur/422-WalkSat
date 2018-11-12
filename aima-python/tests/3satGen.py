from random import randint
from logic import *

alpha = "ABCDEFGPQXYZOLKJTVNM"
exprMap={'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'P': P, 'Q': Q, 'X': X,
         'Y': Y, 'Z': Z, 'O': O, 'L': L, 'K': K, 'J': J, 'T': T, 'V': V, 'N': N, 'M': M}
Vars=[]
Clauses=[]

for i in alpha:
    if len(Vars) >=20:
        break
    Vars.append(i)


def genClauses(N):
    diq={}
    counts=0
    ret=[]
    while counts<N:
        clause= makeClause()
        if clause in diq:
            continue
        else:
            diq[clause]=1
            ret.append(clause)
            counts+=1

    return ret

def makeClause():
    Var3=[]
    while len(Var3)<3:
        i =randint(0, 19)
        Var = Vars[i]
        if Var not in Var3:
            Var3.append(exprMap[Var])

    clause = Var3[0]| Var3[1] | Var3[2]
    return clause


#print(genClauses(10))
for i in range(10):

    soln, flips = WalkSAT(genClauses(10))# change the number here
    print(soln, flips)