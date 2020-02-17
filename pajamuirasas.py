import datetime
from irasas import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, id, suma, kategorijos, siuntejas, pap_info):
        Irasas.__init__(self, id, suma, kategorijos)
        self.siuntejas = siuntejas
        self.pap_info = pap_info
        self.tipas = 'Pajamos'
        self.data = datetime.datetime.now()
