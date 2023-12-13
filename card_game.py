# ========================================================================
# ===  Importation du module randint de la bibliothèque python random  ===
# ========================================================================
from random import randint

# ====================================
# ===  Création de la classe Card  ===
# ====================================
class Card:
    
    def __init__(self, nom, description, cout):
        self.__nom = nom
        self.__description = description
        self.__cout_en_mana = cout
        
    
    def get_Name(self):
        return self.__nom
        
    def get_Description(self):
        return self.__description
        
    def get_Cout(self):
        return self.__cout_en_mana  


# ====================================
# ===  Création de la classe Mage  ===
# ====================================    
class Mage:
    
    def __init__(self, nom, pv_initiaux, pv_courant, mana_initial, mana_courant):
        self.__nom = nom
        self.__pv_initiaux = pv_initiaux
        self.__pv_courant = pv_courant
        self.__mana_initial = mana_initial
        self.__mana_courant = mana_courant
        self.__main = {}
        self.__defausse = []
        self.__zone_de_jeu = ""
        
    def get_Name(self):
        return self.__nom
    
    def get_Pv_initiaux(self):
        return self.__pv_initiaux
    
    def get_Pv_courant(self):
        return self.__pv_courant
    
    def get_Mana_initial(self):
        return self.__mana_initial
    
    def get_Mana_courant(self):
        return self.__mana_courant
    
    def get_Main(self):
        return self.__main
    
    def get_Defausse(self):
        return self.__defausse
    
    def get_Zone_de_jeu(self):
        return self.__zone_de_jeu
    
    
    def play_card(self, card):
        """
        méthode ayant pour but d'ajouter a la zone de jeu une carte qui
        sera retirée de la main du mage
        """
        # self.__zone_de_jeu.append(card)
        # self.__main.pop(self.__main[card])
    
    def recover_mana(self):
        self.__mana_courant = self.__mana_initial
    
    def attack_mage(self,cible):
        cible.__pv_courant -= self.__zone_de_jeu.get_Card().get_Score_attaque()


# ==================================================================================
# ===  Création de la classe Cristal qui hérite des ettributs de la classe Card  ===
# ==================================================================================
class Cristal(Card):
    
    def __init__(self, nom, description, cout, valeur):
        super().__init__(nom, description, cout)
        self.__valeur = valeur
        
        
    def get_Valeur(self):
        return self.__valeur


# ====================================================================================
# ===  Création de la classe Créatures qui hérite des ettributs de la classe Card  ===
# ====================================================================================
class Creatures(Card):
    
    def __init__(self, nom, description, cout, pv_initiaux, pv_courant, score_attaque):
        super().__init__(nom, description, cout)
        
        self.__pv_initiaux = pv_initiaux
        self.__pv_courant = pv_courant
        self.__score_attaque = score_attaque

    def get_Pv_initiaux(self):
        return self.__pv_initiaux
        
    def get_Pv_courant(self):
        return self.__pv_courant
        
    def get_Score_attaque(self):
        return self.__score_attaque 
    
    """
    def attack(self,cible):
        cible.get_Pv_courant() -= self.__score_attaque # Je ne comprend pas pourquoi il me fait une erreur
    """
    
    def perd_pv(self, degats):
        self.__pv_courant -= degats
    
    def update_defausse(self,cible):
        cible.get_Defausse().append(self)


# ================================================================================
# ===  Création de la classe Blast qui hérite des ettributs de la classe Card  ===
# ================================================================================
class Blast(Card):
    
    def __init__(self, nom, description, cout, valeur):
        super().__init__(nom, description, cout)
        
        self.__valeur = valeur
        
    def get_Valeur(self):
        return self.__valeur
    
    def use(self,lanceur,cible):
        """ 
        méthode ayant pour objectif de faire des dégats a la cible et que la carte
        soit retirer de la zone de jeux du lanceur
        """

        # Manque de temps

# ========================
# ===  Code principal  ===
# ========================

print("\033c", end="") # Permet de nettoyer la console a chaque exécution du fichier "main_code.py"

joueur_1 = Mage("Andeddo", 100, 100, 50, 50)
joueur_2 = Mage("Koda", 100, 100, 50, 50)

def pioche(cible):
    
    type_card = int(randint(1,3))
    
    if type_card == 1:
        cible.get_Main()[f"Carte {len(cible.get_Main())+1}"] = Cristal("Coeur de dragon","Un coeur de dragon plutôt gros ...", 10, 20)
        
    elif type_card == 2:
        cible.get_Main()[f"Carte {len(cible.get_Main())+1}"] = Creatures("Ogre","Un gros tas de muscle sans cervelle", 5, 30, 30, 10)
        
    else:
        cible.get_Main()[f"Carte {len(cible.get_Main())+1}"] = Blast("Fire ball","Le feu, ça brule", 5, 15)


print(joueur_1.get_Name(), joueur_1.get_Main())
print(joueur_2.get_Name(), joueur_2.get_Main())

pioche(joueur_1)
pioche(joueur_2)

pioche(joueur_1)
pioche(joueur_2)

pioche(joueur_1)
pioche(joueur_2)

print(joueur_1.get_Name(), joueur_1.get_Main())
print(joueur_2.get_Name(), joueur_2.get_Main())















