from abc import ABC, abstractmethod
import math

class ColorMixin:
    def __init__(self, couleur="Aucune"):
        self.couleur = couleur

    def afficher_couleur(self):
        return f" (couleur : {self.couleur})"


class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"


class Cercle(ColorMixin, Forme):
    def __init__(self, rayon, couleur="Aucune"):
        ColorMixin.__init__(self, couleur)
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def __str__(self):
        return super().__str__() + self.afficher_couleur()


class Rectangle(ColorMixin, Forme):
    def __init__(self, largeur, hauteur, couleur="Aucune"):
        ColorMixin.__init__(self, couleur)
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def __str__(self):
        return super().__str__() + self.afficher_couleur()


class Carre(Rectangle):
    def __init__(self, cote, couleur="Aucune"):
        super().__init__(cote, cote, couleur)


class Triangle(ColorMixin, Forme):
    def __init__(self, base, hauteur, couleur="Aucune"):
        ColorMixin.__init__(self, couleur)
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur

    def __str__(self):
        return super().__str__() + self.afficher_couleur()


if __name__ == "__main__":
    formes = [
        Cercle(3, "Rouge"),
        Rectangle(4, 5, "Bleu"),
        Triangle(6, 2, "Vert"),
        Carre(4, "Jaune")
    ]

    for f in formes:
        print(f)
