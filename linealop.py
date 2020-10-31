# Suma los factores de coeficientes duplicados
def removeDuplicates(combination):
    new_combination = [combination[0]]
    temp_elem = []
    for i in range(1, len(combination)):
        # Verificamos que no hayamos contado el coeficiente.
        if contains(new_combination, combination[i][0]):
            continue
        temp_elem = combination[i].copy()

        for j in range(i+1, len(combination)):
            if combination[j][0] == temp_elem[0]:
                temp_elem[1] += combination[j][1]

        new_combination.append(temp_elem)
    return new_combination

# Verifica si el elemento está contenido en la combinación lineal
def contains(combination, coeficient):
    if len(combination) <= 1:
        return False
    for index in range(1, len(combination)):
        if combination[index][0] == coeficient:
            return True
    return False

# Dadas dos combinaciones lineales la segunda se combina con la primera.
# Si hay coeficientes comúnes estos se combinan
# Se eliminan repetidos
def mergeCombinations(comb1, comb2):
    search_elem = comb2.pop(0)
    old_combination = []
    factor = -1
    for index in range(1, len(comb1)):
        if comb1[index][0] == search_elem:
            old_combination = comb1.pop(index)
            factor = old_combination[1]
            break
    if len(old_combination) > 0:
        for index in range(0, len(comb2)):
            comb2[index][1] *= factor
        comb1.extend(comb2)
    return comb1
