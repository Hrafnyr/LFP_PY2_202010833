
class errorS: #Guarda errores sintacticos
    def __init__(self, caracter,tipo,fila,columna):
        self.caracter = caracter
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def enviarErrores(self):
        return [self.caracter,self.tipo,self.fila, self.columna]
    
    def getCaracter(self):
        return self.caracter
    def getTipo(self):
        return self.tipo
    def getFila(self):
        return self.fila
    def getColumna(self):
        return self.columna