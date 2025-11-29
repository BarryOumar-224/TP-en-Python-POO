# ===============================
# Exercice 2 — Classe Article
# ===============================

class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    # 1. Méthode valeur_stock : prix_ht * stock
    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock

    # 2. Méthode __str__
    def __str__(self):
        return (f"Réf {self.reference} — {self.designation} : "
                f"{self.stock} unités à {self.prix_ht} € HT")

    # 3. Extension : approvisionnement
    def approvisionner(self, qte: int):
        self.stock += qte
        with open("mouvements.log", "a", encoding="utf-8") as f:
            f.write(f"Approvisionnement : +{qte} unités sur {self.reference}\n")
