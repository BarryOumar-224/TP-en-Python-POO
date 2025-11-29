import json


# Classe de base : Document


class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        """Retourne True si le document est publié en 2000 ou après."""
        return self.annee >= 2000

    def to_dict(self):
        """Sérialisation générique du document."""
        return {
            "type": self.__class__.__name__,
            "titre": self.titre,
            "annee": self.annee
        }



# Sous-classe : Livre


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")

    def to_dict(self):
        d = super().to_dict()
        d["auteur"] = self.auteur
        return d



# Sous-classe : Magazine


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")

    def to_dict(self):
        d = super().to_dict()
        d["numero"] = self.numero
        return d



# Classe Bibliothèque


class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, document):
        self.documents.append(document)

    def afficher_tous(self):
        for d in self.documents:
            d.afficher()

    def rechercher(self, titre):
        """Recherche tous les documents contenant le mot dans le titre."""
        return [d for d in self.documents if titre.lower() in d.titre.lower()]

    def sauvegarder(self, fichier):
        """Sauvegarder tous les documents au format JSON."""
        data = [doc.to_dict() for doc in self.documents]
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger(self, fichier):
        """Charger une liste de documents depuis un JSON."""
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.documents = []  # Réinitialisation

        for d in data:
            if d["type"] == "Livre":
                self.ajouter(Livre(d["titre"], d["annee"], d["auteur"]))
            elif d["type"] == "Magazine":
                self.ajouter(Magazine(d["titre"], d["annee"], d["numero"]))
            else:
                self.ajouter(Document(d["titre"], d["annee"]))



# Programme principal (test)


if __name__ == "__main__":
    b = Bibliotheque()

    b.ajouter(Livre("1984", 1949, "George Orwell"))
    b.ajouter(Magazine("Science & Vie", 2023, 456))
    b.ajouter(Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"))
    b.ajouter(Magazine("National Geographic", 2021, 78))

    print("=== Tous les documents ===")
    b.afficher_tous()

    print("\n=== Recherche: 'Vie' ===")
    for doc in b.rechercher("Vie"):
        doc.afficher()

    print("\n=== Documents récents (>= 2000) ===")
    for doc in b.documents:
        if doc.est_recent():
            doc.afficher()

    # Sauvegarde
    b.sauvegarder("biblio.json")

    # Démonstration du chargement
    print("\n=== Après rechargement ===")
    b2 = Bibliotheque()
    b2.charger("biblio.json")
    b2.afficher_tous()
