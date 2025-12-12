class Client:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Client(id={self.id}, nom='{self.nom}', email='{self.email}')"
