from PyQt5 import uic, QtWidgets, QtGui
from time import sleep
from MIPS_SIMULATOR import MIPS_SIMULATOR
from threading import Thread

app = QtWidgets.QApplication([])
interface = uic.loadUi("InterfaceGrafica//MainInterface.ui")

Simulator = None
Simulator = MIPS_SIMULATOR(interface)

def LoadSimulator():
    global Simulator
    global interface

    ark = QtWidgets.QFileDialog.getOpenFileName()[0]

    Simulator.load(ark)
    AttTable()

def msgBox(msgTxt):
    msg = QtWidgets.QMessageBox()
    msg.setText(msgTxt)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setWindowTitle("Opps!")

    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

    msg.exec_()

def check():

    if(Simulator == None):
        msgBox("Você precisa escolher um arquivo!")
        return False

    return True

def AttTable(ExecutionState = 0):
    check()


    row = 0
    for r in Simulator.REGISTERS.registers:
        interface.RegisterTable.setRowHeight(row,19)
        interface.RegisterTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(r)))
        interface.RegisterTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(Simulator.REGISTERS.registers[r])))
        row += 1

    row = 0
    for line in Simulator.AssemblyCode:
        interface.AssemblyCodeTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(line)))
        row += 1

    if(Simulator.pc >= 4194304 and Simulator.pc <= Simulator.EOF):

        line = int((Simulator.pc - 4194304)/4)
        interface.AssemblyCodeTable.selectRow(line)
        if(ExecutionState!='Erro1'):
            interface.AssemblyCodeTable.item(line,0).setBackground(QtGui.QColor(120, 230, 120))
        else:
            interface.AssemblyCodeTable.item(line,0).setBackground(QtGui.QColor(230, 120, 120))
            msgBox(f"Falha na execução da instrução {line+1}\nSimulação resetada!")
            Simulator.ResetAllSteps()

def AllStepsNext():
    if(check()):

        Simulator.ResetAllSteps()
        i = 0
        run = True
        while(Simulator.pc != Simulator.EOF and run):
            Simulator.RunOneStep()
            AttTable()
            i += 1
            if(i > 5000):
                msgBox("Possivel Loop infinito, a execução foi interrompida!")
                run = False
                Simulator.ResetAllSteps()
                AttTable()

def AllStepsBack():
    if(check()):
        Simulator.ResetAllSteps()
        AttTable()

def OneStepNext():
    if(check()):
        ExecutionState = Simulator.RunOneStep()
        AttTable(ExecutionState)

def OneStepBack():
    if(check()):
        Simulator.ResetOneStep()
        AttTable()

AttTable()
interface.btn_OpenFile.clicked.connect(LoadSimulator)
interface.btn_AllStepsNext.clicked.connect(AllStepsNext)
interface.btn_AllStepsBack.clicked.connect(AllStepsBack)
interface.btn_OneStepNext.clicked.connect(OneStepNext)
interface.btn_OneStepBack.clicked.connect(OneStepBack)

interface.show()
app.exec()
