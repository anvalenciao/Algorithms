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
| 16 | 35 | 39 | 50 | 37 | 24 | 12 |
+----+----+----+----+----+----+----+

'''

def process(N, S):
    print(N)
    print(S)
    return True


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
        if N < 2:
            #print()
            break
        print(process(N, S))
    return

UVaLive7889_DatingOnLine()