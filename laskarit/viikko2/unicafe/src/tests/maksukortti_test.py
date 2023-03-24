import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
        return True
 

    # def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
    #     self.kortti.syo_maukkaasti()

    #     self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_ei_vie_saldoa_negatiiviseksi(self):

        self.maksukortti.ota_rahaa(10000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        return False


    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    # def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
    #     self.maksukortti.lataa_rahaa(20000)

    #     self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 150.00 euroa")

    # def test_maukkaan_luonaan_syominen_ei_vie_saldoa_negatiiviseksi(self):
    #     kortti = Maksukortti(200)
    #     kortti.syo_maukkaasti()

    #     self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
 

    # def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
    #     self.maksukortti.lataa_rahaa(-20000)
    #     self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
 

    # def test_edullinen_lounas_jos(self):
    #     kortti = Maksukortti(250)
    #     kortti.syo_edullisesti()
    #     self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
        
    # def test_edullinen_lounas_jos(self):
    #     kortti = Maksukortti(400)
    #     kortti.syo_maukkaasti()
    #     self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")



