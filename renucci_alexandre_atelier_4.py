from random import *

###################################################################

#Partie 
#Exo 1

def gen_list_random_int(int_binf=0, int_bsup=10-1, int_nbr=10) -> list:
    """
    Génère une liste de n entiers aléatoires entre deux bornes.
    Args:
        int_binf (int): La borne inférieure. Par défaut à 0.
        int_bsup (int): La borne supérieure. Par défaut à 9.
        int_nbr (int): Le nombre d'entiers à générer. Par défaut à 10.
    Returns:
        list: La liste de n entiers aléatoires.
    """
    return [randint(int_binf,int_bsup) for i in range(int_nbr)]

#print(gen_list_random_int(10,20,5)) #[15, 13, 18, 14, 18]
#print(gen_list_random_int(10,20)) #[20, 13, 15, 16, 18, 19, 15, 19, 14, 13]
#print(gen_list_random_int()) #[3, 7, 6, 0, 3, 7, 3, 0, 1, 1]

###################################################################

#Exo 2

def mix_list(list_to_mix:list) -> list:
    """ 
    Mélange une liste aléatoirement.
    Args:
        list_to_mix (list): La liste à mélanger
    Returns:
        list: La liste mélangée
    """
    list_mixed = []
    for i in range(len(list_to_mix)):
        list_mixed.append(list_to_mix.pop(randint(0,len(list_to_mix)-1)))
    return list_mixed

#print(mix_list([1,2,3,4,7])) 

###################################################################

#Exo 3

def choose_element_list(list_in_which_to_choose:list) -> any:
    """
    Choisis un élément de la liste aléatoirement.
    Args:
        list_in_which_to_choose (list): La liste de choix
    Returns:
        any: L'element choisi
    """
    return list_in_which_to_choose[randint(0,len(list_in_which_to_choose)-1)]


#print(choose_element_list([1,2,3,4,5,6,7,8,9,"fruit","légume","viande"]))

###################################################################

#Exo 4

def extract_elements_list (list_in_which_to_choose:list, int_nbr_element_to_extract:int) -> list:
    """
    Extrait n éléments d'une liste aléatoirement.
    Args:
        list_in_which_to_choose (list): La liste de choix
        int_nbr_element_to_extract (int): Le nombre d'éléments à extraire
    Returns:
        list: La liste des éléments extraits
    """
    list_extracted = []
    for i in range(int_nbr_element_to_extract):
        list_extracted.append(list_in_which_to_choose.pop(randint(0,len(list_in_which_to_choose)-1)))
    return list_extracted

print(extract_elements_list([1,2,3,4,5,6,7,8,9,"fruit","légume","viande"],5))
