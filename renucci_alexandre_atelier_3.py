import random

# Atelier 3

# Exercice 1 1)

def full_name(str_arg:str)->str:
   """
        Retourne le nom et le prénom en majuscule

        Args:
            str_arg (str): Le nom et le prrenom

        Returns:
            str: Le nom et le prrenom en majuscule
   """
   parts = str_arg.split()
   
   if len(parts) != 2:
       return "" 
   
   nom, prenom = parts
   
   nom_majuscule = nom.upper()
   prenom_formate = prenom.capitalize()
   
   return f"{nom_majuscule} {prenom_formate}"

###################################################################

# 2)

def is_mail(str_arg:str)-> (tuple[int,int]) : 
    """
        Retourne 1 si l'adresse mail est correcte et 0 sinon

        Args:
            str_arg (str): L'adresse mail

        Returns:
            tuple[int,int]: 1,0 si l'adresse mail est correcte et 0,x sinon avec x un chiffre entre 1 et 4 selon l'erreur
    """
    if '@' not in str_arg:
        return (0,2)
    
    debut , fin = str_arg.split('@')
    
    if '.' not in fin:
        return (0,4)
    
    domaine , fr = fin.split('.')
    
    if len(debut) == 0:
        return (0,1)
    
    elif domaine != 'univ-corse':
        return (0,3)
    else:
        return (1,0)
    
###################################################################

# Exercice 2 1)

def mots_Nlettres(lst_mot:list , n:int)-> list:
    """
        Retourne la liste des mots de longueur n

        Args:
            lst_mot (list): La liste des mots
            n (int): La longueur des mots

        Returns:
            list: La liste des mots de longueur n
    """
    resultat = []
    for mot in lst_mot:
        if len(mot) == n:
            resultat.append(mot)
    return resultat

###################################################################

# 2)

def commence_par(mot:str ,prefixe:str)->bool:
    """
        Retourne True si le mot commence par le prefixe et False sinon

        Args:
            mot (str): Le mot
            prefixe (str): Le prefixe

        Returns:
            bool: True si le mot commence par le prefixe et False sinon
    """
    if mot[0]==prefixe:
        return True
    else:
        return False

###################################################################

# 3)

def finit_par(mot:str,suffixe:str)->bool:
    """
        Retourne True si le mot finit par le suffixe et False sinon

        Args:
            mot (str): Le mot
            suffixe (str): Le suffixe

        Returns:
            bool: True si le mot finit par le suffixe et False sinon
    """
    if mot[-1]==suffixe:
        return True
    else:
        return False
    
###################################################################

# 4)

def finissent_par(lst_mot:list, suffixe:str)->list:
    """
        Retourne la liste des mots qui finissent par le suffixe

        Args:
            lst_mot (list): La liste des mots
            suffixe (str): Le suffixe

        Returns:
            list: La liste des mots qui finissent par le suffixe
    """
    resultat = []
    for i in lst_mot:
        if i[-1]==suffixe:
            resultat.append(i)
    return resultat

###################################################################

# 5)

def commencent_par(lst_mot:list, prefixe:str)->list:
    """
        Retourne la liste des mots qui commencent par le prefixe

        Args:
            lst_mot (list): La liste des mots
            prefixe (str): Le prefixe

        Returns:
            list: La liste des mots qui commencent par le prefixe
    """
    resultat = []
    for i in lst_mot:
        if i[0]==prefixe:
            resultat.append(i)
    return resultat

###################################################################

# 6)

#def liste_mots(lst_mot:list, prefixe:str, suffixe:str, n:int)->list:
    

###################################################################

# 7)

#def dictionnaire(fichier):
    

###################################################################

# Pendu

def places_lettre(ch: str, mot: str) -> list:
    """
        Renvoie la liste des positions d'une lettre dans un mot.

        Args:
            ch (str): La lettre recherchée
            mot (str): Le mot

        Returns:
            list: La liste des positions
    """
    positions = []
    for i in range(len(mot)):
        if mot[i] == ch:
            positions.append(i)
    return positions

def outputStr(mot: str, lpos: list) -> str:
    """
        Renvoie le mot formatté en fonction des positions des lettre dans un mot.

        Args:
            mot (str): Le mot
            lpos (list): La liste des positions

        Returns:
            str: Le mot formatté
    """
    result = ""
    for i in range(len(mot)):
        if i in lpos:
            result += mot[i] + " "
        else:
            result += "_ "
    return result.strip()

def runGame():
    """
        Fonction pour lancer le jeu
    """
    lst = ['ajaccio', 'bastia', 'paris', 'londres', 'madrid', 'berlin', 'new-york', 
           'le barca est le meilleur club du monde', 'messi>>>penaldo','dix>>>>>>>sept']
    
    mot = random.randint(0, len(lst)-1)
    mot_secret = lst[mot]
    
    lettres_trouvees = []
    erreurs = 0
    
    C5 = "|---] \n| O \n| T \n|/ \ \n|______ "
    C4 = "| O \n| T \n|/ \ \n|______"
    C3 = "| T \n|/ \ \n|______"
    C2 = "|/ \ \n|______"
    C1 = "|______"
    
    print(f"Mot à deviner: {outputStr(mot_secret, [])}")
    
    while erreurs < 5 and len(lettres_trouvees) < len(mot_secret):
        lettre = input("Entrez une lettre: ").lower()
        
        positions = places_lettre(lettre, mot_secret)
        
        if positions:
            lettres_trouvees.extend(positions)
            print(f"État actuel: {outputStr(mot_secret, lettres_trouvees)}")
        else:
            erreurs += 1
            print(f"État actuel: {outputStr(mot_secret, lettres_trouvees)}")
            
            if erreurs == 1:
                print(C1)
            elif erreurs == 2:
                print(C2)
            elif erreurs == 3:
                print(C3)
            elif erreurs == 4:
                print(C4)
            elif erreurs == 5:
                print(C5)
        
        print(f"Coups restants: {5 - erreurs} \n")
    
    if len(lettres_trouvees) == len(mot_secret):
        print("GAGNÉ !")
        print(f"Le mot était: {mot_secret}")
    else:
        print("PERDU ! \nT'es éteint")
        print(f"Le mot était: {mot_secret}")

print(runGame())

###################################################################

def test_exercice1():
    # test full_name
    print(full_name("renucci alexandre"), '\n') #RENUCCI Alexandre
    
    # test is_mail
    print(is_mail('alex@univ-corse.fr')) #(1, 0)
    print(is_mail('alex@univ-cose.fr')) #(0, 3)
    print(is_mail('@univ-corse.fr')) #(0, 1)
    print(is_mail('alex@univ-corsefr'), '\n') #(0, 4)
    
    # test mots_Nlettres
    lst_mot = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"]
    print(mots_Nlettres(lst_mot, 5), '\n') #['jouer', 'punir', 'finir', 'aimer'] 
