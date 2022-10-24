import datumfuncties


class Familielid:
    """
    Deze klasse legt een familielid vast met voornaam, familieverband en geboortedatum.
    Deze kan worden uitgebreid met een functie om te bepalen of iemand bijna jarig is.
    """

    familieverband = ''
    naam = ''
    geboortedatum = None

    def __init__(self, naam, familieverband, geboortedatum):
        """
        Constructor bestaande uit een voornaam, een familieverband en een geboortedatum.

        :param naam: Voornaam
        :param familieverband: Familieverband (vader, moeder, etc.)
        :param geboortedatum: Geboortedatum
        """
        self.naam = naam
        self.familieverband = familieverband.lower()
        self.geboortedatum = geboortedatum

    def __str__(self) -> str:
        return "een " + self.familieverband + " " + self.naam + " van " + str(self.leeftijd())

    def leeftijd(self) -> int:
        """
        Berekent de leeftijd.

        :return: Leeftijd in jaren
        """
        return datumfuncties.bereken_leeftijd(self.geboortedatum)
