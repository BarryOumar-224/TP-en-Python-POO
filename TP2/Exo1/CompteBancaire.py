class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        # Attribut protégé (accès contrôlé mais visible pour les classes dérivées)
        self._titulaire = titulaire
        
        # Attribut privé → non accessible de l’extérieur
        self.__solde = 0  
        self.__set_solde_initial(solde_initial)



    def __set_solde_initial(self, solde):
        """Méthode interne pour initialiser le solde avec validation."""
        if isinstance(solde, (int, float)) and solde >= 0:
            self.__solde = solde
        else:
            raise ValueError("Le solde initial doit être un nombre positif.")

    def __modifier_solde(self, montant):
        """Méthode privée pour modifier le solde (centrale et sécurisée)."""
        self.__solde += montant



    def deposer(self, montant):
        """Dépose un montant valide dans le compte."""
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.__modifier_solde(montant)

    def retirer(self, montant):
        """Retire un montant en respectant les limites."""
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.__solde:
            raise ValueError("Fonds insuffisants.")
        self.__modifier_solde(-montant)

    @property
    def solde(self):
        """Propriété en lecture seule : empêche toute écriture externe."""
        return self.__solde

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
