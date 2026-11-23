import copia_calculadora_03_para_cientifica_06 as cal

class Cientifica(cal.CALCULADORA):
    def sumatorio(self):
        suma=0
        for n in range(self.operando_1,self.operando_2+1):
            suma+=n
        return suma 