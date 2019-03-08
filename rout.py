import os
import shutil
import csv
import os.path
import threading

class rout:
    numero = ""
    reseaux = []
    interface = []
    tableRootage = ""
    mainDirectory = "/Users/"+os.getlogin()+"/Desktop/Routeur/"
    tabTest = []
    ipInterface = []
    working = True

    def __init__(self,numero,reseaux):
        self.numero = numero
        self.reseaux = reseaux
        print (self.numero)
        self.interface = []
        self.ipInterface = []
        str = ""
        for res in self.reseaux:
            res.nbConnect+=1
            self.ipInterface.append(res.ipReseau)
            str += res.numero
        self.tableRootage = self.mainDirectory + self.numero +str+".csv"
        self.addInterface()
        self.createRootageFile()
        self.writeRootage()
        self.tabTest = []
        self.working = True

    def addInterface(self):
        i = 0
        y = 0
        while i < len(self.reseaux):
            self.interface += [["i"+str(self.numero)+str(i+1),str(self.reseaux[i].numero)]]
            i += 1
        while y < len(self.ipInterface):
            self.interface[y] += self.ipInterface[y].split(".")
            self.interface[y][5] = str(int(self.interface[y][5])+self.reseaux[y].nbConnect)
            y+=1
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
            while i < len(self.reseaux):
                writer.writerow({'numeroReseau': self.interface[i][1], 'metric': '0','interface': self.interface[i][0],'nextHop': '-'})
                i+= 1

    def isOnSameReseau(self,file):
        fileReseau = list(file[1:-4])
        for res in fileReseau:
            for myRes in self.reseaux:
                if res == myRes.numero:
                    return True
        return False
        print(fileReseau)
    def writeinfo(self):
        for file in os.listdir(self.mainDirectory):
            if file[0:1] != ".":
                if  self.isOnSameReseau(file):
                    if self.mainDirectory+file != self.tableRootage:
                        with open(self.tableRootage, 'r', newline='') as myFile:
                            fieldnames = ['numeroReseau', 'metric', 'interface', 'nextHop']
                            myReader = csv.DictReader(myFile, fieldnames=fieldnames)
                            with open(self.mainDirectory+file, 'a+') as otherFileAppend:
                                writer = csv.DictWriter(otherFileAppend, fieldnames=fieldnames)
                                find = True
                                for myRow in myReader:
                                    print(myRow)
                                    print("my row")
                                    find = False
                                    with open(self.mainDirectory + file, 'r') as otherFile:
                                        reader = csv.DictReader(otherFile, fieldnames=fieldnames)
                                        for row in reader:
                                            print(row)
                                            print("other row")
                                            if row['numeroReseau'] == myRow['numeroReseau']:
                                                find = True
                                                break
                                        print(find)
                                        if find == False:
                                            #print("add")
                                            tabRow = [myRow['numeroReseau'], myRow['metric'], myRow['interface'], myRow['nextHop']]
                                            self.tabTest.append(tabRow)
                                            #print(self.tabTest)
                                            #print(self.numero)
                                        else:
                                            #print("dont")
                                            continue
                                for row in self.tabTest:
                                    writer.writerow({'numeroReseau': row[0], 'metric': str(int(row[1]) + 1),
                                                     'interface': row[2], 'nextHop': self.numero})
                                    print(row)
                                self.tabTest.clear()
                                print("stoper")


    def work(self):
        if self.working == True:
            global work
            work = threading.Timer(30, self.work).start()
            self.writeinfo()
            print("Routeur "+self.numero+" a envoyer ses infos")

    def getInfo(self):
        info = []
        with open(self.tableRootage, 'r') as myFileRead:
            fieldnames = ['numeroReseau', 'metric', 'interface', 'nextHop']
            myRead = csv.DictReader(myFileRead, fieldnames=fieldnames)
            i = 0
            for row in myRead:
                if row['numeroReseau'] != "numeroReseau":
                    info += [str(i)+" | NumeroReseau : "+row['numeroReseau']+" | Metric : "+row['metric']+" | Interface : "+row['interface']+" | NextHop : "+row['nextHop']]
                i+=1
            return info
    def getIpInterface(self):
        tab = []
        for interface in self.interface:
            i = 2
            tab2 = []
            while i < len(self.interface[0]):
                tab2 += [interface[i]]
                i+=1
            tab.append(tab2)
        return tab
