import fileinput
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import time
import subprocess, shlex, re

class CommunicationAspThread(QThread):
    newObservation_signal = pyqtSignal(str, bool)
    def __init__(self):
        super().__init__()
        self.state = False
        self.stepDuration = 0.5 # duration between two step (secondes)
        self.lastTime = time.time()
        self.stepCounter = 0
        self.currentObsDict = {}
        self.aspFilePath = 'test_communication.sparc'

        self.newObservation_signal.connect(self.newObservation)
    
    def setState(self, b:bool):
        self.stepCounter = 0
        self.state = b
    
    def run(self):
        while True:
            if self.state:
                if time.time() - self.lastTime > self.stepDuration:
                    self.updateObservation()
                    self.updateOrder()

                    self.stepCounter += 1
                    self.currentObsDict = {}
                    self.lastTime = time.time()
    
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

        print('New observation updated:\n' + newObsStr)

    def updateOrder(self):
        self.orderCommand = 'java -jar sparc.jar restaurant_test2.sparc -A -n 1'
        self.orderKeyword = 'occurs'
        self.orderTransmit = []
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
            print('New orders received:')
            print(self.orderTransmit)

        except : print("The program is inconsistent (SPARC).")


    @pyqtSlot(str, bool)
    def newObservation(self, name:str, state:bool):
        self.currentObsDict[name] = state


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
            aspThread.newObservation_signal.emit(str(lastTime), True)

    sys.exit(app.exec_())