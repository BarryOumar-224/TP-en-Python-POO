import unittest
from paiements import CarteBancaire, PayPal, Crypto

class TestPaiements(unittest.TestCase):

    def test_carte(self):
        p = CarteBancaire(50, "4532756279624064", "123")
        self.assertIn("Carte Bancaire", p.payer())
        self.assertIn("50", p.payer())

    def test_paypal(self):
        p = PayPal(20, "ex@mail.com", "tok")
        self.assertIn("PayPal", p.payer())
        self.assertIn("20", p.payer())

    def test_crypto(self):
        p = Crypto(99, "wallet", "ETH")
        self.assertIn("Crypto", p.payer())
        self.assertIn("ETH", p.payer())

if __name__ == "__main__":
    unittest.main()
