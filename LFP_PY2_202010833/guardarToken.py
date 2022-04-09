
class token1: #Guarda los tokens analizados
    def __init__(self, token,valor,fila,columna):
        self.token = token
        self.valor = valor
        self.fila = fila
        self.columna = columna
     
    def enviarTokens(self):
        return [self.token, self.valor, self.fila, self.columna]
    
    def getToken(self):
        return self.token
    def getValor(self):
        return self.valor
    def getFila(self):
        return self.fila
    def getColumna(self):
        return self.columna