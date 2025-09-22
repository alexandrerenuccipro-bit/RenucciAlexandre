# atelier_1

import math

# Exercice 1
def message_imc(imc: float) -> str:
    """
    Détermine la catégorie de corpulence selon l'IMC
    
    Args:
        imc (float): L'Indice de Masse Corporelle calculé
        
    Returns:
        str: Message correspondant à la catégorie de corpulence
    """
    if imc < 16.5:
        return "denutrition ou famine"
    elif imc < 18.5:
        return "maigreur"
    elif imc < 25:
        return "corpulence normale"
    elif imc < 30:
        return "surpoids"
    elif imc < 35:
        return "ob"
    elif imc < 40: 
        return "ob s"
    else:
        return "ob m"

# Test Exercice 1
print("message_imc(22.5):", message_imc(22.5))  

##############################################################################

# Exercice 2
def est_bissextile(annee: int) -> bool:
    """
    Vérifie si une année est bissextile
    
    Args:
        annee (int): L'année à vérifier
        
    Returns:
        bool: True si l'année est bissextile, False sinon
    """
    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        return True
    else:
        return False

# Test Exercice 2
print("est_bissextile(2024):", est_bissextile(2024))  

##############################################################################

# Exercice 3
def distance(xa: int, xb: int, ya: int, yb: int, za: int, zb: int) -> float:
    """
    Calcule la distance euclidienne entre deux points dans l'espace 3D
    
    Args:
        xa, ya, za (int): Coordonnées du premier point
        xb, yb, zb (int): Coordonnées du second point
        
    Returns:
        float: Distance entre les deux points
    """
    return math.sqrt((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)

# Test Exercice 3
print("distance(0, 3, 0, 4, 0, 0):", distance(0, 3, 0, 4, 0, 0))  

##############################################################################

# Exercice 4
def inegalite_triangulaire(a: float, b: float, c: float) -> bool:
    """
    Vérifie si trois longueurs peuvent former un triangle
    
    Args:
        a, b, c (float): Les trois côtés du triangle
        
    Returns:
        bool: True si les côtés peuvent former un triangle, False sinon
    """
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

# Test Exercice 4
print("inegalite_triangulaire(3, 4, 5:", inegalite_triangulaire(3, 4, 5))  

##############################################################################

# Exercice 5
def conversion_masse(poids: float, unite_initiale: str, unite_voulue: str) -> float:
    """
    Convertit une masse d'une unité vers une autre
    
    Args:
        poids (float): La masse à convertir
        unite_initiale (str): L'unité de départ
        unite_voulue (str): L'unité d'arrivée
        
    Returns:
        float: La masse convertie (0 si erreur)
    """
    unites = ["tonnes", "qgrammes", "dkgrammes", "kilos", "hgrammes", 
              "dagrammes", "grammes", "dgrammes", "cgrammes", "mgrammes"]
    
    if unite_initiale not in unites or unite_voulue not in unites:
        print("Erreur: unité non reconnue")
        return 0
    
    position_init = unites.index(unite_initiale)
    position_final = unites.index(unite_voulue)
    facteur = position_final - position_init
    
    return poids * (10 ** facteur)

# Test Exercice 5
print('conversion_masse(2, "kilos", "grammes")', conversion_masse(2, "kilos", "grammes")) 

##############################################################################

# Exercice 6
def calculer_impots_v2(mon_revenu: float, nb_adultes: int, nb_enfants: int) -> float:
    """
    Calcule le montant des impôts sur le revenu français
    
    Args:
        mon_revenu (float): Revenu annuel imposable en euros
        nb_adultes (int): Nombre d'adultes dans le foyer fiscal
        nb_enfants (int): Nombre d'enfants à charge
        
    Returns:
        float: Montant des impôts à payer en euros
    """
    if mon_revenu < 0 or nb_adultes < 1 or nb_enfants < 0:
        print("Erreur: valeurs invalides")
        return 0
    
    quotient = nb_adultes + 0.5 * nb_enfants
    revenu_par_part = mon_revenu / quotient
    
    impot_par_part = 0
    
    if revenu_par_part <= 11497:
        impot_par_part = 0
    else:
        if revenu_par_part > 11497:
            impot_par_part += (min(29315, revenu_par_part) - 11497) * 0.11
        
        if revenu_par_part > 29315:
            impot_par_part += (min(83823, revenu_par_part) - 29315) * 0.30
        
        if revenu_par_part > 83823:
            impot_par_part += (min(180294, revenu_par_part) - 83823) * 0.41
        
        if revenu_par_part > 180294:
            impot_par_part += (revenu_par_part - 180294) * 0.45
    
    impot_brut = impot_par_part * quotient
    
    if nb_adultes >= 2 and impot_brut < 3248:
        decote = 1470 - (impot_brut * 0.4525)
        return max(0, impot_brut - decote)
    
    elif nb_adultes == 1 and impot_brut < 1964:
        decote = 889 - (impot_brut * 0.4525)
        return max(0, impot_brut - decote)
    
    return impot_brut

# Test Exercice 6
print("calculer_impots_v2(25000, 1, 0):", calculer_impots_v2(25000, 1, 0)) 

####################################################################

# Exercice 6 amélioration IA (Claude)

"""
    Améliorations apportées :

    Quotient familial corrigé : À partir du 3ème enfant, chaque enfant supplémentaire compte pour une part complète (1.0) au lieu de 0.5
    Seuil de recouvrement ajouté : Si l'impôt calculé est inférieur à 61€, il n'y a rien à payer
    Arrondi à l'euro : Le résultat est arrondi comme dans la réalité
    Tests simples : Quelques exemples pour vérifier que ça marche
"""

def calculer_impots_ameliore(mon_revenu: float, nb_adultes: int, nb_enfants: int) -> float:
    """
    Calcule le montant des impôts sur le revenu français selon le barème 2025.
    
    Args:
        mon_revenu (float): Revenu annuel imposable en euros
        nb_adultes (int): Nombre d'adultes dans le foyer fiscal (1 ou 2)
        nb_enfants (int): Nombre d'enfants à charge
        
    Returns:
        float: Montant des impôts à payer en euros
    """
    # Validation simple
    if mon_revenu < 0 or nb_adultes < 1 or nb_enfants < 0:
        print("Erreur: valeurs invalides")
        return 0
    
    # Calcul du quotient familial (corrigé pour 3ème enfant et plus)
    if nb_enfants <= 2:
        quotient = nb_adultes + 0.5 * nb_enfants
    else:
        quotient = nb_adultes + 1.0 + (nb_enfants - 2) * 1.0
    
    revenu_par_part = mon_revenu / quotient
    
    # Calcul de l'impôt par part (barème 2025)
    impot_par_part = 0
    
    if revenu_par_part > 11497:
        impot_par_part += (min(29315, revenu_par_part) - 11497) * 0.11
    
    if revenu_par_part > 29315:
        impot_par_part += (min(83823, revenu_par_part) - 29315) * 0.30
    
    if revenu_par_part > 83823:
        impot_par_part += (min(180294, revenu_par_part) - 83823) * 0.41
    
    if revenu_par_part > 180294:
        impot_par_part += (revenu_par_part - 180294) * 0.45
    
    impot_brut = impot_par_part * quotient
    
    # Application de la décote
    if nb_adultes >= 2 and impot_brut < 3248:
        decote = 1470 - (impot_brut * 0.4525)
        impot_final = max(0, impot_brut - decote)
    elif nb_adultes == 1 and impot_brut < 1964:
        decote = 889 - (impot_brut * 0.4525)
        impot_final = max(0, impot_brut - decote)
    else:
        impot_final = impot_brut
    
    # Seuil de recouvrement : pas d'impôt si < 61€
    if impot_final < 61:
        return 0
    
    return round(impot_final, 0)


# Tests simples
if __name__ == "__main__":
    print("=== TESTS ===")
    
    # Test 1: Célibataire 30000€
    print(f"Célibataire 30000€: {calculer_impots_ameliore(30000, 1, 0)}€")
    
    # Test 2: Couple 2 enfants 60000€
    print(f"Couple + 2 enfants 60000€: {calculer_impots_ameliore(60000, 2, 2)}€")
    
    # Test 3: Famille nombreuse (3+ enfants)
    print(f"Couple + 3 enfants 50000€: {calculer_impots_ameliore(50000, 2, 3)}€")
    print(f"Couple + 4 enfants 50000€: {calculer_impots_ameliore(50000, 2, 4)}€")



