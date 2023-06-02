
import os
import json


#VALIDAR FECHA
def validar_fecha(fecha):
    #Verifica que el ususario ingresa una fecha valida 
    from datetime import datetime
    while True:
            fecha_str = input(fecha)
            try:
                fecha = datetime.strptime(fecha_str, '%Y/%m/%d').strftime('%Y/%m/%d')
                return fecha
            except ValueError:
                print("No ha ingresado una fecha correcta...")
            else:
                break
    
#VALIDAR NOMBRE
def validacion_nombreC(tex):        

    while True:
        val = []
        x = input(tex)
        lista = x.split(" ")
        for i in lista:
            c = i.isalpha()
            if c == False:
                val.append(1)

        if len(val) == 0:
            
            return x
        else:
            print("Valor invalido, ingrese solo texto, vuelva a intentarlo!")
           
            continue

#VALIDAR ENTERO
def validacionInt(num):
    while True:
        try:
            x= int(input(num))
            return x
        except ValueError:
            print("Valor invalido, ingrese solo numeros enteros, vuelva a intentarlo!")



#VALIDAR CONTRASEÑA
def validacioncontraseña(contra):
    while True:
        try:
            x= int(input(contra))
            if (len(str(x))==4):
                return x
            print("Valor invalido, vuelva a intentarlo!!!!!")
            #print(len(str(x)))
            
        except ValueError:
            print("Valor invalido, vuelva a intentarlo!")


#Valida flotantes
def validacionflo(num):
    while True:
        try:
            x = float(input(num))
            return x
        except ValueError:
            print("Valor invalido, ingrese solo numeros decimales, vuelva a intentarlo!")
            continue

def mostrar_distribuidores():
    print('''Distribuidores:
    101 - Jorge Andrés Camacho.
    203 - María Camila Arias Restrepo.
    345 - Laura Constanza Duque Marín.
    421 - Isabel Cristina Romero Muñoz.
    500 - Juan Camilo Hoyos Diaz''')

def mostrar_ubicaciones():
    print('''Ubicaciones:
    1234 - Hospital San Vicente
    1203 - Hospital Pablo Tobón Uribe
    5588 - Hospital Alma Mater de Antioquia 
    7800 - Clínica del Norte''')