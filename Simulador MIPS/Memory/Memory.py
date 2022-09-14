class Memory:

    def __init__(self):
        self.memory = dict(zip([(x*4) for x in range(0,2048)],[0 for x in range(0,2048)]))

    def getMemoryAdress(self,adress):
        return self.memory[adress]

    def setMemoryAdress(self,adress,value):
        self.memory[adress] = value
