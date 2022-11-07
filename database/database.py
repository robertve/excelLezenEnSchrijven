from pony.orm import commit
from pony.orm import db_session

from familielid import Familielid
from .base import db
from .settings import db_params


@db_session
def geef_chocoladeletters(familie: list):
    """
    Leg een lijst met personen vast en geef iedereen een chocoladeletter van zijn voorletter.

    :param familie: Lijst met personen.
    :return: Niets
    """
    for familielid in familie:
        if isinstance(familielid, Familielid):
            persoon = db.Persoon(naam=familielid.naam, geboortedatum=familielid.geboortedatum)
            cadeau_idee = 'chocoladeletter ' + familielid.naam[:1].upper()
            aanleiding = 'Sinterklaas'
            cadeau = persoon.geef_cadeau(aanleiding=aanleiding, omschrijving=cadeau_idee)
    commit()


def open_database():
    db.bind(**db_params)
    db.generate_mapping(create_tables=True)
