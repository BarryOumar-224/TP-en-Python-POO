class CsvException(Exception):
    def __init__(self, message):
        super().__init__(message)

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    # À compléter : lecture du CSV, vérifications, levée d'exceptions
    pass
