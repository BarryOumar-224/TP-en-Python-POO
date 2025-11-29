class Convertisseur:
    # Attribut de classe
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        """Convertit des euros vers des dirhams selon le taux actuel."""
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux: float):
        """Modifie le taux de conversion pour toute la classe."""
        cls.taux_eur_dh = nv_taux

    @staticmethod
    def vers_eur(dirhams: float) -> float:
        """Convertit des dirhams vers des euros selon le taux actuel."""
        return dirhams / Convertisseur.taux_eur_dh
