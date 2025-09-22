#StPeM = St Pierre et Miquelon
destination = ['France', 'Monaco', 'Andorre', 
              'SP', 'Guyane', 'Guadeloupe', 
              'Martinique', 'Réunion', 'StPeM', 
              'St Barthélémy', 'St-Martin', 'Mayotte',
              'Nouvelle-Calédonie','Polynésie française','Wallis-et-Futuna','T.A.A.F']

taxeGGMRSSSM = ['Guyane', 'Guadeloupe' , 'Martinique' , 'Réunion' , 'StPeM' , 'St Barthélémy' , 'St-Martin' , 'Mayotte']

taxeNCPWT = ['Nouvelle-Calédonie' , 'Polynésie française' , 'Wallis-et-Futuna' , 'T.A.A.F']

typeLettre = ['Verte', 'Prioritaire', 'Ecopli', 'Colissimo Eco Outre-Mer']

#Poids & prix d'une lettre verte
poidsVerte = [20, 100,250,500,1000, 3000, 'Sticker Suivi']
prixVerte = [1.16, 2.32, 4.00, 6.00, 7.50, 10.50, 0.50]

# Poids & prix Prioritaire
poidsPrioritaire = [20, 100, 250, 500, 3000, "Sticker Suivi"]
prixPrioritaire = [1.43, 2.86, 5.26, 7.89, 11.44, 0.50]

# Poids & prix Ecopli
poidsEcopli = [20, 100, 250, "Sticker Suivi"]
prixEcopli = [1.14, 2.28, 3.92, 0.50]

# Poids & prix Colissimo Eco Outre-Mer
poidsCEOM = [500, 1000, 2000, 5000, 10000, 15000, 30000]
prixCEOM = [8.35, 11.20, 14.10, 23.65, 37.50, 75.85, 87.40]

def affranchissement(poids):
    destinationEnvoie = input("Veuillez choisir la destination \n")
    typeDeLettre = input("Veuillez choisir le Type de votre lettre \n")
    prix=0
    """
        
    """
    
    if destinationEnvoie not in destination: 
        return "Nous ne deservons pas cette destination"
    elif typeDeLettre not in typeLettre:
        return "Nous ne connaissons pas ce type de lettre"
    else:
        i=0
        if typeDeLettre == "Verte":
            while poids>=poidsVerte[i]:
                i+=1
                prix = prixVerte[i]
                
            if poids<=poidsVerte[i]:
                prix = prixVerte[0]
                    
            if destinationEnvoie in taxeGGMRSSSM:
                surplus = poids % 10
                prix = prix + surplus*0.05
                return prix
            elif destinationEnvoie in taxeNCPWT:
                surplus = poids % 10
                prix = prix + surplus*0.11
                return prix
            else:
                return prix

        elif typeDeLettre == "Prioritaire":
            while poids>=poidsPrioritaire[i]:
                i+=1
                prix = prixPrioritaire[i]
                
            if poids<=poidsPrioritaire[i]:
                prix = prixPrioritaire[0]
                
            if destinationEnvoie in taxeGGMRSSSM:
                surplus = poids % 10
                prix = prix + surplus*0.05
                return prix
            elif destinationEnvoie in taxeNCPWT:
                surplus = poids % 10
                prix = prix + surplus*0.11
                return prix
            else:
                return prix
                
        elif typeDeLettre == "Ecopli":
            while poids>=poidsEcopli[i]:
                i+=1
                prix = prixEcopli[i]
                
            if poids<=poidsEcopli[i]:
                prix = prixEcopli[0]
                
            if destinationEnvoie in taxeGGMRSSSM:
                surplus = poids % 10
                prix = prix + surplus*0.05
                return prix
            elif destinationEnvoie in taxeNCPWT:
                surplus = poids % 10
                prix = prix + surplus*0.11
                return prix
            else:
                return prix
    
        elif typeDeLettre == "Colissimo Eco Outre-Mer":
            while poids>=poidsCEOM[i]:
                i+=1
                prix = prixCEOM[i]
                return prix
            
        
        
    