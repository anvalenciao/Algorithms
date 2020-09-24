'''
PrimeKebabMenu.in
110
82944
1

$ time python3 PrimeKebabMenu.py < PrimeKebabMenu.in > PrimeKebabMenu.out
https://udebug.com/UVa/13067
-------------------------------------------------------------------------

Primos 
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Notas:
Grupo de 3 personas pedir el primer, tercer y quinto plato del menú, y su camarero lo transmitió a la cocina como 110.
135

Posiciones de en el arreglo de los primos
primer, tercer y quinto plato
2*5*11 = 110

Grupo de cinco pidió los platos número 1, 2, 3, 4 y 5, su camarero dijo que sólo 2310
Números de platos en las posiciones del arreglo de primos
2*3*5*7*11 = 2310

Si un camarero transmite un solo número a la cocina, ¿cómo calculan los chefs el número de clientes en la mesa?
Su tarea es escribir un programa que muestre el número de clientes en la mesa dado el número transmitido por un camarero. 

Input
La entrada consta de varios casos de prueba. Cada caso de prueba es una línea que contiene un número entero 1 < n < 10^14
El final de la entrada viene dado por n = 1, que no debe procesarse como un caso de prueba:

110
82944
1

Output
Para cada caso de prueba, imprima una línea con el número de clientes en el grupo:

3
14

-------------------------------------------------------------------------

Lo mejor es que, antes de procesar el primer caso, se fabrique un arreglo de booleanos usando el Algoritmo de la Criba de Eratóstenes. 
Después, al procesar el caso P basta revisar si los primos menores que sqrt(P) dividen a P.

Evitar fabricar nuevamente la lista de primos en cada iteración
Si el número no es divisible por 5, ¿para qué probar con 15 o cualquier múltiplo de 5?
Este algorimto no es tan eficiente con 10^14 pero sin con la raíz cuadrada de 10^14 = 10^7 = 10000000

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Los dígitos finales de los numeros primos pueden ser solo cuatro terminaciones, a saber: 1, 3, 7 y 9 (excepto, como excepciones, los numeros 2 y 5).

Descomponer el numero 110 en sus factores primos
110 | 2
 55 | 5
 11 | 11
  1 |

82944 | 2
41472 | 2
20736 | 2
10368 | 2
 5184 | 2
 2592 | 2
 1296 | 2
  648 | 2
  324 | 2
  162 | 2
   81 | 3
   27 | 3
    9 | 3
    3 | 3
    1 |

# Ineficiente
def primeFactors(n): 
    factors = []

    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n /= i

    return factors
'''
'''
# Ineficiente 2
def primeFactors(n): 
    factors = []

    # Numeros pares
    while n % 2 == 0:
        factors.append(2)
        n /= 2

    # Numeros impares
    # 1, 3, 7 y 9 
    # Incrementa en 2
    # Cada numero compuesto tiene al menos un factor primo menor o igual a la raiz cuadrada de si mismo
    # math.sqrt(n) = n**(1/2)
    for i in range(3, int(n**(1/2)) + 1, 2):
        print(i)
        while n % i == 0:
            factors.append(i)
            n /= i

    if n > 2:
        factors.append(int(n))

    return factors
'''
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def sieveOfEratosthenes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primeFactors(n) : 
    if n < 4:
        return [n]

    factors = []
    for i in primes:
        if i*i > n:
            break

        while n % i == 0:
            factors.append(i)
            n /= i

    if n > 2:
        factors.append(n)

    return factors


def UVa13067_PrimeKebabMenu():
    while True:
        try:
            n = int(input())
        except ValueError:
            # Not a Number
            print("NaN")
            continue
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if n < 2:
            #print()
            break
        print(len(primeFactors(n)))
    return

MAXN = 10000000
primes = sieveOfEratosthenes(MAXN)

UVa13067_PrimeKebabMenu()