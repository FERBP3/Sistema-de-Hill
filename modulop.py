import linealop

# Calcula el maximo común divisor entre a y b
def mcd(a, b):
    while b != 0:
        a,b = b,a % b
    return a

# Decide si dos números son primos relativos
def relative_primes(a, b):
    if mcd(a,b) == 1:
        return True
    else:
        return False

# Se generan las combinaciones lineales a partir del euclides extendido
def extended_euclidean(a,n):
    combinations = []
    while (n % a) != 0:
        r = n % a
        div = int(n/a)

        linear_combination = [r, [n, 1], [a, -div]]
        combinations.append(linear_combination)

        n = a
        a = r

    combinations.reverse()
    return combinations

# Se calcula el inverso de a en Z_n
def getInverso(a, n):
    combinations = extended_euclidean(a, n)
    # combinacion lineal igualada a 1
    final_combination = combinations.pop(0)
    for combination in combinations:
        final_combination = linealop.mergeCombinations(final_combination, combination)
        final_combination = linealop.removeDuplicates(final_combination)

    inverso = -1
    if final_combination[2][0] == n:
        inverso = final_combination[1][1]
    else:
        inverso = final_combination[2][1]

    if inverso < 0:
        inverso += n
    return inverso
