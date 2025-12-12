import sqlite3
from models.produit import Produit
from models.client import Client
from dao.dao_interface import DAOInterface

class SQLiteDAO(DAOInterface):

    def __init__(self, db_name="boutique.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.creer_tables()

    def creer_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS produit(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prix REAL
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS client(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                email TEXT UNIQUE
            )
        """)

    # ------------------- CRUD ----------------------

    def ajouter_produit(self, produit):
        self.conn.execute("INSERT INTO produit(nom, prix) VALUES (?, ?)",
                          (produit.nom, produit.prix))
        self.conn.commit()

    def ajouter_client(self, client):
        self.conn.execute("INSERT INTO client(nom, email) VALUES (?, ?)",
                          (client.nom, client.email))
        self.conn.commit()

    def lister_produits(self):
        cursor = self.conn.execute("SELECT * FROM produit")
        return [Produit(*row) for row in cursor]

    def lister_clients(self):
        cursor = self.conn.execute("SELECT * FROM client")
        return [Client(*row) for row in cursor]

    def rechercher_client_email(self, email):
        cursor = self.conn.execute("SELECT * FROM client WHERE email = ?", (email,))
        row = cursor.fetchone()
        return Client(*row) if row else None

    def modifier_prix_produit(self, id_produit, nouveau_prix):
        self.conn.execute("UPDATE produit SET prix=? WHERE id=?",
                          (nouveau_prix, id_produit))
        self.conn.commit()
