class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")


class Chien(Animal):
    def parler(self):
        return "Ouaf !"


class Chat(Animal):
    def parler(self):
        return "Miaou !"



class Vache(Animal):
    def parler(self):
        return "Meuh !"



def faire_parler(animal):   
    print(animal.parler())



class Robot:
    def parler(self):
        return "Bip bip, je parle comme un robot."



animaux = [Chien(), Chat(), Vache(), Chien(), Robot()]  # mélange d’objets

for a in animaux:
    faire_parler(a)
