from datetime import date, datetime
from pony.orm import PrimaryKey, Required, Set, db_session

from database import db


class Persoon(db.Entity):
    """
    Deze klasse legt een Persoon in de database vast met naam, geboortedatum en een aantal cadeaus.
    """
    id = PrimaryKey(int, auto=True)
    naam = Required(str)
    geboortedatum = Required(date)
    cadeaus = Set(lambda: db.Cadeau, cascade_delete=True)

    @db_session
    def geef_cadeau(self, aanleiding: str, omschrijving: str) -> int:
        """
        Voegt een cadeau toe aan een persoon.

        :param aanleiding: Aanleiding
        :param omschrijving: Omschrijving van het cadeau.
        :return: Cadeau-object
        """
        datum = datetime.today()
        return db.Cadeau(persoon=self, aanleiding=aanleiding, omschrijving=omschrijving, datum=datum)


