from Registers_Core.Registers import Registers
from Memory.Memory import Memory
from Instructions_Controller_Core.Instruction_Controller import Execute_Instruction
#http://mipsconverter.com/opcodes.html
class MIPS_SIMULATOR:

    def __init__(self,interface):
        self.REGISTERS         = Registers()
        self.DataMemory        = Memory()

        keys = [x for x in range(4194304,5194304,4)]
        self.InstructionMemory = dict(zip(keys,[0]*len(keys)))

        self.Execute_Instruction = None

        self.pc = 4194304
        self.EOF = 0
        self.AssemblyCode = []
        self.history = []
        self.interface = interface

    def RunAllSteps(self,EOE):
        self.ResetAllSteps()
        while(self.pc != EOE):
            self.RunOneStep()

    def syscall_execute(self,call):

        if(call==None):
            return 0

        if(call==1):#print int
            a0 = self.REGISTERS.getRegister(4) #4 = codigo de $a0
            try:
                text = self.interface.Console.toPlainText()+'\n'
            except:
                text=''
            self.interface.Console.setText(f"{text}{str(a0)}") #printa $a0

        if(call==10):
            try:
                text = self.interface.Console.toPlainText()+'\n'
            except:
                text=''
            self.interface.Console.setText(f'{text}syscall exit.') #printa $a0
            self.pc = self.EOF

        self.Execute_Instruction.Logic_Aritmetic_Core.call = None

    def RunOneStep(self):

        if(self.pc<self.EOF):

            self.pc = self.REGISTERS.getRegister('pc')
            self.history.append(self.pc)
            self.REGISTERS.setRegister('pc',self.pc+4)
            try:
                self.Execute_Instruction = Execute_Instruction(self.InstructionMemory[self.pc],self.DataMemory,self.REGISTERS)
                self.syscall_execute(self.Execute_Instruction.Logic_Aritmetic_Core.call)
            except TypeError as E:
                print("\nCódigo Finalizado!")
            except Exception as E:
                print(E)
                return 'Erro1'

    def ResetOneStep(self):

        if(len(self.history) > 1):
            self.history.pop(-1)
            history = self.history.copy()
            pc = history[-1]
            self.ResetAllSteps()
            self.RunAllSteps(pc)
            self.history = history

    def ResetAllSteps(self):

        self.interface.Console.setText('')
        self.REGISTERS         = Registers()
        self.DataMemory        = Memory()
        self.pc = 4194304

    def load(self,ark):
        i = 4194304

        for instruction in open(ark,'r'):
            if(instruction[0] != '\t' and instruction[0] != '\n' and instruction[0] != ' '):
                self.InstructionMemory[i] = instruction[0:32]
                self.AssemblyCode.append(instruction[33:-1])
                i += 4

        self.EOF = i-4
