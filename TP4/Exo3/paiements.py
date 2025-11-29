from abc import ABC, abstractmethod

class Paiement(ABC):
    def __init__(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

    def _verifier_luhn(self, numero):
        total = 0
        inv = numero[::-1]
        for i, c in enumerate(inv):
            n = int(c)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if not numero.isdigit() or not self._verifier_luhn(numero):
            raise ValueError("Numéro de carte invalide.")
        if not (cvv.isdigit() and len(cvv) == 3):
            raise ValueError("CVV invalide.")
        self._numero = numero
        self._cvv = cvv

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ par Carte Bancaire."


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ via PayPal."


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ en Crypto ({self._reseau})."


def traiter_paiements(liste):
    for p in liste:
        print(p.payer())


if __name__ == "__main__":
    paiements = [
        CarteBancaire(50, "4532756279624064", "123"),
        CarteBancaire(19.99, "4716258050959788", "456"),
        PayPal(12.5, "test@example.com", "tok123"),
        PayPal(75, "client@mail.com", "abc987"),
        Crypto(100, "0x123abc", "ETH"),
        Crypto(250, "1BvBMSEYstWetq...", "BTC")
    ]

    traiter_paiements(paiements)
