'''
DatingOnLine.in
6
10 60 70 70 80 80
3
100 100 100
7
16 37 50 35 12 39 24

$ time python3 DatingOnLine.py < DatingOnLine.in > DatingOnLine.out

https://udebug.com/LA/7889
-------------------------------------------------------------------

+----------------------------------+
|                N=7               |
+----+----+----+----+----+----+----+
| S1 | S2 | S3 | S4 | S5 | S6 | S7 |
+----+----+----+----+----+----+----+
| 16 | 37 | 50 | 35 | 12 | 39 | 24 |
+----+----+----+----+----+----+----+
| 12 | 16 | 24 | 35 | 37 | 39 | 50 |
+----+----+----+----+----+----+----+
'''
import math

def calculate(N, S):
    S.sort()
    B = math.pi/N
    CS = math.sin(B)*math.cos(B)
    A = S[0]*S[1]*CS
    for i in range(2, N):
        A += S[i-2]*S[i]*CS
    A += S[i-1]*S[i]*CS

    return round(A, 3)

def UVaLive7889_DatingOnLine():
    while True:
        try:
            N = int(input())
            S = list(map(int, input().split()))
        except ValueError:
            # Not a Number
            print("NaN")
            continue
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if N < 3:
            #print()
            break
        print(calculate(N, S))
    return

UVaLive7889_DatingOnLine()