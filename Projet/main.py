from models.produit import Produit
from models.client import Client
from dao.sqlite_dao import SQLiteDAO
from dao.mysql_dao import MySQLDAO

def choisir_sgbd():
    print("1 - SQLite")
    print("2 - MySQL")
    choix = input("Choisissez le SGBD : ")
    return SQLiteDAO() if choix == "1" else MySQLDAO()

def menu(dao):
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter produit")
        print("2. Ajouter client")
        print("3. Lister produits")
        print("4. Lister clients")
        print("5. Rechercher client par email")
        print("6. Modifier prix produit")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom produit : ")
            prix = float(input("Prix : "))
            dao.ajouter_produit(Produit(None, nom, prix))

        elif choix == "2":
            nom = input("Nom client : ")
            email = input("Email : ")
            dao.ajouter_client(Client(None, nom, email))

        elif choix == "3":
            for p in dao.lister_produits():
                print(p)

        elif choix == "4":
            for c in dao.lister_clients():
                print(c)

        elif choix == "5":
            email = input("Email client : ")
            client = dao.rechercher_client_email(email)
            print(client if client else "Client introuvable.")

        elif choix == "6":
            idp = int(input("ID produit : "))
            prix = float(input("Nouveau prix : "))
            dao.modifier_prix_produit(idp, prix)

        elif choix == "0":
            break

if __name__ == "__main__":
    dao = choisir_sgbd()
    menu(dao)
