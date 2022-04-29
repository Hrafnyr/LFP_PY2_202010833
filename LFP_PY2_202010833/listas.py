
from guardarToken import token1
import os as documento
from errores import error
from erroresSi import errorS
from tkinter import messagebox as MessageBox
import webbrowser
import pandas as pd

class lista():
    def __init__(self):
        self.listaTokens = [] #lista que guarda los tokens
        self.listaErrores = [] #lista que guarda los errores
        self.contadorReportes = 1
        self.controlTokens = 0 #Permite el múltiple análisis sintactico sin limpiar datos

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
            datos = sintantico()
            datos.limpiar()
            aux = []
            aux2 = 0
            for i in self.listaTokens:
               
                r =i.enviarTokens()
                print(r)

                if self.controlTokens == 0:
                    self.controlTokens+=1
                    aux.append(r) 
                elif self.controlTokens > 0:
                    if aux2 >= self.controlTokens:
                        self.controlTokens+=1
                        aux.append(r)
                
                aux2 += 1


            datos.insert(aux)
            respuesta = datos.inicio()
            return respuesta

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
        data= sintantico()
        del self.listaErrores[:]
        data.limpiarError()
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
        self.equipos = []
        self.puntajes =[]
        self.errores = []
        self.columna = 0
        self.contador = 0

    def insert(self,lista):
        self.tokensS.extend(lista)

    def insertErrorS(self, caracter,tipo,fila,columna):
        self.errores.append(errorS(caracter,tipo,fila,columna))  

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
        i:errorS
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
            r = "Se esperaba: RESULTADO,JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS" + "\n"
            return r
        elif tmp[0] == "tk_resultado":
            r = self.resultadoPartido()
            return r
        elif tmp[0] == "tk_jornada":
            r = self.jornada()
            return r
        elif tmp[0] == "tk_goles":
            r = self.goles()
            return r
        elif tmp[0] == "tk_tabla":
            r = self.t_Temporada()
            return r
        elif tmp[0] == "tk_partidos":
            r = self.partidos()
            return r
        elif tmp[0] == "tk_top":
            r = self.top()
            return r
        elif tmp[0] == "tk_adios":
            r = self.adios()
            return r
        else:
            label = "Error: {}".format(tmp[1])
            txt = "Se esperaba: RESULTADO,JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS" + "\n"
            self.insertErrorS(label,"Se esperaba: RESULTADO,JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS",1,0)
            return txt

    #--> se espera tk_resultado
    def resultadoPartido(self):
        equipo1 = None
        equipo2 = None
        año1 = None
        año2 = None

        tk = self.quitarToken()
        if tk[0] == "tk_resultado":
            
            #---> se espera tk_cadena
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba una cadena",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_cadena":
                equipo1 = tk[1]
                #---> se espera tk_vs
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba VS",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                elif tk[0] == "tk_vs":
                
                    #---> se espera tk_cadena
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba una cadena",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_cadena":
                        equipo2 = tk[1]
                        #---> se espera tk_temporada
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_temporada":
                            
                            #---> se espera tk_Smenor
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un <",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_Smenor":

                                #---> se espera tk_año
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un año",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_año":
                                    año1 = tk[1]
                                    #---> se espera tk_guion
                                    tk = self.quitarToken()
                                    if tk is None:
                                        self.insertErrorS("Null","Se esperaba un -",11,0)
                                        return #Si no viene entonces ya no se ejecuta lo demás
                                    elif tk[0] == "tk_guion":

                                        #---> se espera tk_año
                                        tk = self.quitarToken()
                                        if tk is None:
                                            self.insertErrorS("Null","Se esperaba un año",11,0)
                                            return #Si no viene entonces ya no se ejecuta lo demás
                                        elif tk[0] == "tk_año":
                                            año2 = tk[1]
                                            #---> se espera tk_Smayor
                                            tk = self.quitarToken()
                                            if tk is None:
                                                self.insertErrorS("Null","Se esperaba un >",11,0)
                                                return #Si no viene entonces ya no se ejecuta lo demás
                                            elif tk[0] == "tk_Smayor":
                                                
                                                #Funcionalidad a realizar
                                                print("Todo correcto")
                                                print("procesando...")

                                                dataR = self.resultadoCSV(equipo1,equipo2,año1,año2)   
                                                return dataR

                                            else:
                                                label = "Error: {}".format(tk[1])
                                                self.insertErrorS(label,"Se esperaba un >",11,0)
                                        else:
                                            label = "Error: {}".format(tk[1])
                                            self.insertErrorS(label,"Se esperaba un año",11,0)                                            
                                    else:
                                        label = "Error: {}".format(tk[1])
                                        self.insertErrorS(label,"Se esperaba un -",11,0)
                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un año",11,0)
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un <",11,0)        
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba una cadena",11,0)
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba VS",11,0)
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba una cadena",11,0)
        else:
            self.insertErrorS("Null","Se esperaba RESULTADO",1,0)            

    #--> se espera tk_jornada
    def jornada(self):
        numJornada = None
        año1 = None
        año2 = None
        asignar_nombre = None

        tk = self.quitarToken()
        if tk[0] == "tk_jornada":
            
            #---> se espera tk_num
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_num":
                numJornada = tk[1]
                #---> se espera tk_temporada
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                elif tk[0] == "tk_temporada":
                            
                    #---> se espera tk_Smenor
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un <",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_Smenor":

                        #---> se espera tk_año
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba un año",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_año":
                            año1 = tk[1]
                            #---> se espera tk_guion
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un -",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_guion":

                                #---> se espera tk_año
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un año",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_año":
                                    año2 = tk[1]
                                    #---> se espera tk_Smayor
                                    tk = self.quitarToken()
                                    if tk is None:
                                        self.insertErrorS("Null","Se esperaba un >",11,0)
                                        return #Si no viene entonces ya no se ejecuta lo demás
                                    elif tk[0] == "tk_Smayor":
                                        
                                        #Se espera ---> <ASIGNAR_NOMBRE>
                                        #Se llama la función
                                        asignar_nombre = self.asignarNombre()
                                        if asignar_nombre is None: #Si es none entonces no viene esa bandera
                                            asignar_nombre = "jornada.html"
                                            print("Agregando nombre por defecto: jornada.html")
                                        else:
                                            asignar_nombre = asignar_nombre+".html"
                                            print("El nombre de asignación es:", asignar_nombre)

                                        print(numJornada,año1,año2,asignar_nombre)
                                        resp = self.jornadaCSV(numJornada,año1,año2,asignar_nombre)
                                        return resp

                                    else:
                                        label = "Error: {}".format(tk[1])
                                        self.insertErrorS(label,"Se esperaba un >",11,0)
                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un año",11,0)                                  
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un -",11,0)
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba un año",11,0)
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un <",11,0)        
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba un número de 1 o 2 dígitos positivos",11,0)
        else:
            self.insertErrorS("Null","Se esperaba JORNADA",1,0)       

    #Produccion ::= tk_-f tk_id | épsilon
    def asignarNombre(self):
        tk = self.getToken()

        #Si no viene el nombre
        if tk is None:
            return None
        
        else:
            #---> se espera tk_-f
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba -f",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_guion":
                
                #---> se espera tk_-f
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba -f",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás

                elif tk[0] == "tk_-f":

                    #---> se espera tk_id
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un ID",11,0)
                        return
                    elif tk[0] == "tk_id":
                        
                        #Funcionalidad
                        print("El nombre es: ",tk[1])
                        return tk[1]

                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba -f",11,0)
                else: 
                    return None #Si no lo encuentra entonces devuelve None para simular el épsilon
            else:
                return None   

    #---> se espera tk_goles        
    def goles(self):
        equipo = None
        condicion = None
        año1 = None
        año2 = None

        tk = self.quitarToken()
        if tk[0] == "tk_goles":

            #Se espera ---> <CONDICION>
            #Se llama la función
            condicion = self.condicion()
            if condicion is None:
                self.insertErrorS("Null","Se esperaba LOCAL,VISITANTE O TOTAL",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            else:
                print("Condicion es:", condicion)
            
                #---> se espera tk_cadena
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba una cadena",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                
                elif tk[0] == "tk_cadena":
                    equipo = tk[1]
                    #---> se espera tk_temporada
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_temporada":

                        #---> se espera tk_Smenor
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba un <",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_Smenor":

                            #---> se espera tk_año
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un año",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_año":
                                año1 = tk[1]
                                #---> se espera tk_guion
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un -",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_guion":

                                    #---> se espera tk_año
                                    tk = self.quitarToken()
                                    if tk is None:
                                        self.insertErrorS("Null","Se esperaba un año",11,0)
                                        return #Si no viene entonces ya no se ejecuta lo demás
                                    elif tk[0] == "tk_año":
                                        año2 = tk[1]
                                        #---> se espera tk_Smayor
                                        tk = self.quitarToken()
                                        if tk is None:
                                            self.insertErrorS("Null","Se esperaba un >",11,0)
                                            return #Si no viene entonces ya no se ejecuta lo demás
                                        elif tk[0] == "tk_Smayor":
                                            
                                            #Funcionalidad
                                            print("Todo correcto")
                                            print("procesando...")
                                            res = self.golesCSV(equipo,año1,año2,condicion)
                                            return res

                                        else:
                                            label = "Error: {}".format(tk[1])
                                            self.insertErrorS(label,"Se esperaba un >",11,0)
                                    else:
                                        label = "Error: {}".format(tk[1])
                                        self.insertErrorS(label,"Se esperaba un año",11,0)
                                        
                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un -",11,0)
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un año",11,0)
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba un <",11,0)        
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba una cadena",11,0)
        else:
            self.insertErrorS("Null","Se esperaba GOLES",1,0)    
  
    #<CONDICION>::= tk_local | tk_visitante | tk_total
    def condicion(self):

        tk = self.getToken()

        #Si no viene el token
        if tk is None:
            return None
        
        else:
            #---> se espera tk_local o tk_visitante o tk_total
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba LOCAL,VISITANTE O TOTAL",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_local" or tk[0] == "tk_visitante" or tk[0] == "tk_total":
                
                        #Funcionalidad
                        print("La condicion es: ",tk[1])
                        return tk[1]
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba LOCAL,VISITANTE O TOTAL",11,0)     

    #--> Se espera tk_tabla
    def t_Temporada(self):
        año1 = None
        año2 = None
        asignar_nombre = None

        tk = self.quitarToken()
        if tk[0] == "tk_tabla":
            
            #---> se espera tk_temporada
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            elif tk[0] == "tk_temporada":
                       
                #---> se espera tk_Smenor
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba un <",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                elif tk[0] == "tk_Smenor":

                    #---> se espera tk_año
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un año",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_año":
                        año1 = tk[1]
                        #---> se espera tk_guion
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba un -",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_guion":

                            #---> se espera tk_año
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un año",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_año":
                                año2 = tk[1]
                                #---> se espera tk_Smayor
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un >",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_Smayor":
                                    
                                    #Se espera ---> <ASIGNAR_NOMBRE>
                                    #Se llama la función
                                    asignar_nombre = self.asignarNombre()
                                    if asignar_nombre is None:
                                        asignar_nombre = "temporada.html"
                                        print("Agregando nombre por defecto:",asignar_nombre)
                                    else:
                                        asignar_nombre = asignar_nombre+".html"
                                        print("El nombre de asignación es:", asignar_nombre)

                                    #Funcionalidad
                                    res = self.tablaTemp(año1,año2,asignar_nombre)
                                    return res

                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un >",11,0)
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un año",11,0)
                                
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba un -",11,0)
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un año",11,0)
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba un <",11,0)        
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
        else:
            self.insertErrorS("Null","Se esperaba TABLA",1,0)   

    #--> Se espera tk_partidos
    def partidos(self):
        equipo = None
        año1 = None
        año2 = None
        asignar_nombre = None
        jornada_inicial = None
        jornada_final = None

        tk = self.quitarToken()
        if tk[0] == "tk_partidos":
            
            #---> se espera tk_cadena
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba un cadena",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_cadena":
                equipo = tk[1]
                #---> se espera tk_temporada
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                elif tk[0] == "tk_temporada":
      
                    #---> se espera tk_Smenor
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un <",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_Smenor":

                        #---> se espera tk_año
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba un año",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_año":
                            año1 = tk[1]
                            #---> se espera tk_guion
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un -",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_guion":

                                #---> se espera tk_año
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un año",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_año":
                                    año2 = tk[1]
                                    #---> se espera tk_Smayor
                                    tk = self.quitarToken()
                                    if tk is None:
                                        self.insertErrorS("Null","Se esperaba un >",11,0)
                                        return #Si no viene entonces ya no se ejecuta lo demás
                                    elif tk[0] == "tk_Smayor":
                                        
                                        #Se espera ---> <ASIGNAR_NOMBRE>
                                        #Se llama la función
                                        asignar_nombre = self.asignarNombre()
                                        if asignar_nombre is None:
                                            asignar_nombre = "partidos.html"
                                            print("Agregando nombre por defecto:",asignar_nombre)
                                        else:
                                            asignar_nombre = asignar_nombre+".html"
                                            print("El nombre de asignación es:", asignar_nombre)

                                        #Se espera ---> <RANGO1>
                                        #Se llama la función
                                        jornada_inicial = self.rango1()
                                        if jornada_inicial is None:
                                            jornada_inicial = "0"
                                            print("Inicio por defecto: Primer elemento")
                                        else:
                                            print("Se iniciará en:", jornada_inicial)

                                        #Se espera ---> <RANGO2>
                                        #Se llama la función
                                        jornada_final = self.rango2()
                                        if jornada_final is None:
                                            jornada_final = "0"
                                            print("Final por defecto: último elemento")
                                        else:
                                            print("Se terminará en:", jornada_final)
                                        
                                        #Funcionalidad
                                        res = self.tempEquipo(equipo,año1,año2,asignar_nombre,jornada_inicial,jornada_final)
                                        return res
                                    else:
                                        label = "Error: {}".format(tk[1])
                                        self.insertErrorS(label,"Se esperaba un >",11,0)
                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un año",11,0)
                                    
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un -",11,0)
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba un año",11,0)
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un <",11,0)        
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba una cadena",11,0)
        else:
            self.insertErrorS("Null","Se esperaba PARTIDOS",1,0)   

    #<RANGO1> ::= tk_ji tk_num | épsilon
    def rango1(self):
        tk = self.getToken()

        #Si no viene el -ji
        if tk is None:
            return None
        
        else:
            #---> se espera tk_-ji
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba -ji",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_guion":
                
                #---> se espera tk_-ji
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba -ji",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás

                elif tk[0] == "tk_-ji":

                    #---> se espera tk_num
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                        return
                    elif tk[0] == "tk_num":
                        
                        #Funcionalidad
                        print("El inicio es: ",tk[1])
                        return tk[1]

                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                else: 
                    return None #Si no lo encuentra entonces devuelve None para simular el épsilon
            else:
                return None 
    
    #<RANGO2> ::= tk_jf tk_num | épsilon
    def rango2(self):
        tk = self.getToken()

        #Si no viene el -jf
        if tk is None:
            return None
        
        else:
            #---> se espera tk_-jf
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba -jf",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_guion":
                
                #---> se espera -jf
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba -jf",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás

                elif tk[0] == "tk_-jf":

                    #---> se espera tk_num
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                        return
                    elif tk[0] == "tk_num":
                        
                        #Funcionalidad
                        print("El final es: ",tk[1])
                        return tk[1]

                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                else: 
                    return None #Si no lo encuentra entonces devuelve None para simular el épsilon
            else:
                return None

    #--> Se espera un tk_top
    def top(self):
        condicion2 = None
        bandera = None
        año1 = None
        año2 = None

        tk = self.quitarToken()
        if tk[0] == "tk_top":

            #Se espera ---> <CONDICION2>
            #Se llama la función
            condicion2 = self.condicion2()
            if condicion2 is None:
                self.insertErrorS("Null","Se esperaba SUPERIOR o INFERIOR",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            else:
                print("Condicion es:", condicion2)
                
                #---> se espera tk_temporada
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba TEMPORADA",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás
                elif tk[0] == "tk_temporada":

                    #---> se espera tk_Smenor
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un <",11,0)
                        return #Si no viene entonces ya no se ejecuta lo demás
                    elif tk[0] == "tk_Smenor":

                        #---> se espera tk_año
                        tk = self.quitarToken()
                        if tk is None:
                            self.insertErrorS("Null","Se esperaba un año",11,0)
                            return #Si no viene entonces ya no se ejecuta lo demás
                        elif tk[0] == "tk_año":
                            año1 = tk[1]
                            #---> se espera tk_guion
                            tk = self.quitarToken()
                            if tk is None:
                                self.insertErrorS("Null","Se esperaba un -",11,0)
                                return #Si no viene entonces ya no se ejecuta lo demás
                            elif tk[0] == "tk_guion":

                                #---> se espera tk_año
                                tk = self.quitarToken()
                                if tk is None:
                                    self.insertErrorS("Null","Se esperaba un año",11,0)
                                    return #Si no viene entonces ya no se ejecuta lo demás
                                elif tk[0] == "tk_año":
                                    año2 = tk[1]
                                    #---> se espera tk_Smayor
                                    tk = self.quitarToken()
                                    if tk is None:
                                        self.insertErrorS("Null","Se esperaba un >",11,0)
                                        return #Si no viene entonces ya no se ejecuta lo demás
                                    elif tk[0] == "tk_Smayor":
                                        
                                        #Se espera ---> <BANDERA>
                                        #Se llama la función
                                        bandera = self.bandera()
                                        if bandera is None:
                                            bandera = "5"
                                            print("valor por defecto: 5 equipos a mostrar")
                                        else:
                                            print("Equipos a mostrar:", bandera)

                                        #Funcioanalidad
                                        res = self.topCSV(condicion2,año1,año2,bandera)
                                        return res

                                    else:
                                        label = "Error: {}".format(tk[1])
                                        self.insertErrorS(label,"Se esperaba un >",11,0)
                                else:
                                    label = "Error: {}".format(tk[1])
                                    self.insertErrorS(label,"Se esperaba un año",11,0)
                                    
                            else:
                                label = "Error: {}".format(tk[1])
                                self.insertErrorS(label,"Se esperaba un -",11,0)
                        else:
                            label = "Error: {}".format(tk[1])
                            self.insertErrorS(label,"Se esperaba un año",11,0)
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un <",11,0)        
                else:
                    label = "Error: {}".format(tk[1])
                    self.insertErrorS(label,"Se esperaba TEMPORADA",11,0)
        else:
            self.insertErrorS("Null","Se esperaba TOP",1,0) 

    #<CONDICION2>::= tk_superior | tk_inferior
    def condicion2(self):

        tk = self.getToken()

        #Si no viene el token
        if tk is None:
            return None
        
        else:
            #---> se espera tk_superior o tk_inferior
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba SUPERIOR o INFERIOR",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_superior" or tk[0] == "tk_inferior":
                
                        #Funcionalidad
                        print("La condicion es: ",tk[1])
                        return tk[1]
            else:
                label = "Error: {}".format(tk[1])
                self.insertErrorS(label,"Se esperaba SUPERIOR o INFERIOR",11,0)     

    #<BANDERA> ::= tk_n tk_num | épsilon
    def bandera(self):
        tk = self.getToken()

        #Si no viene la bandera
        if tk is None:
            return None
        
        else:
            #---> se espera tk_-n
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba -n",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_guion":
                
                #---> se espera tk_-n
                tk = self.quitarToken()
                if tk is None:
                    self.insertErrorS("Null","Se esperaba -n",11,0)
                    return #Si no viene entonces ya no se ejecuta lo demás

                elif tk[0] == "tk_-n":

                    #---> se espera tk_num
                    tk = self.quitarToken()
                    if tk is None:
                        self.insertErrorS("Null","Se esperaba un número de 1 o 2 dígitos positivo",11,0)
                        return
                    elif tk[0] == "tk_num":
                        
                        #Funcionalidad
                        print("Cantidad de equipos a mostrar: ",tk[1])
                        return tk[1]
                    else:
                        label = "Error: {}".format(tk[1])
                        self.insertErrorS(label,"Se esperaba un número de 1 o 2 dígitos positivo",11,0)
                else: 
                    return None #Si no lo encuentra entonces devuelve None para simular el épsilon
            else:
                return None   

    #--> se espera tk_adios  
    def adios(self):
        tk = self.quitarToken()

        if tk[0] == "tk_adios":
            message = "Adios, vuelve pronto :)"
            return message

    def limpiar(self):
        del self.tokensS [:]
           
    def limpiarError(self):
        del self.errores [:]

    #--------------------- Funciones con CSV para mostrar resultados ---------------------

    def resultadoCSV(self,equipo1,equipo2, año1, año2):

        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]
        
        datos = pd.DataFrame(df, columns = ['Temporada', 'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        res = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo1) & (datos['Equipo2'] == equipo2)].values
        
        if len(res) ==0:
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        
        else:
            print(datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo1) & (datos['Equipo2'] == equipo2)].values)

            show = "El resultado de este partido fue: {} {} - {} {}".format(equipo1,res[0][3],equipo2,res[0][4]) + "\n"
            print(show)
            return show
    
    def jornadaCSV(self,jNum,año1,año2,nombre):
        numJ = int(jNum)
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]
        
        datos = pd.DataFrame(df, columns = ['Temporada', 'Jornada' ,'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        res = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'] == numJ)].values
        
        print(res)       
        if len(res) ==0:
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        
        else:
            
            #Generacion del html:
            reporte_J = open(nombre, 'w')

            html_parte1 = '''
            <body style="background-color:#F4F8F4;">
            <h2 style="text-align: center;">"Reporte de jornada"</h2>
            <table style="width: 50%; border-collapse: collapse; border-style: solid; margin: 0 auto;" border="1">
            <tbody>
            <tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Temporada</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Jornada</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Equipo 1</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Equipo 2</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Goles 1</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Goles 2</span></strong></td>
            </tr>'''

            html_parte2 = ''
     
            for i in res:
                v_Temporada = i[0]
                v_Jornada   = i[1]
                v_Equipo1   = i[2]
                v_Equipo2   = i[3]
                v_Goles1    = i[4]
                v_Goles2    = i[5]

                html_parte2 += '''<tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4ite;">{}</td>
            <td style="width: 2%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            </tr>'''.format(v_Temporada,v_Jornada,v_Equipo1,v_Equipo2,v_Goles1,v_Goles2)
                

            hmtl_fin = '''
            </tbody>
            </table> </body>'''

            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte_J.write(html_archivo)
            reporte_J.close()

            print('Reporte creado con éxito')
            webbrowser.open_new_tab(nombre)

            show = "Generando archivo de resultados jornada {} temporada {} - {}".format(jNum,año1,año2) + "\n"
            print(show)
            return show
    
    def golesCSV(self,equipo,año1,año2,condicion):
        
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]
        
        datos = pd.DataFrame(df, columns = ['Temporada', 'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        
        golesT = 0

        if condicion == 'LOCAL':

            golesT = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo)].groupby('Equipo1')['Goles1'].sum().head().values
       
        elif condicion == 'VISITANTE':

            golesT = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo)].groupby('Equipo2')['Goles2'].sum().head().values
        
        elif condicion == 'TOTAL':
            local = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo)].groupby('Equipo1')['Goles1'].sum().head().values
            visita = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo)].groupby('Equipo2')['Goles2'].sum().head().values
            golesT = local + visita
        
        if len(golesT) == 0:
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        
        else:
            show = "Los goles anotados del equipo {} en {} del la temporada {}-{} fueron {}".format(equipo,condicion,año1,año2, golesT) + "\n"
            print(show)
            return show

    def tablaTemp(self,año1,año2,nombre):
        arregloDePuntos = []
        arregloEquiposAnalizados = []
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]
        
        datos = pd.DataFrame(df, columns = ['Temporada','Equipo1', 'Equipo2', 'Goles1', 'Goles2']) #Columnas a mostrar
        
        # Obtiene el arreglo de temporada
        arregloEquipos = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2))].values 
        
        if len(arregloEquipos) == 0:
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        else:

            #Recorro por equipos para tener la lista de equipos
            for equipo in arregloEquipos:

                if equipo[1] in arregloEquiposAnalizados: #Si está paso, si no entonces lo agrego al arreglo
                    pass
                else: arregloEquiposAnalizados.append(equipo[1])  

            #Una vez teniendo el arreglo de equipos que jugaron se procede a buscar en el csv y validar puntos
            for equipo_1 in arregloEquiposAnalizados:

                # Obtiene el arreglo con los datos donde el equipo fue local
                aux = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo_1)].values
                
                #Teniendo el arreglo local completo entonces se recorre para la verificacion de puntos
                contadorPuntos = 0
        
                for golL in aux:
        
                    gol1 = golL[3] #Se obtienen los goles -> gol1 es goles del equipo analizado
                    gol2 = golL[4]

                    #Pasando a int:
                    g1 = int(gol1)
                    g2 = int(gol2)

                    if g1 > g2: #Si ganó
                        contadorPuntos+=3
                    elif g1 == g2: #Si empató
                        contadorPuntos+=1

                #Ahora con el arreglo de visitante
                aux = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo_1)].values

                #Teniendo el arreglo visitante completo entonces se recorre para la verificacion de puntos
                for golV in aux:

                    gol1 = golV[3] 
                    gol2 = golV[4] #Se obtienen los goles -> gol2 es goles del equipo analizado

                    #Pasando a int:
                    g1 = int(gol1)
                    g2 = int(gol2)

                    if g2 > g1: #Si ganó
                        contadorPuntos+=3
                    elif g2 == g1: #Si empató
                        contadorPuntos+=1
                
                arregloDePuntos.append(contadorPuntos) #Se agregan los puntos obtenidos por el equipo

                #----- Aquí termina la ejecución de 1 equipo, regresa para el siguiente y el proceso continua

            #print(arregloEquiposAnalizados)
            #print(arregloDePuntos)
            
            #Se espera obtener 2 arreglos, equipos y puntos, cada indice corresponde a equipo y puntos respectivos

            #Generacion del html:
            reporte_J = open(nombre, 'w')

            html_parte1 = '''
            <body style="background-color:#F4F8F4;">
            <h2 style="text-align: center;">"Tabla de temporada"</h2>
            <table style="width: 50%; border-collapse: collapse; border-style: solid; margin: 0 auto;" border="1">
            <tbody>
            <tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Equipo</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Puntos</span></strong></td>
            </tr>'''

            html_parte2 = ''
     
            for i in range(len(arregloEquiposAnalizados)): #Como debería tener la misma longitud los equipos y puntos se elige cualquiera
                v_equipo = arregloEquiposAnalizados[i]
                v_puntos   = arregloDePuntos[i]

                html_parte2 += '''<tr>
            <td style="width: 2%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            </tr>'''.format(v_equipo,v_puntos)
                
            hmtl_fin = '''
            </tbody>
            </table> </body>'''

            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte_J.write(html_archivo)
            reporte_J.close()

            print('Reporte creado con éxito')
            webbrowser.open_new_tab(nombre)

            show = "Generando archivo de clasificación de temporada {} - {}".format(año1,año2) + "\n"
            print(show)
            return show

    def tempEquipo(self,equipo,año1,año2,archivo,inicio,fin):
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]

        #Convertir a int 
        first = int(inicio)
        last = int(fin)

        datos = pd.DataFrame(df, columns = ['Temporada','Jornada','Equipo1', 'Equipo2', 'Goles1', 'Goles2'])

        #Valores por defecto --> Se incluyen todas las jornadas
        if first == 0 and last == 0: 

            #Arreglo completo de temporada de un equipo: local y visitante
            res1 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo)].values
        
            res2 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo)].values

        elif first == 0 and last > 0: #Inicia desde primer jornada hasta el rango indicado

            res1 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].le(last)) & (datos['Equipo1'] == equipo)].values
        
            res2 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].le(last)) & (datos['Equipo2'] == equipo)].values

        elif first > 0 and last == 0: #Inicia en el rango y llega hasta el final

            res1 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].ge(first)) & (datos['Equipo1'] == equipo)].values
        
            res2 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].ge(first)) & (datos['Equipo2'] == equipo)].values

        elif first > 0 and last > 0: #Si viene el rango completo

            res1 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].ge(first) & datos['Jornada'].le(last)) & (datos['Equipo1'] == equipo)].values
        
            res2 = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'].ge(first) & datos['Jornada'].le(last)) & (datos['Equipo2'] == equipo)].values


        if len(res1) == 0: #Verificacion de datos existentes
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        
        else:
            
            #Generar HTML
            reporte_Partidos = open(archivo, 'w')

            html_parte1 = '''
            <body style="background-color:#F4F8F4;">
            <h2 style="text-align: center;">"Reporte de jornada"</h2>
            <table style="width: 50%; border-collapse: collapse; border-style: solid; margin: 0 auto;" border="1">
            <tbody>
            <tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Temporada</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Jornada</span></strong></td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Equipo 1</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Equipo 2</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Goles 1</span></strong></td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Goles 2</span></strong></td>
            </tr>'''

            html_parte2 = ''
     
            for i in res1:
                v_Temporada = i[0]
                v_Jornada   = i[1]
                v_Equipo1   = i[2]
                v_Equipo2   = i[3]
                v_Goles1    = i[4]
                v_Goles2    = i[5]

                html_parte2 += '''<tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4ite;">{}</td>
            <td style="width: 2%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            </tr>'''.format(v_Temporada,v_Jornada,v_Equipo1,v_Equipo2,v_Goles1,v_Goles2)

            for i in res2:
                v_Temporada = i[0]
                v_Jornada   = i[1]
                v_Equipo1   = i[2]
                v_Equipo2   = i[3]
                v_Goles1    = i[4]
                v_Goles2    = i[5]

                html_parte2 += '''<tr>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 5%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4ite;">{}</td>
            <td style="width: 2%; text-align: left; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            <td style="width: 2%; text-align: center; border-style: solid; border-color: black; background-color: #F4F8F4;">{}</td>
            </tr>'''.format(v_Temporada,v_Jornada,v_Equipo1,v_Equipo2,v_Goles1,v_Goles2)
                

            hmtl_fin = '''
            </tbody>
            </table> </body>'''

            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte_Partidos.write(html_archivo)
            reporte_Partidos.close()

            print('Reporte creado con éxito')
            webbrowser.open_new_tab(archivo)

            show = "Generando archivos de resultados de temporada {} - {} del equipo {}".format(año1,año2,equipo) + "\n"
            print(show)
            return show

    def topCSV(self,condicion, año1,año2,num):
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv" #Ruta
        df = pd.read_csv(path) #Lectura
        
        df.values [0][0]

        bandera = int(num)

        datos = pd.DataFrame(df, columns=["Temporada", "Equipo1", "Equipo2", "Goles1", "Goles2"])

        #Calculo de puntos --------- Estructura similar a la parte de Tabla temporada...
        arregloDePuntos = []
        arregloEquiposAnalizados = []
       
        # Obtiene el arreglo de temporada
        arregloEquipos = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2))].values 
        #print(arregloEquipos)
        if len(arregloEquipos) == 0:
            print("No se encontró en la base de datos")
            show = "No se encontró en la base de datos" + "\n"
            return show
        else:

            #Recorro por equipos para tener la lista de equipos
            for equipo in arregloEquipos:

                if equipo[1] in arregloEquiposAnalizados: #Si está paso, si no entonces lo agrego al arreglo
                    pass
                else: arregloEquiposAnalizados.append(equipo[1])  

            #Una vez teniendo el arreglo de equipos que jugaron se procede a buscar en el csv y validar puntos
            for equipo_1 in arregloEquiposAnalizados:

                # Obtiene el arreglo con los datos donde el equipo fue local
                aux = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo_1)].values
                
                #Teniendo el arreglo local completo entonces se recorre para la verificacion de puntos
                contadorPuntos = 0
        
                for golL in aux:
        
                    gol1 = golL[3] #Se obtienen los goles -> gol1 es goles del equipo analizado
                    gol2 = golL[4]

                    #Pasando a int:
                    g1 = int(gol1)
                    g2 = int(gol2)

                    if g1 > g2: #Si ganó
                        contadorPuntos+=3
                    elif g1 == g2: #Si empató
                        contadorPuntos+=1

                #Ahora con el arreglo de visitante
                aux = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo_1)].values

                #Teniendo el arreglo visitante completo entonces se recorre para la verificacion de puntos
                for golV in aux:

                    gol1 = golV[3] 
                    gol2 = golV[4] #Se obtienen los goles -> gol2 es goles del equipo analizado

                    #Pasando a int:
                    g1 = int(gol1)
                    g2 = int(gol2)

                    if g2 > g1: #Si ganó
                        contadorPuntos+=3
                    elif g2 == g1: #Si empató
                        contadorPuntos+=1
                
                arregloDePuntos.append(contadorPuntos) #Se agregan los puntos obtenidos por el equipo
            
            #Ahora el ordenamiento por defecto mayor a menor
            #Método de burbuja
            for i in range(1,len(arregloDePuntos)):
                for j in range(0,len(arregloDePuntos)-i):
                    if(arregloDePuntos[j+1] > arregloDePuntos[j]):
                        aux1 = arregloDePuntos[j]
                        aux2 = arregloEquiposAnalizados[j]

                        arregloDePuntos[j]=arregloDePuntos[j+1]
                        arregloDePuntos[j+1]=aux1

                        arregloEquiposAnalizados[j]=arregloEquiposAnalizados[j+1]
                        arregloEquiposAnalizados[j+1]=aux2

            #Mostrado de datos según bandera y condición
            if condicion == "SUPERIOR":

                if bandera > len(arregloEquiposAnalizados):
                    bandera = len(arregloEquiposAnalizados)
                
                texto = "El top superior de la temporada {}-{} fue:\n".format(año1,año2)

                #Iteracion de datos a mostrar
                for i in range(bandera):
                    texto+= "{}.{} \n".format(i+1,arregloEquiposAnalizados[i])
                return texto
            
            elif condicion == "INFERIOR":
                
                if bandera > len(arregloEquiposAnalizados):
                    bandera = len(arregloEquiposAnalizados)
                
                texto = "El top inferior de la temporada {}-{} fue:\n".format(año1,año2)

                #Iteracion de datos a mostrar
                contador = 0
                for item in reversed(arregloEquiposAnalizados):

                    if contador > bandera:
                        break
                    else:
                        texto+= "{}.{} \n".format(contador+1,item)
                        contador+=1
                        
                return texto




        