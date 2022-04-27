
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
            self.insertErrorS(label,"Se esperaba: RESULTADO,JORNADA,GOLES,TABLA, PARTIDOS, TOP O ADIOS",1,0)
        
        self.showError()

    #--> se espera tk_resultado
    def resultadoPartido(self):
        tk = self.quitarToken()
        if tk[0] == "tk_resultado":
            
            #---> se espera tk_cadena
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba una cadena",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_cadena":
               
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

                                            #---> se espera tk_Smayor
                                            tk = self.quitarToken()
                                            if tk is None:
                                                self.insertErrorS("Null","Se esperaba un >",11,0)
                                                return #Si no viene entonces ya no se ejecuta lo demás
                                            elif tk[0] == "tk_Smayor":
                                                
                                                #Funcionalidad a realizar
                                                print("todo correcto")   


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

        asignar_nombre = None

        tk = self.quitarToken()
        if tk[0] == "tk_jornada":
            
            #---> se espera tk_num
            tk = self.quitarToken()
            if tk is None:
                self.insertErrorS("Null","Se esperaba un número de 1 o 2 dígitos positivos",11,0)
                return #Si no viene entonces ya no se ejecuta lo demás
            
            elif tk[0] == "tk_num":
               
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
                                            print("Agregando nombre por defecto: jornada.html")
                                        else:
                                            print("El nombre de asignación es:", asignar_nombre)

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
        condicion = None

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

                                        #---> se espera tk_Smayor
                                        tk = self.quitarToken()
                                        if tk is None:
                                            self.insertErrorS("Null","Se esperaba un >",11,0)
                                            return #Si no viene entonces ya no se ejecuta lo demás
                                        elif tk[0] == "tk_Smayor":
                                            
                                            #Funcionalidad
                                            print("PROCESO CORRECTO")

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
                                        print("Agregando nombre por defecto: temporada.html")
                                    else:
                                        print("El nombre de asignación es:", asignar_nombre)

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
                                            print("Agregando nombre por defecto: partidos.html")
                                        else:
                                            print("El nombre de asignación es:", asignar_nombre)

                                        #Se espera ---> <RANGO1>
                                        #Se llama la función
                                        jornada_inicial = self.rango1()
                                        if jornada_inicial is None:
                                            print("Inicio por defecto: Primer elemento")
                                        else:
                                            print("Se iniciará en:", jornada_inicial)

                                        #Se espera ---> <RANGO2>
                                        #Se llama la función
                                        jornada_final = self.rango2()
                                        if jornada_final is None:
                                            print("Final por defecto: último elemento")
                                        else:
                                            print("Se terminará en:", jornada_final)

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
                
                #---> se espera -f
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
                                            print("valor por defecto: 5 equipos a mostrar")
                                        else:
                                            print("Equipos a mostrar:", bandera)

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
                        self.insertErrorS(label,"Se esperaba num",11,0)
                else: 
                    return None #Si no lo encuentra entonces devuelve None para simular el épsilon
            else:
                return None   

    #--> se espera tk_adios  
    def adios(self):
        tk = self.quitarToken()

        if tk[0] == "tk_adios":
            exit()



