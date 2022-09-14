from Aritmetic_Core.BinaryConversor import BinaryConversor

class Logic_Aritmetic_Core:

    def __init__(self,DataMemory,registers):
        self.REGISTERS = registers
        self.DataMemory = DataMemory
        self.call = None

    def add(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])
        self.REGISTERS.setRegister(instruction['rd'],r1+r2)

    def addi(self, instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        imm = BinaryConversor().B2D(instruction['imm'])
        self.REGISTERS.setRegister(instruction['rt'],r1+imm)

    def sub(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])
        self.REGISTERS.setRegister(instruction['rd'],r1-r2)

    def mult(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])
        self.REGISTERS.setRegister('lo',r1*r2)
        self.REGISTERS.setRegister('hi',-1) if r1*r2 < 0 else self.REGISTERS.setRegister('hi',0)

    def mflo(self,instruction):

        lo = self.REGISTERS.getRegister('lo')
        self.REGISTERS.setRegister(instruction['rd'],lo)

    def div(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])
        self.REGISTERS.setRegister('lo',int(r1/r2))
        self.REGISTERS.setRegister('hi',int(r1%r2))

    def and_(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])

        r1 = BinaryConversor().D2B(r1)
        r2 = BinaryConversor().D2B(r2)

        r3_array = ['1' if((r1[x])==r2[x]) else '0' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rd'],r3)

    def andi(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        imm = instruction['imm']

        r1 = BinaryConversor().D2B(r1)
        imm = BinaryConversor().B2D(imm)
        imm = BinaryConversor().D2B(imm)

        r3_array = ['1' if((r1[x])==imm[x]) else '0' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rt'],r3)

    def or_(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])

        r1 = BinaryConversor().D2B(r1)
        r2 = BinaryConversor().D2B(r2)

        r3_array = ['1' if(r1[x] == '1' or r2[x] == '1') else '0' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rd'],r3)

    def ori(self,instruction):

        r1 = self.REGISTERS.getRegister(instruction['rs'])

        imm = instruction['imm'] #isso ja e binario, mas de 16bits

        r1 = BinaryConversor().D2B(r1)
        imm = BinaryConversor().B2R(imm)#convertido pra decimal (APENAS POSITIVO)
        imm = BinaryConversor().D2B(imm)#convertido pra binario de 32 bits

        r3_array = ['1' if(r1[x] == '1' or imm[x] == '1') else '0' for x in range(0,32)]
        r3 = ''.join(r3_array)
        self.REGISTERS.setRegister(instruction['rt'],r3)

    def xor(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])

        r1 = BinaryConversor().D2B(r1)
        r2 = BinaryConversor().D2B(r2)

        r3_array = ['1' if(r1[x] != r2[x]) else '0' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rd'],r3)

    def xori(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        imm = instruction['imm']

        r1 = BinaryConversor().D2B(r1)
        imm = BinaryConversor().B2D(imm)
        imm = BinaryConversor().D2B(imm)

        r3_array = ['0' if((r1[x])==imm[x]) else '1' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rt'],r3)

    def nor(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])

        r1 = BinaryConversor().D2B(r1)
        r2 = BinaryConversor().D2B(r2)

        r3_array = ['0' if(r1[x] == '1' or r2[x] == '1') else '1' for x in range(0,32)]
        r3 = ''.join(r3_array)

        self.REGISTERS.setRegister(instruction['rd'],r3)

    def slt(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        r2 = self.REGISTERS.getRegister(instruction['rt'])
        r3 = 1 if (r1<r2) else 0
        self.REGISTERS.setRegister(instruction['rd'],r3)

    def lui(self,instruction):
        r1 = self.REGISTERS.getRegister(instruction['rs'])
        imm = BinaryConversor().B2R(instruction['imm'])*-1

        self.REGISTERS.setRegister(instruction['rt'],r1+imm)

    def sll(self,instruction):

        rt = self.REGISTERS.getRegister(instruction['rt'])
        rt = BinaryConversor().D2B(rt)
        sa = BinaryConversor().B2D(instruction['shamt'])

        rt = rt[sa:]
        rt = rt+('0'*sa)

        rt = BinaryConversor().B2D(rt)
        self.REGISTERS.setRegister(instruction['rd'],rt)

    def srl(self,instruction):

        rt = self.REGISTERS.getRegister(instruction['rt'])
        rt = BinaryConversor().D2B(rt)
        sa = BinaryConversor().B2D(instruction['shamt'])

        rt = rt[0:32-sa]
        rt = ('0'*sa)+rt

        rt = BinaryConversor().B2D(rt)
        self.REGISTERS.setRegister(instruction['rd'],rt)

    def sra(self,instruction):
        #shift logical a direta mantendo o sinal
        rt = self.REGISTERS.getRegister(instruction['rt'])

        if(rt>0):
            c = '0'
        else:
            c = '1'

        rt = BinaryConversor().D2B(rt)
        sa = BinaryConversor().B2D(instruction['shamt'])

        rt = rt[0:32-sa]

        rt = (c*sa)+rt
        print(rt)
        rt = BinaryConversor().B2D(rt)
        self.REGISTERS.setRegister(instruction['rd'],rt)

    def lw(self,instruction):
        rs = self.REGISTERS.getRegister(instruction['rs'])
        imm = BinaryConversor().B2D(instruction['imm'])
        value = self.DataMemory.getMemoryAdress(rs+imm)
        self.REGISTERS.setRegister(instruction['rt'],value)

    def sw(self,instruction):
        rs = self.REGISTERS.getRegister(instruction['rs'])
        rt = self.REGISTERS.getRegister(instruction['rt'])
        imm = BinaryConversor().B2D(instruction['imm'])
        self.DataMemory.setMemoryAdress((rs+imm), rt)

    def j(self,instruction):

        target = instruction['target']+'00'
        target = BinaryConversor().B2D(target)
        self.REGISTERS.setRegister('pc',target)

    def jal(self,instruction):

        pc = self.REGISTERS.getRegister('pc')
        self.REGISTERS.setRegister('11111',pc) #1111 = codigo para $ra
        self.j(instruction)

    def jr(self,instruction):
        ra = self.REGISTERS.getRegister(instruction['rs'])
        self.REGISTERS.setRegister('pc',ra)

    def beq(self,instruction):
        rs = self.REGISTERS.getRegister(instruction['rs'])
        rt = self.REGISTERS.getRegister(instruction['rt'])
        if(rs==rt):
            offset = BinaryConversor().B2D(instruction['imm'])*4
            pc = self.REGISTERS.getRegister('pc')+offset
            self.REGISTERS.setRegister('pc',pc)

    def bnq(self,instruction):
        rs = self.REGISTERS.getRegister(instruction['rs'])
        rt = self.REGISTERS.getRegister(instruction['rt'])
        if(rs!=rt):
            offset = BinaryConversor().B2D(instruction['imm'])*4
            pc = self.REGISTERS.getRegister('pc')+offset
            self.REGISTERS.setRegister('pc',pc)

    def syscall(self,instruction):

        v0 = self.REGISTERS.getRegister(2) #2 = codigo para $v0
        self.call = v0
