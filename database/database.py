from datetime import date, datetime

from pony.orm import Database, PrimaryKey, Required, Set, db_session
from pony.orm import commit

from datumfuncties import vandaag
from familielid import Familielid

db = Database()


class Persoon(db.Entity):
    """
    Deze klasse legt een Persoon in de database vast met naam, geboortedatum en een aantal cadeaus.
    """
    id = PrimaryKey(int, auto=True)
    naam = Required(str)
    geboortedatum = Required(date)
    cadeaus = Set(lambda: Cadeau, cascade_delete=True)

    @db_session
    def __init__(self, naam, geboortedatum):
        """
        Constructor bestaande uit een naam en een geboortedatum.

        :param naam: Volledige naam
        :param geboortedatum: Geboortedatum
        """
        naam = naam
        geboortedatum = geboortedatum

    @db_session
    def geef_cadeau(self, aanleiding: str, omschrijving: str) -> int:
        """
        Voegt een cadeau toe aan een persoon.

        :param aanleiding: Aanleiding
        :param omschrijving: Omschrijving van het cadeau.
        :return: Cadeau-object
        """
        datum = datetime.today()
        return Cadeau(ontvanger=self, aanleiding=aanleiding, omschrijving=omschrijving, datum=datum)


class Cadeau(db.Entity):
    id = PrimaryKey(int, auto=True)
    aanleiding = Required(str)
    omschrijving = Required(str)
    datum = Required(date)
    persoon = Required(Persoon)

    @db_session
    def __init__(self, aanleiding: str, omschrijving: str, datum: date):
        # self.ontvanger = ontvanger
        aanleiding = aanleiding
        omschrijving = omschrijving
        datum = datum


@db_session
def geef_chocoladeletters(familie: list):
    """
    Leg een lijst met personen vast en geef iedereen een chocoladeletter van zijn voorletter.

    :param familie: Lijst met personen.
    :return: Niets
    """
    for familielid in familie:
        if isinstance(familielid, Familielid):
            persoon = Persoon(naam=familielid.naam, geboortedatum=familielid.geboortedatum)
            cadeau_idee = 'chocoladeletter ' + familielid.naam[:1].upper()
            aanleiding = 'Sinterklaas'
            cadeau = Cadeau(aanleiding=aanleiding, omschrijving=cadeau_idee, datum=vandaag())
    commit()


def open_database():
    db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='postgres')
    db.generate_mapping(create_tables=True)
