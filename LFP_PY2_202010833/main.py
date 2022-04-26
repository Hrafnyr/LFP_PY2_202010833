
import os as documento
from listas import lista
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as stxt
from tkinter import filedialog
from tkinter import messagebox as MessageBox
import webbrowser
import pandas as pd

data = lista()

def obtenerCSV():
    path = documento.path.dirname(documento.path.abspath(__file__))+ "\LaLigaBot.csv"

    df = pd.read_csv(path)
    print (df.values)
    
def mostrarDatos():
    #txt.delete("1.0", "end")

    texto = cajaEnvio.get() + "\n" #Obtiene el dato de envío
   
    txt.config(state='normal') #Habilita la edicion del scrolledtext
    txt.tag_configure("tag_name", justify='right')
    txt.insert(INSERT,texto) #insertar texto en el scrolledtext
    txt.tag_add("tag_name", "1.0", "end") #Alineación a la izquierda
    txt.config(state=DISABLED) #Modo lectura del scrolledtext
    
    cajaEnvio.delete(0,tk.END) # Limpia la caja de envío
    
    #data.botonEvento(texto)
    
    return texto

def analizarTexto():  #Analizador léxico
    #data.botonEvento(t)
    t = cajaEnvio.get() + " "
    mostrarDatos()
    fila = 1
    columna = 1
    x = 0   #Indice
    estado = 0 #Estado inicial
    lexema = ""
    contadorDigitos = 0 #----> número: 2, año: 4
   
    while x < len(t):
        if estado == 0:
            if t[x] == " ": #No se analiza espacio
                x+=1
                columna +=1
            elif t[x] == "\n": #No se analiza salto de línea 
                columna =1
                fila+=1
                x+=1
            elif t[x] == "\t": #No se analiza tabulación
                x+=1
                columna +=8
            elif t[x].isalpha(): #Si viene una letra se va al estado 1
                lexema = ""
                lexema+= t[x]
                x+=1
                estado = 1
                columna +=1
            elif t[x] == "<" or t[x]==">" or t[x]=="-": #Si viene un símbolo se va al estado 2
                lexema = t[x]
                estado = 2
            elif t[x] == "\"": #Si vienen comillas dobles  se va al estado 3
                columna +=1
                lexema=""
                x+=1
                estado = 3
            
            elif t[x].isdigit(): #Si viene un dígito se va al estado 4
                lexema = t[x]
                columna+=1
                x+=1
                contadorDigitos+=1
                estado = 4
            else:
                data.insertError(t[x],"Caracter desconocido, error léxico",fila,columna)
                columna +=1
                x+=1
                estado = 0  
        
        elif estado == 1: #Termina de concatenar los caracteres de tipo alfabeto y guarda tokens de palabra reservada o ID
            if t[x].isalpha() or t[x]=="_" or t[x].isdigit():
                lexema+= t[x]
                x+=1
                columna +=1         
                estado = 1
            else:
                inicio = columna-len(lexema) 
                verificaPalabrasReservadas(lexema,fila,inicio)
                estado=0

        elif estado == 2: #Estado de símbolos
            if t[x] == "<":
                lexema=t[x]
                data.insertarToken("tk_Smayor",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]==">":
                lexema=t[x]
                data.insertarToken("tk_Smenor",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]=="-":
                lexema=t[x]
                data.insertarToken("tk_guion",lexema,fila,columna)
                x+=1
                columna +=1          
                estado = 2
            elif t[x]== "f" or t[x]== "j" or t[x]== "i" or t[x]== "n":
                lexema+=t[x]
                x+=1
                columna +=1          
                estado = 2
            else:
                inicio = columna - len(lexema)
                if lexema == "-f" or lexema == "-ji" or lexema == "-jf" or lexema == "-n":
                    label = "tk_{}".format(lexema)
                    data.insertarToken(label,lexema,fila,inicio) 
                estado = 0

        elif estado == 3: #Estado para cadenas  " "
            if  t[x] != "\"":
                lexema+=t[x]
                x+=1
                columna +=1
                estado = 3       
            else:
                inicio = columna - len(lexema)   
                data.insertarToken("tk_cadena",lexema,fila,inicio)
                x+=1
                columna +=1
                estado = 0
        
        elif estado == 4: #Estado para dígitos
           
            if  t[x].isdigit():
                lexema+=t[x]
                columna +=1
                x+=1
                contadorDigitos+=1
                estado = 4
            else:
                inicio = columna - len(lexema)
                if contadorDigitos == 4:
                    data.insertarToken("tk_año",lexema,fila,inicio)
                elif contadorDigitos > 0 and contadorDigitos <= 2:
                    data.insertarToken("tk_num",lexema,fila,inicio)            
                else:
                    data.insertarToken("tk_digito",lexema,fila,inicio)
                
                contadorDigitos = 0
                estado = 0

    print('Errores:')
    data.mostrarErrores()

    print('Tokens:')
    data.mostrarTokens()

def verificaPalabrasReservadas(lexema,fila,columna): #Método que verifica las palabras reservadas
    palabras_Reservadas = ["RESULTADO", "VS","TEMPORADA", "JORNADA","-f","GOLES","LOCAL","VISITANTE","TOTAL","TABLA","PARTIDOS", "-ji", "-jf","TOP","SUPERIOR","INFERIOR","-n","ADIOS"]
    encontrado = False
    for x in palabras_Reservadas:
        if x == lexema:
            label = "tk_{}".format(x.lower())
            data.insertarToken(label,lexema,fila,columna)
            encontrado = True
         
    if encontrado == False:
        data.insertarToken("tk_id",lexema,fila,columna)

def verReportes():
    op = ""
    if op =="Manual de usuario":
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\Documentación\Manual de Usuario.pdf"
        webbrowser.open_new(path)
    elif op =="Manual técnico":
        path = documento.path.dirname(documento.path.abspath(__file__))+ "\Documentación\Manual Técnico.pdf"
        webbrowser.open_new(path)
    else:
        print('NONE')
    
def verHtml():
    t = True
    if t:
        data.crearHtml()

#------------------------------Interfaz gráfica-------------------------------------

root = tk.Tk()                 #Raiz           
#Configuración Raiz
root.title('La Liga Bot')      
root.geometry('1050x675')
root.resizable(0,0)
root.config(bg="#87F7EC")  
root.eval('tk::PlaceWindow . center')

#Botón 1
# botonCargar = tk.Button(text="Cargar archivo", command=abrirDocumentoForm)
# botonCargar.place(x=25, y=20)
# botonCargar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=15)

#---------------------------- Botones menú -----------------------------------------
#Botón 1
botonReporteErrores = tk.Button(text="Reporte de errores", command=data.reporteErrores)
botonReporteErrores.place(x=780, y=25)
botonReporteErrores.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 1
botonLimpiarErrores = tk.Button(text="Limpiar log de errores",command=data.limpiarLogErrores)
botonLimpiarErrores.place(x=780, y=65)
botonLimpiarErrores.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 3
botonReporteTokens = tk.Button(text="Reporte de Tokens",command=data.reporteTokens)
botonReporteTokens.place(x=780, y=105)
botonReporteTokens.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 4
botonLimpiarTokens = tk.Button(text="Limpiar log de tokens",command=data.limpiarLogTokens)
botonLimpiarTokens.place(x=780, y=145)
botonLimpiarTokens.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 5
botonManualUsuario = tk.Button(text="Manual de Usuario")
botonManualUsuario.place(x=780, y=185)
botonManualUsuario.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 6
botonManualtecnico = tk.Button(text="Manual Técnico")
botonManualtecnico.place(x=780, y=225)
botonManualtecnico.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 7
botonSalir = tk.Button(text="Salir",command=exit)
botonSalir.place(x=780, y=265)
botonSalir.config(font=("Courier", 12), bg="#0A1246",fg="white",width=23)

#Botón 8
botonEnviar = tk.Button(text="Enviar", command=analizarTexto) 
botonEnviar.place(x=765, y=600)
botonEnviar.config(font=("Courier", 8), bg="#0A1246",fg="white",width=10)

#------------------------- Area de texto ----------------------------------------
txt = stxt.ScrolledText(root,width=90, height=35)
txt.place(x=15, y=25)

cajaEnvio = ttk.Entry(width=120)
cajaEnvio.place(x=15, y=600)

#Visualización
root.mainloop()

