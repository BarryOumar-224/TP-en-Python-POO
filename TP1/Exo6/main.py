from convertisseur import Convertisseur

montant = 100
print("Avant mise à jour :", Convertisseur.vers_dh(montant))

Convertisseur.mettre_a_jour_taux(11.2)
print("Après mise à jour  :", Convertisseur.vers_dh(montant))

# Test de l'extension
print("1120 DH en euros   :", Convertisseur.vers_eur(1120))
