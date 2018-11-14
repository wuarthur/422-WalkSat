from random import randint
from logic import *
import sys
import statistics as stats
from multiprocessing import Pool


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
            if randint(0, 19) > 9:
                Var3.append(~exprMap[Var])
            else:
                Var3.append(exprMap[Var])

    clause = Var3[0]| Var3[1] | Var3[2]
    return clause

def solve(C):
    print('C=', C)
    flippy = []
    fails = 0
    for i in range(50):
        print(i)
        c = genClauses(C)
        # print(c)
        soln, flips = WalkSAT(c)  # change the number here
        if soln:
            flippy.append(flips)
        else:
            fails += 1
        # print(flips ,soln )

    # print(flippy)
    print("median:", flippy)
    print('fails:', fails)

# for j in [20,40,60,80,100,120,140,160,180,200]:
if __name__ == '__main__':
    # pool = Pool(processes=10)
    for j in [160,180,200]:
        solve(j)
    # pool = Pool(processes=10)              # start 4 worker processes
    # r1 = pool.apply_async(solve, [20])
    # print (r1.get(timeout=10) )
    #
    # r2 = pool.apply_async(solve, [40])
    # print (r2.get(timeout=10) )
    #
    # r3 = pool.apply_async(solve, [60])
    # print (r3.get(timeout=10) )
    #
    # r4 = pool.apply_async(solve, [80])
    # print (r4.get(timeout=500) )
    #
    # r5 = pool.apply_async(solve, [100])
    # print (r5.get(timeout=500) )
    #
    # r6 = pool.apply_async(solve, [120])
    # print (r6.get(timeout=500) )
    #
    # r7 = pool.apply_async(solve, [140])
    # print (r7.get(timeout=500) )
    #
    # r8 = pool.apply_async(solve, [160])
    # print (r8.get(timeout=500) )
    #
    # r9 = pool.apply_async(solve, [180])
    # print (r9.get(timeout=500) )
    #
    # r10 = pool.apply_async(solve, [200])
    # print(r10.get(timeout=500))
