from datetime import date


def bereken_leeftijd(geboortedatum: date):
    """
    Berekent de leeftijd op basis van een geboortedatum.

    @:param geboortedatum Geboortedatum
    :return: Leeftijd (in jaren)
    """
    referentiedatum = vandaag()
    return referentiedatum.year - geboortedatum.year - (
            (referentiedatum.month, referentiedatum.day) < (geboortedatum.month, geboortedatum.day))


def vandaag():
    return date.today()
