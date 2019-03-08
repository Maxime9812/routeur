class Reseau:
    numero = ""
    nbConnect = 0
    ipReseau = ""
    ipDifusion = ""

    def __init__(self,numero,ip):
        self.numero = str(numero)
        self.nbConnect = 0
        self.ipReseau = ip[0]
        self.ipDifusion = ip[1]