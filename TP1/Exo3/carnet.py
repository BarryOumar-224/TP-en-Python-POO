from contact import Contact

class Carnet:
    def __init__(self):
        self._contacts = []

    def ajouter(self, contact: Contact):
        self._contacts.append(contact)

    def recherche(self, fragment: str):
        fragment = fragment.lower()
        return [c for c in self._contacts if fragment in c.nom.lower()]

    def afficher_tous(self):
        for c in self._contacts:
            print(f"{c.nom} - {c.telephone} - {c.email}")

    @property
    def nombre_contacts(self):
        return len(self._contacts)
