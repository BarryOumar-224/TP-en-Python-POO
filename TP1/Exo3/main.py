from carnet import Carnet
from contact import Contact

c = Carnet()
c.ajouter(Contact("Amina Saidi", "0612345678", "amina@example.com"))
c.ajouter(Contact("Youssef Belkhou", "0699988877", "youssef@example.com"))
c.ajouter(Contact("Said Toumi", "0677001122", "said@example.com"))

resultat = c.recherche("sa")
for contact in resultat:
    print(contact.nom, contact.telephone)

print("Nombre total :", c.nombre_contacts)
