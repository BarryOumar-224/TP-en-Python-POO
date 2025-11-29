import uuid
from datetime import datetime

class CompteBancaire:
    def __init__(self, solde_initial=0.0):
        self.id = uuid.uuid4()                 # Identifiant unique
        self.__solde = solde_initial           # Solde privé
        self.operations = []                   # Historique des opérations

        # Log de création du compte
        self._log("Creation du compte", solde_initial)

    def _log(self, type_op, montant):
        """Ajoute une operation horodatée au relevé."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operations.append(
            f"{timestamp} | {type_op} : {montant}€ | Solde = {self.__solde}€"
        )

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._log("Depot", montant)
        else:
            self._log("Echec depot (montant invalide)", montant)

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._log("Retrait", montant)
        else:
            self._log("Echec retrait (montant invalide)", montant)

    def get_solde(self):
        return self.__solde

    def afficher_releve(self):
        print(f"\n===== Releve du Compte {self.id} =====")
        for op in self.operations:
            print(op)
        print("====================================\n")


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []   # Liste de comptes (un client peut en avoir plusieurs)

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher(self):
        print(f"\n----- Client : {self.nom} -----")
        if not self.comptes:
            print("Aucun compte associe.")
            return
        for c in self.comptes:
            print(f"Compte {c.id} -> Solde : {c.get_solde()} €")
        print("--------------------------------\n")

    def afficher_releves(self):
        print(f"\n######## Releves de {self.nom} ########")
        for compte in self.comptes:
            compte.afficher_releve()
        print("########################################\n")



# Création d'un client
cli = Client("Yassir")

# Création de deux comptes
c1 = CompteBancaire(500)
c2 = CompteBancaire(1500)

# On ajoute les comptes au client
cli.ajouter_compte(c1)
cli.ajouter_compte(c2)

# Opérations sur les comptes
c1.deposer(300)
c1.retirer(50)

c2.retirer(200)
c2.deposer(1000)

# Affichage simple
cli.afficher()

# Affichage détaillé (relevés)
cli.afficher_releves()
