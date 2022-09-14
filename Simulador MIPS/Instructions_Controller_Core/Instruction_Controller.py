from Aritmetic_Core.Logic_Aritmetic_Core import Logic_Aritmetic_Core

class FormatDecoder:

    def Decode(self,instruction_32bit):

        self.tipe_of_opcode = {
        '000000':'R',
        '001000':'I',
        '001100':'I',
        '001101':'I',
        '001110':'I',
        '001111':'I',
        '100011':'I',
        '101011':'I',
        '000100':'I',
        '000101':'I',
        '000010':'J',
        '000011':'J'}

        self.opcode = instruction_32bit[0:6]

        if(self.tipe_of_opcode[self.opcode] == 'R'):
            return self.Mask_Register(instruction_32bit)
        elif(self.tipe_of_opcode[self.opcode] == 'I'):
            return self.Mask_Immediate(instruction_32bit)
        elif(self.tipe_of_opcode[self.opcode] == 'J'):
            return self.Mask_Jump(instruction_32bit)

    def Mask_Register(self,instruction_32bit):
        rs      = instruction_32bit[6:11]
        rt      = instruction_32bit[11:16]
        rd      = instruction_32bit[16:21]
        shamt   = instruction_32bit[21:26]
        funct   = instruction_32bit[26:32]
        return {'type':'R','opcode':self.opcode,'rs':rs,'rt':rt,'rd':rd,'shamt':shamt,'funct':funct}

    def Mask_Immediate(self,instruction_32bit):
        rs      = instruction_32bit[6:11]
        rt      = instruction_32bit[11:16]
        immediate   = instruction_32bit[16:32]

        return {'type':'I','opcode':self.opcode,'rs':rs,'rt':rt,'imm':immediate}

    def Mask_Jump(self,instruction_32bit):
        target   = instruction_32bit[6:32]
        return {'type':'J','opcode':self.opcode,'target':target}


class Execute_Instruction:

    def __init__(self,instruction,DataMemory,registers):

        instruction = FormatDecoder().Decode(instruction)
        self.Logic_Aritmetic_Core = Logic_Aritmetic_Core(DataMemory,registers)
        self.R(instruction) if instruction['type'] == 'R' else None
        self.I(instruction) if instruction['type'] == 'I' else None
        self.J(instruction) if instruction['type'] == 'J' else None

    def R(self,instruction):
        self.Logic_Aritmetic_Core.add(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100000") else None
        self.Logic_Aritmetic_Core.sub(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100010") else None
        self.Logic_Aritmetic_Core.mult(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "011000") else None
        self.Logic_Aritmetic_Core.mflo(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "010010") else None
        self.Logic_Aritmetic_Core.div(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "011010") else None
        self.Logic_Aritmetic_Core.and_(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100100") else None
        self.Logic_Aritmetic_Core.or_(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100101") else None
        self.Logic_Aritmetic_Core.xor(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100110") else None
        self.Logic_Aritmetic_Core.nor(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "100111") else None
        self.Logic_Aritmetic_Core.slt(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "101010") else None
        self.Logic_Aritmetic_Core.sll(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "000000") else None
        self.Logic_Aritmetic_Core.srl(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "000010") else None
        self.Logic_Aritmetic_Core.sra(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "000011") else None
        self.Logic_Aritmetic_Core.jr(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "001000") else None
        self.Logic_Aritmetic_Core.syscall(instruction) if(instruction['opcode'] == "000000" and instruction['funct'] == "001100") else None

    def I(self,instruction):
        self.Logic_Aritmetic_Core.addi(instruction) if(instruction['opcode'] == "001000") else None
        self.Logic_Aritmetic_Core.lui(instruction) if(instruction['opcode'] == "001111") else None
        self.Logic_Aritmetic_Core.andi(instruction) if(instruction['opcode'] == "001100") else None
        self.Logic_Aritmetic_Core.ori(instruction) if(instruction['opcode'] == "001101") else None
        self.Logic_Aritmetic_Core.xori(instruction) if(instruction['opcode'] == "001110") else None
        self.Logic_Aritmetic_Core.sw(instruction) if(instruction['opcode'] == "101011") else None
        self.Logic_Aritmetic_Core.lw(instruction) if(instruction['opcode'] == "100011") else None
        self.Logic_Aritmetic_Core.beq(instruction) if(instruction['opcode'] == "000100") else None
        self.Logic_Aritmetic_Core.bnq(instruction) if(instruction['opcode'] == "000101") else None

    def J(self,instruction):
        self.Logic_Aritmetic_Core.j(instruction) if(instruction['opcode'] == "000010") else None
        self.Logic_Aritmetic_Core.jal(instruction) if(instruction['opcode'] == "000011") else None
