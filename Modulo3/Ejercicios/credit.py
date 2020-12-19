class Tarjeta:
    def __init__(self, numtarjeta):
        self.numtarjeta = numtarjeta

    #Validando la tarjeta con algoritmo Luhn
    def Luhn(self):
            pos1 = len(self.numtarjeta) - 2
            pos2 = len(self.numtarjeta) - 1
            suma1 = 0
            suma2 = 0
    
            while (pos1 + pos2) >= -1:
                i = int(self.numtarjeta[pos1])
                j = int(self.numtarjeta[pos2])

                if pos1 != -1:    
                    if i*2 >= 10:
                        suma1 = suma1 + int(i*2/10) + (i*2)%10
                    else:
                        suma1 = suma1 + i*2
                
                suma2 = suma2 + j
    
                pos1 = pos1 - 2
                pos2 = pos2 - 2
            
            if (suma1 + suma2)%10 == 0:
                return True
            else:
                print("No pasó el Luhn")
                return False
    
    #Validando la tarjeta por cantidad de dígitos y algoritmo Luhn
    def validar(self):
        if (len(self.numtarjeta) == 15 or len(self.numtarjeta) == 16 or len(self.numtarjeta) == 13) and self.Luhn():
            return True
        else:
            return False

    def tipo(self):
        if self.validar():
            if len(self.numtarjeta) == 15 and (self.numtarjeta[0:2] == '34' or self.numtarjeta[0:2] == '37'):
                print("AMEX\n")
            elif len(self.numtarjeta) == 16  and (self.numtarjeta[0:2] == '51' or self.numtarjeta[0:2] == '52' or self.numtarjeta[0:2] == '53' or self.numtarjeta[0:2] == '54' or self.numtarjeta[0:2] == '55'):
                print("MASTERCARD\n")
            elif (len(self.numtarjeta) == 13 or len(self.numtarjeta) == 16) and self.numtarjeta[0] == '4':
                print("VISA\n")
            else:
                print("INVALID\n")
        else:
            print("INVALID\n")


if __name__ == '__main__':
    while True:
        numtarjeta = input("Introduce tu número de tarjeta: ")
        for digito in numtarjeta:
            try:
                n = int(digito)
                valido = True
            except:
                valido = False
                print("El número de tarjeta solo puede contener números")
                break

        if valido:
            break

    tarjeta = Tarjeta(numtarjeta)
    tarjeta.tipo()


        
        
        

    