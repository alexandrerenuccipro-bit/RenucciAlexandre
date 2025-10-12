import numpy as np

#Partie 1 - Récursivité
#Question 1

def somme_recursive(liste:list) -> int:
    """
    Retourne la somme de la liste en recursivife
    Args:
        liste(list): La liste
    Returns:
        int: La somme de la liste
    """
    if len(liste) == 0:
        return 0
    else:
        return liste[0] + somme_recursive(liste[1:])
    
#print(somme_recursive([1,2,3,4,6])) 

###################################################################

#Question 2

def factorielle_recursive(n:int) -> int:
    """
    Retourne la factorielle de n en recursif
    Args:
        n(int): Le nombre
    Returns:
        int: La factorielle de n
    """
    if n == 0:
        return 1
    else:
        return n * factorielle_recursive(n-1)

#print(factorielle_recursive(5))

###################################################################

#Question 3

def longueur_recursive(liste:list) -> int:
    """
    Retourne la longueur de la liste en recursif
    Args:
        liste(list): La liste
    Returns:
        int: La longueur de la liste
    """
    if liste == []:
        return 0
    else:
        return 1 + longueur_recursive(liste[1:])
    
print(longueur_recursive([1,2,3,4,5,6,7,8,9]))

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

