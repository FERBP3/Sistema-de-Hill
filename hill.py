# Criptografía y seguridad
# Sistema de Hill
# José Fernando Brigido Pablo

import matrices
import modulop
import linealop

# Devueve el mapeo de la letra pasado como parámetro a su índice
# correspondiente
def mapLetter(a):
    a = a.upper()
    mapped = -1
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for index,letter in enumerate(alphabet):
        if a == letter:
            mapped = index
    return mapped

def mapNumber(n):
    mapped = -1
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for index,letter in enumerate(alphabet):
        if n == index:
            mapped = letter
    return mapped

def mapMessage(message, n):
    ngramas = []
    ngrama = []
    for letter in message:
        ngrama.append(mapLetter(letter))
        if (len(ngrama) % n) == 0:
            ngramas.append(ngrama)
            ngrama = []
    return ngramas

# Calcula la dimension de la matriz dependiendo la longitud de la clave
def getNmatrix(clave):
    n = -1
    if len(clave) == 0:
        return -1
    for i in range(1, len(clave)+1):
        if i*i >= len(clave):
            n = i
            break
    return n

# Devuelve la matriz correspondiente a la clave
def getMatrix(n, clave):
    matrix = []
    sub_matrix = []
    while(len(clave) < n*n):
        clave += "A"

    for letter in clave:
        if(len(sub_matrix) == n):
            matrix.append(sub_matrix)
            sub_matrix = [mapLetter(letter)]
        else:
            sub_matrix.append(mapLetter(letter))
    matrix.append(sub_matrix)
    return matrix

# Se verifica que la la matriz asociada a la clave sea invertible
# Para esto se verifica que el determinante sea invertible en Z27
def checkClave(clave):
    n = getNmatrix(clave)
    matrix = getMatrix(n, clave)
    det = matrices.getDeterminant(matrix)
    if det == 0 or (modulop.relative_primes(det, 27) is not True):
        raise Exception("La matriz no es invertible")
    return n

def checkMessage(message, n):
    if len(message) % n != 0:
        raise Exception("El mensaje no es múltiplo de "+str(n))

# Cifra el mensaje con método de Hill
def cifrar(message, clave):
    n = getNmatrix(clave)
    ngramas = mapMessage(message, n)
    matrix = getMatrix(n, clave)
    cifrado = ""
    for m in ngramas:
        cipherMatrix = matrices.multiplicaMatrices(matrix, m)
        for i in range(0, len(cipherMatrix)):
            cifrado += mapNumber(cipherMatrix[i] % 27)
    return cifrado

# Decifra el mensaje usando la clave pasada como parámetro
def decifrar(clave, message):
    n = getNmatrix(clave)
    matrix = getMatrix(n, clave)
    inversa = matrices.getMatrizInversa(matrix, 27)
    ngramas = mapMessage(message, n)
    texto_decifrado = ""
    for m in ngramas:
        decifrado = matrices.multiplicaMatrices(inversa, m)
        for i in range(0, len(decifrado)):
            texto_decifrado += mapNumber(decifrado[i] % 27)
    return texto_decifrado

def main():
    clave = "FORTALEZA"
    message = "CONSUL"

    checkClave(clave)
    n = getNmatrix(clave)
    checkMessage(message, n)

    cifrado = cifrar(message, clave)
    print("El texto cifrado es: \n{}".format(cifrado))

    decifrado = decifrar(clave, cifrado)
    print("Texto decifrado es:\n{}".format(decifrado))

if __name__ == '__main__':
    main()
