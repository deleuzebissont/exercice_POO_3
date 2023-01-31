import random


def number():
    # nous creons ici le nombre demande par les instructions
    nombre_1 = random.randint(1, 6)
    nombre_2 = random.randint(1, 6)
    nombre_3 = random.randint(1, 6)
    nombre_4 = random.randint(1, 6)
    liste = [nombre_1, nombre_2, nombre_3, nombre_4]
    # nous placons les nombres de la liste en ordre croissant
    liste.sort()
    # nous eleminons le nombre le plus faible
    liste.pop(0)
    nombre = sum(liste)
    return nombre


class npc:
    def __init__(self):
        # nous definissons tout les caracteristiques du npc (par exemple, son nom
        self.name = str
        self.race = str
        self.espece = str
        self.profession = str
        self.number = number()
        self.force = number()
        self.agilite = number()
        self.constitution = number()
        self.intelligence = number()
        self.sagesse = number()
        self.charisme = number()
        self.classe_armure = random.randint(1, 12)
        self.point_de_vie = random.randint(1, 20)

    def afficher_infos(self):
        # la methode permet ici d afficher toutes les caracteristiques definis plus tot
        print(f"""
      Caracteristiques :
      Force : {self.force}
      Agilite : {self.agilite}
      Constitution : {self.constitution}
      Intelligence : {self.intelligence}
      Sagesse : {self.sagesse}
      Charisme : {self.charisme}
      Classe armure : {self.classe_armure}
      Point de vie : {self.point_de_vie}
      """)


class kobold(npc):
    # la classe heritiere est initialise
    def __init__(self):
        super().__init__()

    # le kobold ne peut attaquer
    def attaquer(self):
        return

    # le kobold peut seulement subir des dommages, c'est donc ici qu on effectue cette operation
    def subir_dommage(self, quantite_de_dommage):
        self.point_de_vie -= quantite_de_dommage


class hero(npc):
    # on recoit la cible en parametre et la quantite de dommage un peu plus bas
    def __init__(self):
        super().__init__()

    # on definit la methode attaquer selon les caracteristiques expliques ( ex si dee = 20 = on fait des degats de 1
    # a 8)
    def attaquer(self, cible):
        dee_20 = random.randint(1, 20)
        if dee_20 == 20:
            cible.subir_dommage(random.randint(1, 8))
        elif dee_20 == 1:
            return
        elif dee_20 >= cible.classe_armure:
            cible.subir_dommage(random.randint(1, 6))

    # le hero ne peut subir de dommages
    def subir_dommage(self):
        return
