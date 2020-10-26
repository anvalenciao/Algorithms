'''
5 5
3 4
2 3
7 0
0 0

$ time python3 Kbonacci.py < Kbonacci.in > Kbonacci.out
https://www.udebug.com/UVa/13298
-------------------------------------------------------
'''
# https://www.programiz.com/python-programming/examples/multiply-matrix
# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python

MOD = 1000000009
'''
def matrixMult(A, B):
    R = [[0 for col in range(len(B[0]))] for row in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for l in range(len(B)):
                R[i][j] += A[i][l] * B[l][j] % MOD
    return R
'''

def matrixMult(A, B):
    R = [[sum(a*b % MOD for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return R

def matrixPow(k, A, b):
    # I = [[0 for col in range(k)] for row in range(k)]
    I = [[0]*k]*k
    for i in range(k):
        I[i][i] = 1

    if (b==0): return(I)
    elif (b==1): return(A)
    elif (b%2 == 0):
        R = matrixPow(k, A, b/2)
        return(matrixMult(R , R))
    else: return(matrixMult(A, matrixPow(k, A, b-1)))

def kbonacci(k, n):
    if (k == 1 or k == 0 or n == 1): return(1)

    A = [[0 for col in range(k)] for row in range(k)]

    for i in range(k):
        A[0][i] = 1
    
    for j in range(k-1):
        A[j+1][j] = 1

    Ans = matrixPow(k, A, n)

    return(Ans[0][0])

def UVa13298_AFibonacciFamilyFormula():
    while True:
        try:
            k, n = map(int, input().split())
        except ValueError:
            # Not a Number
            print("NaN")
            continue
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if k <= 0 and n <= 0:
            #print()
            break
        print(kbonacci(k, n))
    return

UVa13298_AFibonacciFamilyFormula()

#print(kbonacci(5, 5))
#print(kbonacci(3, 4))
#print(kbonacci(2, 3))
#print(kbonacci(7, 0))