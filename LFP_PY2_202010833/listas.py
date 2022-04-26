
from guardarToken import token1
from errores import error
from tkinter import messagebox as MessageBox
import webbrowser

class lista():
    def __init__(self):
        self.listaTokens = [] #lista que guarda los tokens
        self.listaErrores = [] #lista que guarda los errores
        self.contadorReportes = 1

    def insertarToken(self, token,valor,fila,columna):
        self.listaTokens.append(token1(token,valor,fila,columna))

    def insertError(self, caracter,tipo,fila,columna):
        self.listaErrores.append(error(caracter,tipo,fila,columna))

    def mostrarTokens(self): #Metodo de prueba para verificar el correcto guardado de los tokens
        i:token1
        if len(self.listaTokens)==0:
            print('No hay tokens aún')
            MessageBox.showinfo('Mensaje','No hay tokens para mostrar')
        else:
            aux = []
            for i in self.listaTokens:
                r =i.enviarTokens()
                print(r)
                aux.append(r)
            datos = sintantico()
            datos.insert(aux)
            datos.inicio()

    def mostrarErrores(self): #Metodo de prueba para verificar el correcto guardado de los errores
        i:error
        if len(self.listaErrores)==0:
            print('No hay errores')
            MessageBox.showinfo('Mensaje','No hay errores')
        else:
            MessageBox.showerror('Atención','Se encontraron errores')
            for i in self.listaErrores:
                s = i.enviarErrores()
                print(s)
           

    def limpiarLogErrores(self):
        del self.listaErrores[:]
        print("Vaciando...")
        MessageBox.showinfo('Mensaje','Errores eliminados correctamente')

    def limpiarLogTokens(self):
        del self.listaTokens[:]
        print("Vaciando...")
        MessageBox.showinfo('Mensaje','Tokens eliminados correctamente')

    def reporteTokens(self):

        if len(self.listaTokens)==0:
            print('No hay información')
            MessageBox.showinfo('Atención','No se ha analizado el texto')
        else:
            print('-------------------> Generando reporte, espere...')
            name = "Reporte"+str(self.contadorReportes)+"Tokens.html"
            reporte = open(name, 'w')

            html_parte1 = '''
            <body style="background-color:#F4F8F4;">
            <h2 style="text-align: center;">"Reporte de Tokens"</h2>
            <table style="width: 50%; border-collapse: collapse; border-style: solid; margin: 0 auto;" border="1">
            <tbody>
            <tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">No.</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Token</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Lexema</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Fila</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Columna</span></strong></td>
            </tr>'''

            html_parte2 = ''
            contador = 1
            i:token1
            for i in self.listaTokens:
                token = i.getToken()
                valor = i.getValor()
                fila =  i.getFila()
                columna = i.getColumna()

                html_parte2 += '''<tr>
            <td style="width: 2%;">{}</td>
            <td style="width: 5%;">{}</td>
            <td style="width: 5%; text-align: center">{}</td>
            <td style="width: 2%; text-align: center">{}</td>
            <td style="width: 2%; text-align: center">{}</td>
            </tr>'''.format(contador,token,valor,fila,columna)
                contador+=1

            hmtl_fin = '''
            </tbody>
            </table> </body>'''

            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte.write(html_archivo)
            reporte.close()

            print('Reporte creado con éxito')
            self.contadorReportes+=1
            webbrowser.open_new_tab(name)

    def reporteErrores(self):
        if len(self.listaErrores)==0:
            print('No hay información')
            MessageBox.showinfo('Atención','No hay errores')
        else:
            print('-------------------> Generando reporte, espere...')
            contadorReportes = 1
            name = "Reporte"+str(contadorReportes)+"Error.html"
            reporte = open(name, 'w')

            html_parte1 = '''
            <body style="background-color:#F4F8F4;">
            <h2 style="text-align: center;">"Reporte de Errores"</h2>
            <table style="width: 50%; border-collapse: collapse; border-style: solid; margin: 0 auto;" border="1">
            <tbody>
            <tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">No.</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Caracter</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">tipo</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Fila</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Columna</span></strong></td>
            </tr>'''

            html_parte2 = ''
            contador = 1
            e:error
            for e in self.listaErrores:
                caracter = e.getCaracter()
                tipo = e.getTipo()
                fila = e.getFila()
                columna = e.getColumna()
                html_parte2 += '''<tr>
            <td style="width: 2%;">{}</td>
            <td style="width: 5%;">{}</td>
            <td style="width: 5%; text-align: center">{}</td>
            <td style="width: 2%; text-align: center">{}</td>
            <td style="width: 2%; text-align: center">{}</td>
            </tr>'''.format(contador,caracter,tipo,fila,columna)
                contador+=1

            hmtl_fin = '''
            </tbody>
            </table></body>'''

            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte.write(html_archivo)
            reporte.close()

            print('Reporte creado con éxito')
            contadorReportes+=1
            webbrowser.open_new_tab(name)

class sintantico():

    def __init__(self):
        self.tokensS = []
        self.errores = []
        self.columna = 0

    def insert(self,lista):
        self.tokensS.extend(lista)

    def insertErrorS(self, caracter,tipo,fila,columna):
        self.errores.append(error(caracter,tipo,fila,columna))   

    def quitarToken(self):
        #Sacar el primer token de la lista
        try:
            return self.tokensS.pop(0)
        except:
            return None
    
    def getToken(self):
        #Método para observar el token
        try:
            return self.tokensS[0]
        except:
            return None

    def showError(self): #Metodo de prueba para verificar el correcto guardado de los errores
        i:error
        if len(self.errores)==0:
            print('No hay errores Sintácticos')
            #MessageBox.showinfo('Mensaje','No hay errores')
        else:
            #MessageBox.showerror('Atención','Se encontraron errores')
            for i in self.errores:
                s = i.enviarErrores()
                print(s)

    #----- Inicio del analizador sintáctico con base a la gramática establecidad en la documentacion ---------
    
    #<INICIO> ::= <RESULTADO_PARTIDO> | <JORNADA> | <GOLES> | <T_TEMPORADA> | <PARTIDOS> | <TOP> | <ADIOS>
    def inicio(self):

        #Primero se verifica hacia donde ir según el token 
        tmp = self.getToken()

        if tmp is None:
            self.insertErrorS("Null","Se esperaba: RESULTADO, JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS",1,0)
        elif tmp[0] == "tk_resultado":
            self.resultadoPartido()
        elif tmp[0] == "tk_jornada":
            self.jornada()
        elif tmp[0] == "tk_goles":
            self.goles()
        elif tmp[0] == "tk_tabla":
            self.t_Temporada()
        elif tmp[0] == "tk_partidos":
            self.partidos()
        elif tmp[0] == "tk_top":
            self.top()
        elif tmp[0] == "tk_adios":
            self.adios()
        else:
            label = "Error: {}".format(tmp[1])
            self.insertErrorS(label,"Se esperaba: RESULTAOD, JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS",1,0)
        
        self.showError()

    #<RESULTADO_PARTIDO> ::= tk_resultado(ya analizado) tk_cadena tk_vs tk_cadena tk_temporada tk_Smenor tk_año tk_guion tk_año tk_Smayor
    def resultadoPartido(self):
        pass

    def jornada(self):
        pass

    def goles(self):
        pass

    def t_Temporada(self):
        pass

    def partidos(self):
        pass

    def top(self):
        pass

    def adios(self):
        pass



