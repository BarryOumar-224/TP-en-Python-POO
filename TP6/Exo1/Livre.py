from dataclasses import dataclass, asdict
import json
from functools import total_ordering

@total_ordering
@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit: float) -> "Livre":
        return Livre(self.titre, self.auteur, self.annee, prix_reduit)

    @staticmethod
    def from_json(json_str: str) -> "Livre":
        data = json.loads(json_str)
        return Livre(**data)

    def __lt__(self, other: "Livre") -> bool:
        if not isinstance(other, Livre):
            return NotImplemented
        return self.prix < other.prix

livre = Livre("1984", "George Orwell", 1949, 9.90)
print(livre.to_json())

livre_promo = livre.promo(7.99)
print(livre_promo.to_json())

json_data = livre.to_json()
livre2 = Livre.from_json(json_data)
print(livre2.to_json())

l1 = Livre("Livre A", "Auteur X", 2020, 10.0)
l2 = Livre("Livre B", "Auteur Y", 2020, 15.0)
print(l1 < l2)
print(l1 == l2)
