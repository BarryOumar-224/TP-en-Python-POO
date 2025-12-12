from dataclasses import dataclass, asdict
import json
from functools import total_ordering

@total_ordering
@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self) -> bool:
        return self.annee < 2000

    @staticmethod
    def from_json(json_str: str) -> "Film":
        data = json.loads(json_str)
        return Film(**data)

    def __lt__(self, other: "Film") -> bool:
        if not isinstance(other, Film):
            return NotImplemented
        return self.note < other.note

# Exemple d’utilisation
film1 = Film("Le Fabuleux Destin d'Amélie Poulain", "Jean-Pierre Jeunet", 2001, 8.6)
film2 = Film("Titanic", "James Cameron", 1997, 7.8)
film3 = Film("Inception", "Christopher Nolan", 2010, 8.8)

print(film1.to_json())
print(film2.est_classique())
print(film3 < film1)

# Liste de favoris et sérialisation multiple
favoris = [film1, film2, film3]
favoris_json = json.dumps([asdict(f) for f in favoris], ensure_ascii=False)
print(favoris_json)

# Chargement depuis JSON
loaded_films = [Film.from_json(json.dumps(f)) for f in [asdict(f) for f in favoris]]
for f in loaded_films:
    print(f.to_json())
