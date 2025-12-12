from csv_reader import (
    charger_csv,
    CsvException,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)

def main():
    try:
        articles = charger_csv("Groceries_dataset IA.csv")
    except FichierIntrouvableException as e:
        print("Erreur :", e)
    except LigneInvalideException as e:
        print("Erreur :", e)
    except PrixNegatifException as e:
        print("Erreur :", e)
    except CsvException as e:
        print("Erreur :", e)

if __name__ == "__main__":
    main()
