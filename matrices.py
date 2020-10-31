import modulop
# Devuelve una copia de la matriz pasada como parámetro
def cloneMatrix(matrix):
    if len(matrix) == 0:
        return []
    else:
        new_matrix = []
        indexRow = 0
        for row in matrix:
            new_sub_matrix = []
            for element in matrix[indexRow]:
                new_sub_matrix.append(element)

            new_matrix.append(new_sub_matrix)
            new_sub_matrix = []
            indexRow += 1
        return new_matrix

# Devuelve la matriz pasada como parámetro sin la columna y renglón dados
def removeRowColumn(matrix, row, column):
    new_matrix = cloneMatrix(matrix)
    new_matrix.pop(row)
    for r in new_matrix:
        r.pop(column)
    return new_matrix

# Se calcula el determinante de una matriz de NxN
def getDeterminant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        s1 = matrix[0][0]*matrix[1][1]
        s2 = matrix[0][1]*matrix[1][0]
        return s1 - s2
    else:
        i = 0
        det = 0
        for element in matrix[0]:
            sub_matrix = removeRowColumn(matrix, 0, i)
            s = element*getDeterminant(sub_matrix)
            if (i % 2) != 0:
                s *= -1
            det += s
            i += 1
        return det

# Calcula la transpuesta de una matriz cuadrada
def transpuesta(matrix):
    n = len(matrix)
    new_matrix = []
    for i in range(0, n):
        new_matrix.append([])

    index = 0
    for row in matrix:
        for elem in row:
            new_matrix[index].append(elem)
            index += 1
        index = 0
    return new_matrix

def adjunta(matrix):
    new_matrix = []
    for i in range(0, len(matrix)):
        new_matrix.append([])

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            factor = getDeterminant(removeRowColumn(matrix, row, col))
            if (row+col) % 2 != 0:
                factor *= -1
            new_matrix[row].append(factor)
    return new_matrix

# Multiplica una matrix de nxn por un n-grama
def multiplicaMatrices(k, m):
    n = len(k)
    new_matrix = []
    for i in range(0, n):
        entrada = 0
        for j in range(0, n):
            entrada += m[j]*k[i][j]
        new_matrix.append(entrada)
        entrada = 0
    return new_matrix

# Devuelve la matriz inversa modulo n
def getMatrizInversa(matrix, n):
    inversa = adjunta(transpuesta(matrix))
    inverso_modulo = modulop.getInverso(getDeterminant(matrix), n)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            inversa[i][j] = (inversa[i][j]*inverso_modulo) % n
    return inversa
