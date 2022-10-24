from pony.orm import Database, db_session, commit

from database.persoon import Persoon
from database.cadeau import Cadeau
from datumfuncties import vandaag
from familielid import Familielid


def geef_chocoladeletters(familie: list):
    db = Database()
    db.bind(provider='sqlite', filename=':memory:', create_db=True)
    db.generate_mapping(create_tables=True)

    for familielid in familie:
        if isinstance(familielid, Familielid):
            persoon = Persoon(naam=familielid.naam, geboortedatum=familielid.geboortedatum)
            cadeau_idee = 'chocoladeletter ' + familielid.naam[:1].upper()
            aanleiding = 'Sinterklaas'
            cadeau = Cadeau(aanleiding=aanleiding, omschrijving=cadeau_idee, datum=vandaag())

    commit()
