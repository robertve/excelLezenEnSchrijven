from datetime import date

from pony.orm import PrimaryKey, Required

from database import db


class Cadeau(db.Entity):
    """
    Deze klasse legt een Cadeau in de database vast met persoon (de ontvanger), de aanleiding, een omschrijving en
    een datum.
    """
    id = PrimaryKey(int, auto=True)
    aanleiding = Required(str)
    omschrijving = Required(str)
    datum = Required(date)
    persoon = Required(db.Persoon)
