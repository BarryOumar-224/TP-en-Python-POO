import mysql.connector
from models.produit import Produit
from models.client import Client
from dao.dao_interface import DAOInterface

class MySQLDAO(DAOInterface):

    def __init__(self, host="localhost", user="root", password="", database="boutique"):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()
        self.creer_tables()

    def creer_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produit(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nom VARCHAR(100),
                prix FLOAT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS client(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nom VARCHAR(100),
                email VARCHAR(100) UNIQUE
            )
        """)

    # ------------------------- CRUD ------------------------

    def ajouter_produit(self, produit):
        self.cursor.execute("INSERT INTO produit(nom, prix) VALUES (%s, %s)",
                            (produit.nom, produit.prix))
        self.conn.commit()

    def ajouter_client(self, client):
        self.cursor.execute("INSERT INTO client(nom, email) VALUES (%s, %s)",
                            (client.nom, client.email))
        self.conn.commit()

    def lister_produits(self):
        self.cursor.execute("SELECT * FROM produit")
        return [Produit(*row) for row in self.cursor.fetchall()]

    def lister_clients(self):
        self.cursor.execute("SELECT * FROM client")
        return [Client(*row) for row in self.cursor.fetchall()]

    def rechercher_client_email(self, email):
        self.cursor.execute("SELECT * FROM client WHERE email=%s", (email,))
        row = self.cursor.fetchone()
        return Client(*row) if row else None

    def modifier_prix_produit(self, id_produit, nouveau_prix):
        self.cursor.execute("UPDATE produit SET prix=%s WHERE id=%s",
                            (nouveau_prix, id_produit))
        self.conn.commit()
