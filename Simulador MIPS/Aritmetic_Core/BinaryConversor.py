class BinaryConversor:

    def __init__(self):
        pass

    def B2D(self,binary_number):#Converte binarios comuns e complementos de dois (101 = 3) (0101 = 5) Usado para o nucleo aritmetico
        decimal_result = 0
        j = len(binary_number)-1
        sub = 0

        for i in range(0,len(binary_number)):

            if(binary_number[0]=='0'):#positive number
                decimal_result += (2**i) if binary_number[j] == '1' else 0
                j-=1

            if(binary_number[0]=='1'):#negative number
                all = 2**(len(binary_number)-1)
                if(i!=len(binary_number)-1):
                    sub += (2**i) if binary_number[j] == '1' else 0
                j-=1
                decimal_result = (all - sub)*-1

        return decimal_result

    def B2R(self,binary_number):#Converte apenas binarios comuns, neste caso (101 = 5) Usada para operar registradores
        decimal_result = 0
        j = len(binary_number)-1
        sub = 0

        for i in range(0,len(binary_number)):
            decimal_result += (2**i) if binary_number[j] == '1' else 0
            j-=1

        return decimal_result

    def D2B(self,decimal_number):#Converte decimais negativos e positivos

        if(decimal_number>0):
            negative = False
        else:
            negative = True
            decimal_number = decimal_number*-1

        binary_array_invert = []
        while(decimal_number != 1):

            binary_part = 1 if((decimal_number%2)!=0) else 0
            decimal_number = int(decimal_number/2)
            binary_array_invert.append(binary_part)


        binary_array_invert.append(1)

        binary_array =  ['0' for i in range(0,(32-len(binary_array_invert)))]
        for i in range(len(binary_array_invert)-1,-1,-1):
            binary_array.append(str(binary_array_invert[i]))

        string = ''

        if(negative == False):
            return string.join(binary_array[0:32])
        else:
            binary_array_negative = ['1' if i == '0' else '0' for i in binary_array]
            trava = True
            for i in range(1,32):
                i = i*-1

                if(binary_array_negative[i]=='0' and trava):
                    binary_array_negative[i] = '1'
                    trava = False

            return string.join(binary_array_negative[0:32])
