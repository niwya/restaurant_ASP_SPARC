import fileinput
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import time
import subprocess, shlex, re

class CommunicationAspThread(QThread):
    newObservation_signal = pyqtSignal(str, bool)
    newOrder_signal = pyqtSignal(str, int)
    def __init__(self):
        super().__init__()

        self.state = False
        self.stepDuration = 0.5 # duration between two step (secondes)
        self.lastTime = time.time()
        self.stepCounter = 0
        self.currentObsDict = {}
        self.currentOrdDict = {}
        self.aspFilePath = 'restaurant_test2.sparc'

        self.newObservation_signal.connect(self.newObservation)
    
    def setState(self, b:bool):
        self.stepCounter = 0
        self.state = b
    
    def run(self):
        while True:
            if self.state:
                if time.time() - self.lastTime > self.stepDuration:
                    self.currentOrdDict = {}
                    self.updateObservation()
                    self.updateOrder()

                    self.stepCounter += 1
                    self.currentObsDict = {}
                    self.lastTime = time.time()
                    print(self.getOrders())
    
    def updateObservation(self):
        newObsStr = ''
        for obs in self.currentObsDict.keys():
            newObsStr += 'obs(' + obs + ','
            newObsStr += 'true' if self.currentObsDict[obs] else 'false'
            newObsStr += ',' + str(self.stepCounter) + ').\n'
        
        for line in fileinput.FileInput(self.aspFilePath,inplace=1):
            if "%e_obs" in line:
                line=line.replace(line, newObsStr + line)
            print(line,end='')

    def updateOrder(self):
        ## Command line to retrieve only 1 answer set ##
        self.orderCommand = 'java -jar sparc.jar restaurant_test2.sparc -A -n 1'
        ## Filtering keyword to only retrieve actions to perform ##
        self.orderKeyword = 'occurs'

        self.orderTransmit = []

        ## Formatting, running the command and retrieving, formatting the output ##
        args = shlex.split(self.orderCommand)
        output = subprocess.check_output(args)
        output = str(output)
        outputList = re.findall('\{(.*?)\}', output)
        outputList = outputList[0].split(' ')

        orderList = []

        try : 
            for i in range(len(outputList)):
                if 'occurs' in outputList[i] and not '-occurs' in outputList[i]:
                    if outputList[i][-1]==',': 
                        outputList[i]=outputList[i][:-1]
                    orderList.append(outputList[i])
            if orderList != self.orderTransmit: self.orderTransmit = orderList
            #print('New orders received:')
            #print(self.orderTransmit)

            n = len(self.orderTransmit)
            if n==0 : self.newOrder_signal.emit('', 0)
            else:
                orderList_formatted = [['', '']]*n

                for i in range(n):
                    temp = self.orderTransmit[i][7:-1]
                    matches = re.finditer(r"(?:[^\,](?!(\,)))+$", temp)
                    for matchNum, match in enumerate(matches, start=1):
                        orderList_formatted[i][0] = temp[:match.start()-1]
                        orderList_formatted[i][1] = match.group()
                
                for i in range(n):
                    self.currentOrdDict[orderList_formatted[i][0]] = int(orderList_formatted[i][1])
                    #print(orderList_formatted[i][1])
                    #self.newOrder_signal.emit(orderList_formatted[i][0], int(orderList_formatted[i][1]))

        except : print("The SPARC program is inconsistent.")

    @pyqtSlot(str, bool)
    def newObservation(self, name:str, state:bool):
        self.currentObsDict[name] = state
    
    def getOrders(self):
        return self.currentOrdDict


if __name__ == "__main__":

    import sys
    from PyQt5 import QtWidgets as Qtw
    app = Qtw.QApplication(sys.argv)
    aspThread = CommunicationAspThread()
    aspThread.setState(True)
    aspThread.start()
    lastTime = time.time()

    while(True):
        if time.time() - lastTime > 0.3:
            lastTime = time.time()
            aspThread.newObservation_signal.emit("bill_wave(c1)", True)

    sys.exit(app.exec_())