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