from datetime import datetime
from contextlib import ExitStack
import os

class ConnectionManager:
    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"[{datetime.now()}] Connexion a {self.service_name} etablie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[{datetime.now()}] Deconnexion de {self.service_name}.")
        if exc_type:
            print(f"Erreur detectee : {exc_type.__name__} -- {exc_value}")

if __name__ == "__main__":
    print("Debut Partie 2")
    with ExitStack() as stack:
        log = stack.enter_context(open("log.txt", "a"))
        conn = stack.enter_context(ConnectionManager("Serveur X"))
        log.write(f"[{datetime.now()}] Tache effectuee sur {conn.service_name}\n")
    print("Fin Partie 2")

    print("Debut Partie 3")
    try:
        with ExitStack() as stack:
            log = stack.enter_context(open("log.txt", "a"))
            conn = stack.enter_context(ConnectionManager("Base Y"))
            print("Provocation de l'erreur...")
            raise RuntimeError("Erreur de traitement")
    except RuntimeError:
        print("Exception capturee dans le bloc principal")
    print("Fin Partie 3")

    if os.path.exists("log.txt"):
        os.remove("log.txt")
    print("Nettoyage termine")