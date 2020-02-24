import datetime
from irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, id, suma, kategorijos, atsiskaitymo_budas, isigyta_preke_paslauga):
        Irasas.__init__(self, id, suma, kategorijos)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.tipas = 'Išlaidos'
        self.data = datetime.datetime.now()
