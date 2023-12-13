class Carte:
    def __init__(self,mana,name,description):
        self.__manacost = mana
        self.__name = name
        self.__description = description
    def getManacost(self):
        return self.__manacost
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description

class Mage:
    def __init__(self,name,PV,total,mana,main,zone,defausse):
        self.__name = name
        self.__PV = PV
        self.__total = total
        self.__mana = mana
        self.__main = main
        self.__zone = zone
        self.__defausse = defausse
    def jouer(self,carte):                  #quand on joue une carte
        self.__mana-= self.__main[carte].getManacost()
        self.__main[carte].jouer(self)
        self.__main.pop(carte)
    def defausse(self,carte):               #appelé quand on joue une carte blast
        self.__defausse.append(carte)
    def zone(self,carte):                   #appelé quand on joue une carte cristal ou créature
        self.__zone.append(carte)
    def PerdPv(self,PVperdus):
        self.__PV -= PVperdus
    def getmain(self):
        temp = []
        for i in range(len(self.__main)):
            temp.append(self.__main[i].getName())
        return temp
    def getzone(self):
        temp = []
        for i in range(len(self.__zone)):
            temp.append(self.__zone[i].getName())
        return temp
    def getName(self):
        return self.__name
    def GagneMana(self,nombre):
        self.__mana += nombre

class Cristal(Carte):
    def __init__(self,mana,name,description,valeur):
        Carte.__init__(self,mana,name,description)
        self.__valeur = valeur
    def jouer(self,mage):
        mage.zone(self)
    def gagneMana(self,mage):           #appelé quand la carte est dans la zone de jeu
        mage.GagneMana(self.__valeur)

class Creature(Carte):
    def __init__(self,mana,name,description,pv,attaque):
        Carte.__init__(self,mana,name,description)
        self.__pv = pv
        self.__attaque = attaque
    def jouer(self,mage):
        mage.zone(self)
    def attaquer(self,cible):           #appelé quand la carte est dans la zone de jeu
        cible.perdPv(self.__attaque)
    def perdPv(self,nombre,mage):
        self.__pv -= nombre
        if self.__pv<=0:
            mage.defausse(self)


class Blast(Carte):
    def __init__(self,mana,name,description,valeur):
        Carte.__init__(self,mana,name,description)
        self.__valeur = valeur
    def jouer(self,mage,cible):
        mage.defausse(self)
        cible.perdPv(self.__valeur)

cristal1 = Cristal(4,"cristal1","un cristal qui donne 1 mana",1)
mage1 = Mage("mage1",100,100,5,[cristal1],[],[])


print(mage1.getmain())
print(mage1.getzone())
mage1.jouer(0)
print(mage1.getmain())
print(mage1.getzone())