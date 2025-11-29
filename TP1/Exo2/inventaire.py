# ===============================
# Exercice 2 — Inventaire
# ===============================

from article import Article

# 1. Création de trois articles
a1 = Article("A101", "Clavier mécanique", 79.90, 10)
a2 = Article("A205", "Souris gaming", 49.50, 25)
a3 = Article("B330", "Écran 27 pouces", 189.00, 5)

articles = [a1, a2, a3]

# 2. Affichage des articles
for a in articles:
    print(a)

# 3. Calcul de la valeur totale de l’inventaire
total = sum(a.valeur_stock() for a in articles)
print(f"\nValeur d’inventaire : {total:.2f} €")

# 4. Test de l’approvisionnement (facultatif)
a1.approvisionner(5)
a3.approvisionner(2)
