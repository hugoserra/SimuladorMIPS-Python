from Aritmetic_Core.BinaryConversor import BinaryConversor

class Registers:

    def __init__(self):
        self.registers = dict(zip([x for x in range(0,32)],[0 for x in range(0,32)]))
        self.registers.update({'pc':4194304,'hi':0,'lo':0, 29:(4*1024)})
        #29 representa o registrador $sp, que recebe o endereço 4096 inicialmente

    def setRegister(self,code,value):
        if(code == 'pc' or code == 'hi' or code == 'lo'):
            self.registers[code] = value
            return True

        code = BinaryConversor().B2R(code)
        if(type(value) == str):
            value = BinaryConversor().B2D(value)
        self.registers[code] = value

    def getRegister(self,code):
        if(code == 'pc' or code == 'hi' or code == 'lo'):
            return self.registers[code]

        if(type(code) == str):
            return self.registers[BinaryConversor().B2R(code)]
        return self.registers[code]
