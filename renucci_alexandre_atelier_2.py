# atelier_2

# Execice 1

def moyenne_dune_lst(ma_liste: list) -> float:
    """
    Calcule la moyenne des valeurs d'une liste d'entiers.
    
    Args:
        ma_liste (list): Liste d'entiers
        
    Returns:
        float: La moyenne des valeurs de la liste
    """
    if len(ma_liste)==0:
        return len(ma_liste)
    else:
        return sum(ma_liste) / len(ma_liste)

print("===Test moyenne_dune_lst()===")
print ( moyenne_dune_lst([1,2,3,4,5,6,7,8,9]), "\n")

################################################################

# Version avec boucle for sur les indices
def nb_sup_indices(ma_liste: list, element: int) -> list:
    """
    Renvoie la liste des nombres supérieur a l'élément indiqué'
    Version avec boucle for sur les indices.
    
    Args:
        ma_liste(list): Liste d'entiers
        element(int): L'élément '
    
    Returns:
        list: La liste avec les éléments supérieur au parametre "element"
        
    """
    resultat = []
    vide = [0]
    if len(ma_liste)==0:
        return vide
    else:
        for i in range(len(ma_liste)):
            if ma_liste[i] > element:
                resultat.append(ma_liste[i])
                i+=1
        return resultat #len(resultat)


print("===Test nb_sup_indices() vide===")
print ( nb_sup_indices([], 5), "\n")


print("===Test nb_sup_indices()===")
print ( nb_sup_indices([1,2,3,4,5,6,7,8,9], 5), "\n")

################################################################

# Version avec boucle for sur les éléments
def nb_sup_elements(ma_liste: list, element: int) -> list:
    """
    Version avec boucle for sur les éléments.
    """
    resultat = []
    vide = [0]
    if len(ma_liste)==0:
        return vide
    else:
        for valeur in ma_liste:
            if valeur > element:
                resultat.append(valeur)
        return resultat #len(resultat)

print("===Test nb_sup_elements()===")
print ( nb_sup_elements([1,2,3,4,5,6,7,8,9], 5), "\n")

################################################################

# Version avec boucle while
def nb_sup_while(ma_liste: list, element: int) -> list:
    """
    Version avec boucle while.
    """
    resultat = []
    vide = [0]
    i = 0
    if len(resultat)==0:
        return vide
    else:
        while i < len(ma_liste):
            if ma_liste[i] > element:
                resultat.append(ma_liste[i])
            i += 1
        return resultat #len(resultat)

print("===Test nb_sup_while()===")
print ( nb_sup_while([1,2,3,4,5,6,7,8,9], 5), "\n")

################################################################

def moy_sup(ma_liste: list, elt: int) -> float:
    """
    Calcule la moyenne des valeurs de la liste strictement supérieures à elt.
    
    Args:
        ma_liste (list): Liste d'entiers
        elt (int): Valeur de référence
        
    Returns:
        float: Moyenne des valeurs strictement supérieures à elt
    """
    valeurs_sup = [x for x in ma_liste if x > elt]

    return sum(valeurs_sup) / len(valeurs_sup)

print("===Test moy_sup()===")
print ( moy_sup([1,2,3,4,5,6,7,8,9], 2), "\n")

################################################################

def val_max(lst: list) -> float:
    """
    Retourne la valeur maximale d'une liste d'entiers.
    
    Args:
        lst (list): Liste d'entiers
        
    Returns:
        float: La valeur maximale de la liste
    """
    return max(lst)


print("===Test val_max()===")
print ( val_max([1,2,3,4,5,6,7,8,9]), "\n")

################################################################

def ind_max(lst: list) -> int:
    """
    Retourne l'indice de l'élément maximal d'une liste d'entiers.
    La liste est supposée sans répétition.
    
    Args:
        lst (list): Liste d'entiers sans répétition
        
    Returns:
        int: L'indice de l'élément maximal
    """
    max_val = max(lst)
    return lst.index(max_val)

print("===Test ind_max()===")
print ( ind_max([1,2,3,4,5,6,7,8,9]), "\n")

################################################################
print("-------------------")

# Exercice 2

def position(lst:list, elt:int)->int:
    """
        Retourne l'indice de l'élément elt dans la liste
        
        Args:
            lst (list): Liste d'entier sans répétition 
            elt (int): L'entier dont on doit trouver l'indice
        
        Returns:
            int: L'indice de elt
    """
    for valeur in lst:
        if valeur == elt:
            return lst.index(valeur)
    else:
        return -1
        
print("===Test position()===")
print ( position([1,2,3,4,5,6,7,8,9], 5), "\n")

################################################################

def position_while(lst:list, elt:int)->int:
    """
        Retourne l'indice de l'élément elt dans la liste
        
        Args:
            lst (list): Liste d'entier sans répétition 
            elt (int): L'entier dont on doit trouver l'indice
        
        Returns:
            int: L'indice de elt
    """
    i=0
    while i < len(lst):
        if elt == lst[i]:
            return lst.index(lst[i])
        i+=1
    else:
        return -1
        
        
print("===Test position_while()===")
print ( position_while([1,2,3,4,5,6,7,8,9], 5), "\n")

################################################################

def nb_occurrences(lst:list, e:int)->int:
    """
        Retourne le nombre d'occurrences de l'element e dans la liste lst
        
        Args:
            lst (list): Liste d'entier sans répétition 
            e (int): L'entier dont on doit trouver le nombre d'occurrences
        
        Returns:
            int: Le nombre d'occurrences de e
    """
    i=0
    j=0
    while i<len(lst):
        if e == lst[i]:
            j+=1
        i+=1
    return j
    
    #return lst.count(e)

print("===Test nb_occurrences()===")
print ( nb_occurrences([1,2,3,4,5,6,7,8,9,5,5,5], 5), "\n")

################################################################

print("-------------------")

# Exercice 3

def separer(lst:list)->list:
    """
        Retourne la liste des valeurs de lst par ordre croissant
        
        Args:
            lst (list): Liste d'entier sans répétition 
        
        Returns:
            list: La liste des valeurs de lst par ordre croissant
    """
    lsep = []
    negatif = [] 
    nul = []
    pos = []
    for i in lst:
        if lst[i] < 0:
            negatif.append(lst[i])
        elif lst[i] == 0 :
            nul.append(lst[i])
        else:
            pos.append(lst[i])
    lsep = negatif + nul + pos
    return lsep
    #lsep = sorted(lst)
    
print("===Test separer()===")
print ( separer([4,5,6,7,0,5,-4,-9,-7]), "\n")

################################################################

print("-------------------")

# Exrcice 4

def fizzbuzz(nb:int)->str:
    """ 
        Affiche la suite de FizzBuzz jusqu'au nombre indiqué
        
        Args:
            nb (int): Le nombre jusqu'auquel on affiche la suite
        
        Returns:
            str: La suite de FizzBuzz
    """
    for i in range(1,nb + 1):
        if i % 4 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 4 == 0:
            print("Buzz")
        else:
            print(i)
        
print("===Test fizzbuzz()===")
print ( fizzbuzz(12), "\n")

################################################################

print("-------------------")

# Exercice 5

def rendu(argent: float) -> tuple:
    """ 
        Affiche la suite de FizzBuzz jusqu'au nombre indiqué
        
        Args:
            argent (float): Le montant du rendu
        
        Returns:
            tuple: La liste des billets et pieges
    """
    # Round = arrondir
    argent = round(argent, 2)
    
    b500 = b200 = b100 = b50 = b20 = b10 = b5 = pe2 = pe1 = pc50 = pc20 = pc10 = pc5 = pc2 = pc1 = 0
    
    while argent > 0:
        if argent >= 500:
            argent -= 500
            b500 += 1
        elif argent >= 200:
            argent -= 200
            b200 += 1
        elif argent >= 100:
            argent -= 100
            b100 += 1
        elif argent >= 50:
            argent -= 50
            b50 += 1
        elif argent >= 20:
            argent -= 20
            b20 += 1
        elif argent >= 10:
            argent -= 10
            b10 += 1
        elif argent >= 5:
            argent -= 5
            b5 += 1
        elif argent >= 2:
            argent -= 2
            pe2 += 1
        elif argent >= 1:
            argent -= 1
            pe1 += 1
        elif argent >= 0.50:
            argent -= 0.50
            pc50 += 1
        elif argent >= 0.20:
            argent -= 0.20
            pc20 += 1
        elif argent >= 0.10:
            argent -= 0.10
            pc10 += 1
        elif argent >= 0.05:
            argent -= 0.05
            pc5 += 1
        elif argent >= 0.02:
            argent -= 0.02
            pc2 += 1
        elif argent >= 0.01:
            argent -= 0.01
            pc1 += 1
            
    
    return (b500, b200, b100, b50, b20, b10, b5, pe2, pe1, pc50, pc20, pc10, pc5, pc2, pc1)


print("===Test rendu()===")
print ( rendu(501), "\n")


print("-------------------")

# Exercice 6

def vitrine(nbEmplacement : int, lObjets : list)-> list:
    """ 
        Affiche la suite de FizzBuzz jusqu'au nombre indiqué
        
        Args:
            nbEmplacement (int): Le nombre d'emplacement de la vitrine
            lObjets (list): La liste des objets
            
        Returns:
            list: La liste des objets par ordre croissant
    """
    vitrinea = []
    vitrineb = []
    for i in lObjets:
        if i not in vitrinea and len(vitrinea) < nbEmplacement:
            vitrinea.append(i)
        else:
            if i not in vitrineb and len(vitrineb) < nbEmplacement:
                vitrineb.append(i)
        if len(vitrinea) == nbEmplacement and len(vitrineb) < nbEmplacement and i not in vitrineb:
            vitrineb.append(i)
            vitrinea.remove(i)
            
    return vitrinea, vitrineb
     

print("===Test vitrine()===")
print ( vitrine(4, [1,2,2,3,4,5,5]), "\n")

# Exercice 7 A NE PAS FAIRE
        

    
    

    
