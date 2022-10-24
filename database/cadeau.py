from datetime import date

from pony.orm import PrimaryKey, Required, Database

db = Database()


class Cadeau(db.Entity):
    id = PrimaryKey(int, auto=True)
    aanleiding = Required(str)
    omschrijving = Required(str)
    datum = Required(date)
    # ontvanger = Required(Persoon)

    def __init__(self, aanleiding: str, omschrijving: str, datum: date):
        # self.ontvanger = ontvanger
        aanleiding = aanleiding
        omschrijving = omschrijving
        datum = datum
