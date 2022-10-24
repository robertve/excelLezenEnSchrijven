from datetime import date, datetime

from pony.orm import Database, PrimaryKey, Required, Set, db_session

from database.cadeau import Cadeau

db = Database()


class Persoon(db.Entity):
    id = PrimaryKey(int, auto=True)
    naam = Required(str)
    geboortedatum = Required(date)
    cadeaus = Set(Cadeau)

    def __init__(self, naam, geboortedatum):
        naam = naam
        geboortedatum = geboortedatum

    def geef_cadeau(self, aanleiding: str, omschrijving: str) -> Cadeau:
        datum = datetime.today()
        cadeau = Cadeau(ontvanger=self, aanleiding=aanleiding, omschrijving=omschrijving, datum=datum)
        return cadeau
