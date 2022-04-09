
from guardarToken import token1
from errores import error
from tkinter import messagebox as MessageBox
import webbrowser


class lista():
    def __init__(self):
        self.listaTokens = [] #lista que guarda los tokens
        self.listaErrores = [] #lista que guarda los errores
    
    def insertarToken(self, token,valor,fila,columna):
        self.listaTokens.append(token1(token,valor,fila,columna))
    
    def insertError(self, caracter,tipo,fila,columna):
        self.listaErrores.append(error(caracter,tipo,fila,columna))
        
    def mostrarTokens(self): #Metodo de prueba para verificar el correcto guardado de los tokens
        i:token1
        for i in self.listaTokens:
            r =i.enviarTokens()
            print(r)

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

    def eliminarTodo(self):
        del self.listaErrores[:]
        del self.listaTokens[:]
    
    def reporteTokens(self):
        if len(self.listaTokens)==0:
            print('No hay información')
            MessageBox.showinfo('Atención','No se ha analizado el texto')
        else:
            print('-------------------> Generando reporte, espere...')
            contadorReportes = 1
            name = "Reporte"+str(contadorReportes)+"Tokens.html"
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
            contadorReportes+=1
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
    
    def crearHtml(self):
        contID = 1
        cabecera = '''
        <!DOCTYPE html>
        <html>
        <body style="background-color:#C9FBC9;">
        <form action="ejemplo.php" method="get" name="form1">
        <h1 style="text-align: center;"><strong>Formulario</strong></h1>'''

        htmlTxt = ""
        textoFrame = ""
        variablesFrame =""
        for i in range(len(self.listaTokens)): #Recorre tokens
            if self.listaTokens[i].getValor()=="<": #Abertura
                while self.listaTokens[i].getValor() !=">": #Guardará los datos dentro de <>
                    #print(self.listaTokens[i].getValor())
                    
                    if self.listaTokens[i].getValor() == "etiqueta": #Accede a etiqueta
                        e = i
                        while self.listaTokens[e].getValor() !=">": 
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''<br><br><label><strong>{}</strong></label>'''.format(self.listaTokens[e].getValor())
                                #print('valor etiqueta:',self.listaTokens[i].getValor())
                            e+=1
                    
                    elif self.listaTokens[i].getValor() == "texto": #Accede a texto
                        contador = 0
                        e = i
                        while self.listaTokens[e].getValor() !=">"and contador<1:
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt += '''<input type="text" id="txto{}" name="txt" value="{}" size="50" placeholder="{}">'''.format(contID,self.listaTokens[e].getValor(),self.listaTokens[e+4].getValor())
                                textoFrame+= '''var t{} = document.getElementById("txto{}").value;'''.format(contID,contID)
                                variablesFrame+= '''"Dato:"+t{}+"-"'''.format(contID)
                                contID+=1
                                contador=2
                            e+=1

                    elif self.listaTokens[i].getValor() == "grupo-radio": #Accede a grupo radio
                        e = i
                        while self.listaTokens[e].getValor() !=">": #Guardará los datos dentro de <>
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''  <p>{}</p>'''.format(self.listaTokens[e].getValor())
                            elif self.listaTokens[e].getToken() == "Token cadena simple":
                                htmlTxt+= '''<input type="radio" name="hm" value="h"> {}'''.format(self.listaTokens[e].getValor())
                                
                            textoFrame+= ''' var radiovalue=document.form1.hm.value;
    if(radiovalue.length==0) radiovalue="ninguno";'''
                            variablesFrame+= '''"Dato:"+radiovalie+"-"'''
                            e+=1

                    elif self.listaTokens[i].getValor() == "grupo-option": #Accede a grupo option
                        e = i
                        while self.listaTokens[e].getValor() !=">": #Guardará los datos dentro de <>
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''  <p>{}</p>'''.format(self.listaTokens[e].getValor())
                                htmlTxt+= '''<select name="select" id="s{}">'''.format(contID)
                            elif self.listaTokens[e].getToken() == "Token cadena simple":
                                htmlTxt+= '''<option value="value1">{}</option>'''.format(self.listaTokens[e].getValor())
                            
                            textoFrame += '''var combo = document.getElementById("s{}");
var selected = combo.options[combo.selectedIndex].text;'''.format(contID)
                            variablesFrame+= '''"Dato:"+combo+"-"'''
                            contID+=1
                            e+=1
                        htmlTxt+= ''';</select>'''
                    
                    elif self.listaTokens[i].getValor() == "botón" or self.listaTokens[i].getValor() == "boton": #Accede a grupo option
                        e = i
                        while self.listaTokens[e].getValor() !=">": #Guardará los datos dentro de <>
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                nameB =self.listaTokens[e].getValor()
                                
                            elif self.listaTokens[e].getValor() == "entrada":

                                f1 = '''
                                <script type="text/javascript">
                                        function funcionMostrar() {
                                            var ifrm = document.createElement('iframe');
                                            ifrm.src ="Entrada.html"
                                            ifrm.style.width = "640px";
                                            ifrm.style.height = "480px";
                                            document.body.appendChild(ifrm);
                                        }
                                    </script> '''
                                htmlTxt+= '''</form><p><button name="button" onclick="funcionMostrar()">{}</button></p>{}'''.format(nameB,f1)
                            elif self.listaTokens[e].getValor() == "info":
                                f2 = '''
                                <div id="div-element"></div>
                                <script type="text/javascript">
                                    function funcionInfor(){{
                                    {}
                                    document.getElementById("div-element").innerHTML = {}
                                    }}
                                    </script> '''.format(textoFrame,variablesFrame)
                                htmlTxt+= '''</form><p><button name="button" onclick="funcionInfor()">{}</button></p>{}'''.format(nameB,f2)
                            e+=1
                        
                            
                            
                    i+=1

        final ='''
        </body>
        </html>'''
        html = cabecera + htmlTxt +final

        name = "Formulario.html"
        reporte = open(name, 'w')
        reporte.write(html)
        reporte.close()
        print('Reporte creado con éxito')
        webbrowser.open_new_tab(name)

    def botonEvento(self, text):
        name = "Entrada.html"
        reporte = open(name, 'w')
        html_texto = '''<!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"/></head>
        <body style="background-color:#C9FBC9;">
        <h1 style="text-align: center;"><strong>Archivo de entrada</strong></h1>
        <p>{}</p>
        </body>
        </html>'''.format(text)
        reporte.write(html_texto)
        reporte.close()
            