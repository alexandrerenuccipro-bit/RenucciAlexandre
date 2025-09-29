import numpy as np

#Partie 1 - Récursivité

###################################################################

#Partie 2 - Matrices

#Question 1

def searchsorted(table: object, element: int) -> int:
    """
    Retourne l'indice de l'element dans la table
    Args:
        table(list): La table
        element(int): L'element rechercher
    Returns:
        int: L'indice de l'element
    """
    i = 0
    table.sort() #Trie de la table
    while len(table) > i and table[i] < element:
        i += 1
    return i

#print(searchsorted([5, 7, 8, 9], 10)) #4

###################################################################

def my_where(table: object, valeur: int) -> list:
    """
    Retourne la liste des indices dans un tableau à une ou plusieurs dimensions
    Args:
        table(list): La table (1D ou 2D)
        valeur(int): La valeur à rechercher
    Returns:
        list: La liste des indices de la valeur
    """
    liste_indices = []
    if not isinstance(table[0], (list, tuple)):
        for i in range(len(table)):
            if table[i] == valeur:
                liste_indices.append(i)
    else:
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == valeur:
                    liste_indices.append((i, j))
    
    return liste_indices

#print(my_where([[5, 7, 8], [9, 5, 6], [7, 8, 5]], 5)) #[(0, 0), (1, 1), (2, 2)]
#print(my_where([5, 7, 8, 9, 5, 6, 7, 8, 5], 5)) #[0, 4, 8]

