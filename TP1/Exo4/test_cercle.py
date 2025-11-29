from cercle import Cercle
from math import pi

c = Cercle(3)
print(c.perimetre)  # 2πr
print(c.surface)    # πr²

try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturée :", e)

# Test de la méthode agrandir (optionnel)
c = Cercle(10)
c.agrandir(50)  # augmente le rayon de 50%
print("Nouveau rayon :", c.rayon)
print("Nouvelle surface :", c.surface)
