class Architecture:
    def calculator(self,ip,choix):
        ip = ip.split(".")
        ip = ip[:-1] + ip[len(ip) - 1].split("/")
        masque = int(ip[-1])
        ip.remove(ip[-1])

        str = ""
        for number in ip:
            str += bin(int(number))[2:].zfill(8)

        strMasque = str[masque:]
        strIp = str[:masque]

        adr = self.replace(strIp, len(strMasque), choix)
        adrArray = self.createArray(adr)

        return self.ipToSting(adrArray)

    def getMasque(self,str):
        return int(str.split("/")[1])

    def nbToMasque(self,str):
        i = 2
        nb = 31
        while i <= int(str):
            i *= 2
            nb -= 1
        return nb

    def ipToSting(self,array):
        newString = ""
        for num in array:
            newString += num.__str__() + "."

        return newString[:-1]

    def replace(self,str, lenNumber, newStr):
        i = 0
        while i < lenNumber:
            str += newStr
            i += 1
        return str

    def createArray(self,str):
        array = []
        i = 0
        while i < len(str) / 8:
            if (i == 0):
                array.insert(i, int(str[0:8], 2))
            else:
                array.insert(i, int(str[8 * i:8 * (i + 1)], 2))
            i += 1
        return array

    def nbEquipement(self,masque):
        nb = 0
        i = 0
        while i < 32 - masque:
            if i == 0:
                nb = 2
            else:
                nb *= 2
            i += 1
        return nb - 2

    def getNextAdr(self,str):
        adrArray = str.split(".")
        i = 3
        while i >= 0:
            if int(adrArray[i]) == 255:
                adrArray[i] = "0"
            else:
                adrArray[i] = int(adrArray[i]) + 1
                return self.ipToSting(adrArray)
            i -= 1

    def architecture(self,ipStart,array):
        ipArray = array.split(",")
        architectureIp = []

        i = 0
        lastIp = self.calculator(ipStart, "0")
        while i < len(ipArray):
            ipToCalculate = self.getNextAdr(lastIp) + "/" + self.nbToMasque(ipArray[i]).__str__()
            architectureIp += [[self.calculator(ipToCalculate, "0"), self.calculator(ipToCalculate, "1")]]
            lastIp = self.calculator(ipToCalculate, "1")
            i += 1
        return architectureIp
