import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate= Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kassapaate), 100000)

    def test_edullinen_vahentaa_saldoa_oikein(self):
        maksu=1000
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(maksu),maksu-240)
        self.assertEqual(self.kassapaate.edulliset,2)

    def test_maukas_vahentaa_saldoa_oikein(self):
        maksu=1000
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(maksu),maksu-400)
        self.assertEqual(self.kassapaate.maukkaat,2)

    # def test_jos_maksu_ei_riita(self):
    #     maksu=1000
    #     self.kassapaate.syo_maukkaasti_kateisella(300)
    #     self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    #     self.assertEqual(self.kassapaate.maukkaat,0)

    def test_jos_maksu_ei_riita_maukas_käteinen(self): 
        maksu=10
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat,0)
        return 

    def test_jos_maksu_ei_riita_edullinen_käteinen(self):
        maksu=10
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        return 


    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille(self): #TÄÄ
        #summa=2500
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2500)
        self.assertEqual(self.maksukortti.saldo, 3500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102500)
        return True

    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self): #TÄÄ
        #summa=-1
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo,1000)
        return False

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
  
    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        maksu=1000
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ei_tarpeeks_rahaa_kortil_edulline(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 10)
        self.assertEqual(self.kassapaate.edulliset, 0)
        return False

    def test_ei_tarpeeks_rahaa_kortil_maukas(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 10)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        return False

    # def test_jos_raha_ei_riita_edulliseen(self):
    #     maksukortti = Maksukortti(10)
    #     self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        

    

    
        
    
    




    