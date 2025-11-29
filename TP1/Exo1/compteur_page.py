# ===============================
# Exercice 1 — Compteur de visites
# ===============================

class CompteurPage:
    # 1. Attribut de classe
    total_visites = 0

    # 2. Méthode spéciale __init__
    def __init__(self, url: str):
        self.url = url                      # attribut d’instance : URL
        CompteurPage.total_visites += 1     # incrémentation de l’attribut de classe

        # Extension : attribut d’instance visites_par_page
        self.visites_par_page = 0

    # 3. Méthode afficher_stats
    def afficher_stats(self) -> str:
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"

    # 5. Extension : méthode enregistrer_lecture
    def enregistrer_lecture(self):
        self.visites_par_page += 1
