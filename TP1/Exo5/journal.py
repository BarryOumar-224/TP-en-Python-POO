from datetime import datetime

class JournalTaches:
    def __enter__(self):
        # Ouvre le fichier journal.txt en mode ajout (append)
        self._f = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        timestamp = datetime.now().isoformat()
        self._f.write(f"{timestamp} - {tache}\n")

    def __exit__(self, exc_type, exc, tb):
        self._f.close()

    @classmethod
    def lire(cls):
        """Affiche l’historique en ordre inverse (dernières lignes en premier)."""
        try:
            with open("journal.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
            for ligne in reversed(lignes):
                print(ligne.strip())
        except FileNotFoundError:
            print("Aucun journal trouvé.")
