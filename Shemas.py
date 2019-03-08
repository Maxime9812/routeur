from Architecture import *

class Shemas:
    ipgen = Architecture()
    shema1 = [["1", "2"]]

    shema2 = [["1", "3"], ["3", "2"]]

    shema3 = [["1", "2", "4"], ["2", "3", "5"], ["4", "5", "6", "7"]]

    shema4 = [["1", "2", "4"], ["2", "3", "6"], ["4", "5", "7"], ["8", "5", "6"]]

    shemaIp1 = ipgen.architecture("192.168.0.0/24", "300,25")
    shemaIp2 = ipgen.architecture("192.168.0.0/24","200,30,2")
    shemaIp3 = ipgen.architecture("192.168.0.0/24", "500,400,350,200,2,2,2")
    shemaIp4 = ipgen.architecture("192.168.0.0/24", "1000,700,300,80,2,2,2,2")