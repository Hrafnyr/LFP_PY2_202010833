
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
    
