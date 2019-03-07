import os
import shutil
import csv
import os.path
import threading

class rout:
    numero = ""
    reseau = []
    interface = []
    tableRootage = ""
    mainDirectory = "/Users/"+os.getlogin()+"/Desktop/Routeur/"

    def __init__(self,numero,reseau):
        self.numero = numero
        self.reseau = reseau
        self.interface = []
        self.addInterface()
        self.tableRootage = self.mainDirectory + self.numero + ".csv"
        self.createRootageFile()
        self.writeRootage()


    def addInterface(self):
        i = 0
        while i < len(self.reseau):
            self.interface += [["I"+str(self.numero)+str(i+1),str(self.reseau[i])]]
            i += 1
    def createRootageFile(self):
        file = open(self.tableRootage, "w+")
        file.write("".join(self.tableRootage))
        file.close()

    def writeRootage(self):
        with open(self.tableRootage, 'w+', newline='') as csvfile:
            fieldnames = ['numeroReseau', 'metric','interface','nextHop']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            i = 0
            while i < len(self.reseau):
                writer.writerow({'numeroReseau': self.interface[i][1], 'metric': '0','interface': self.interface[i][0],'nextHop': '-'})
                i+= 1

    def writeinfo(self):
        for file in os.listdir(self.mainDirectory):
            if file[0:1] != ".":
                if self.mainDirectory+file != self.tableRootage:
                    with open(self.mainDirectory+file, 'a+', newline='') as oderFile:
                        fieldnames = ['numeroReseau', 'metric', 'interface', 'nextHop']
                        writer = csv.DictWriter(oderFile, fieldnames=fieldnames)
                        with open(self.tableRootage, 'r') as myFile:
                            spamreader = csv.DictReader(myFile)
                            for row in spamreader:
                                tabRow = [row['numeroReseau'], row['metric'], row['interface'], row['nextHop']]
                                writer.writerow({'numeroReseau': tabRow[0], 'metric': str(int(tabRow[1])+1), 'interface': tabRow[2],'nextHop': tabRow[3]})

    def work(self):
        threading.Timer(10, self.work).start()
        self.writeinfo()
        print("Routeur "+self.numero+" a envoyer ses infos")
