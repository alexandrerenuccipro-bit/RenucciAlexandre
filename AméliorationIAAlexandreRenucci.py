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
