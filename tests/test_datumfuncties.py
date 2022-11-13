from datetime import date, timedelta
from unittest import TestCase

from datumfuncties import bereken_leeftijd


class Test(TestCase):
    vandaag = date.today()
    twintig_jaar_geleden = date.today().replace(year=vandaag.year - 20)

    def test_bereken_leeftijd_vandaag_jarig(self):
        geboortedatum = self.twintig_jaar_geleden
        self.assertEqual(20, bereken_leeftijd(geboortedatum))

    def test_bereken_leeftijd_gisteren_jarig(self):
        geboortedatum = self.twintig_jaar_geleden - timedelta(days=1)
        self.assertEqual(20, bereken_leeftijd(geboortedatum))

    def test_bereken_leeftijd_morgen_jarig(self):
        geboortedatum = self.twintig_jaar_geleden + timedelta(days=1)
        self.assertEqual(19, bereken_leeftijd(geboortedatum))

    def test_bereken_leeftijd_eind_vorige_maand_jarig(self):
        geboortedatum = self.twintig_jaar_geleden.replace(day=1) - timedelta(days=1)
        self.assertEqual(20, bereken_leeftijd(geboortedatum))
