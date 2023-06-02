#Ana Maria Zapata
#Carlos Daniel Solano
#12:13 pm

import Funciones as fu
import mysql.connector

# Establecer la conexión a la base de datos
cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
cursor = cnx.cursor()

# Consulta SQL para crear la tabla Medicamentos
sql1 = '''CREATE TABLE IF NOT EXISTS  Medicamentos(
   Lote CHAR(20),
   Nombre CHAR(20),
   Distribuidor CHAR(20),
   `Cantidad de bodega` INT,
   `Fecha de llegada` CHAR(20),
   `Precio de venta` FLOAT
)'''

# Consulta SQL para crear la tabla Proveedores
sql2 = '''CREATE TABLE IF NOT EXISTS Proveedores(
   Codigo INT,
   Nombre CHAR(20),
   Apellido CHAR(20),
   Documento INT,
   Entidad CHAR(20)
)'''

# Consulta SQL para crear la tabla Ubicaciones
sql3 = '''CREATE TABLE IF NOT EXISTS  Ubicaciones(
   Codigo CHAR(20),
   `Nombre de la ubicacion` CHAR(20),
   Telefono INT
)'''

# Consulta SQL para crear la tabla Usuarios
sql4 = '''CREATE TABLE IF NOT EXISTS  Usuarios(
   user CHAR(20),
   password CHAR(20),
   permisos CHAR(20)
)'''

# Ejecutartamos las consultas SQL
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)

#Confirmarmamos los cambios en la base de datos
cnx.commit()

#Cerramos el cursor y la conexión
cursor.close()
cnx.close()

while True:
    print('\nBienvenidos a FARMACOS\n')




#Realizamos nuevamente la conexion a la base de datos.
    cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
    cursor = cnx.cursor() #esto es para poder manipular en la base de datos.

    
    while True:
        user = fu.validacion_nombreC('Ingresar usuario:')
        psswd = fu.validacionInt('Ingresar contraseña:')

        update = f"SELECT * FROM Usuarios WHERE user LIKE '{user}' AND password LIKE '{psswd}'"
        cursor.execute(update)
        results = cursor.fetchall()
    
        if results != []: #Validacion de usuario
            print('\nInicio de sesion correcto!')
            print('Bienvenido:',results[0][0])


            while True:
                menu_principal=int(input("""Menu:
    1 - Medicamentos.
    2 - Proveedores.
    3 - Ubicaciones.
    4 - Salir.
Ingrese la opcion que desea: """))
                
                #MENU MEDICAMENTOS 
                if menu_principal == 1:
                    print('Usted ha escogido (1): Medicamentos.\n')
                    while True:
                        menu_medicamentos=int(input("""Menu: 
    1 - Ingresar nuevo medicamento.
    2 - Actualizar informacion de  un medicamento.
    3 - Buscar medicamento.
    4 - Ver informacion de todos los medicamentos.
    5 - Eliminar un medicamento
    6- Volver al menu principal

Ingrese la opcion que desea: """))
                    
                        if menu_medicamentos == 1:
                            print('Usted ha escogido (1): Ingresar nuevo medicamento.\n')

                            # Realizamos nuevamente la conexión a la base de datos.
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor() # Esto es para poder manipular en la base de datos.

                            # Ingresamos los datos a guardar en la base de datos.
                            lote = fu.validacionInt('Ingresar numero de Lote: ')
                            Nombre_medicamento = fu.validacion_nombreC('Ingresar nombre del medicamento:')

                            fu.mostrar_distribuidores()

                            Distribuidor = fu.validacionInt('Ingresar distribuidor:')
                            cantidad_bodega = fu.validacionInt('Unidades en bodega: ')
                            Fecha_llegada = fu.validar_fecha('Ingrese fecha de llegada YYYY/MM/DD: ') # Corregido: utilizamos la función fu.validacion_fecha en lugar de fu.validar_fecha
                            precio_venta = fu.validacionflo('Precio de venta: $')

                            # Aquí le decimos la forma en la que vamos a guardar los inputs
                            insertar_sql = '''INSERT INTO Medicamentos (
                                Lote, 
                                Nombre, 
                                Distribuidor, 
                                `Cantidad de bodega`, 
                                `Fecha de llegada`, 
                                `Precio de venta`)
                                VALUES (%s, %s, %s, %s, %s, %s)'''

                            # Metemos los inputs en una tupla 
                            values = (str(lote), Nombre_medicamento, Distribuidor, str(cantidad_bodega), Fecha_llegada, str(precio_venta))

                            # Ejecutamos la opción cursor he insertamos los inputs
                            cursor.execute(insertar_sql, values) 

                            # Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerramos el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            print('\nMedicamento cargado exitosamente.\n')

                                                    
                        elif menu_medicamentos == 2:
                            print('Usted ha escogido (2): Actualizar informacion de  un medicamento.\n')
                            
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            # Obtener datos de entrada del usuario
                            lote_medicamento = input("Ingrese el lote del medicamento que desea actualizar: ")

                            update = f"SELECT * FROM Medicamentos WHERE Lote LIKE '{lote_medicamento}'"
                            cursor.execute(update)
                            results = cursor.fetchall()

                            for i in results:
                                print('Medicamento encontrado, ingrese los datos a actualizar')

                                nuevo_nombre = fu.validacion_nombreC('Ingresar nuevo nombre: ')
                                Nuevo_Distribuidor = fu.validacion_nombreC('Ingresar nuevo distribuidor: ')
                                Nueva_cantidad_bodega = fu.validacionInt('Nuevas unidades en bodega: ')
                                Nueva_Fecha_llegada = fu.validar_fecha('Ingrese nueva fecha de llegada YYYY/MM/DD: ')
                                Nuevo_precio_venta = fu.validacionflo('Nuevo precio de venta: $')

                                # Consulta SQL para actualizar información de un medicamento
                                sql = '''UPDATE Medicamentos
                                        SET Nombre = %s,
                                            Distribuidor = %s,
                                            `Cantidad de bodega` = %s,
                                            `Fecha de llegada` = %s,
                                            `Precio de venta` = %s
                                        WHERE Lote LIKE %s'''

                                # Valores a actualizar en la tabla Medicamentos
                                values = (nuevo_nombre, Nuevo_Distribuidor, str(Nueva_cantidad_bodega), Nueva_Fecha_llegada, str(Nuevo_precio_venta), lote_medicamento)

                                # Ejecutar la consulta SQL parametrizada con los valores
                                cursor.execute(sql, values)

                            # Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            print('Medicamento actualizado correctamente!')
                            #MELO
                        
                        elif menu_medicamentos == 3:
                            print('Usted ha escogido (3): Buscar un medicamento.\n')
                            
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            while True:
                                # Preguntamos el numero del lote
                                lote = fu.validacionInt('Ingresar número de Lote: ')

                                # Buscamos en la base de datos que esta
                                sql = "SELECT * FROM Medicamentos WHERE Lote = %s"
                                cursor.execute(sql, (lote,))
                                results = cursor.fetchall()
                                if results != []:
                                    # Imprimir encabezados de columnas
                                    columnas = [columna[0] for columna in cursor.description] #me entrega una lista con los nombres de las columnas
                                    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*columnas)) #Me imprime la lista anterior con espacios determinados

                                    for i in results: #Recorre cada fila de la tabla
                                        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*i)) #Imprime cada elemento de la fila con el mismo espacio de los nombres de las columnas


                                    break
                                else:
                                    print('Usuario no encontrado, intentelo de nuevo!\n')
                                    continue

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO

                        elif menu_medicamentos == 4:
                            print('Usted ha escogido (4): Ver informacion de todos los medicamentos.\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()
                            sql = "SELECT * FROM Medicamentos"

                            cursor.execute(sql)
                            results = cursor.fetchall()

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] #me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*columnas)) #Me imprime la lista anterior con espacios determinados

                            for i in results: #Recorre cada fila de la tabla
                                print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*i)) #Imprime cada elemento de la fila con el mismo espacio de los nombres de las columnas

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO
                        
                        elif menu_medicamentos == 5:
                            print('Usted ha escogido (5): Eliminar.\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            sql_seleccionar = "SELECT * FROM Medicamentos" # Consulta SQL para seleccionar todos los registros de la tabla Medicamentos

                            cursor.execute(sql_seleccionar) # Ejecuta la consulta de selección

                            results = cursor.fetchall() # Obtiene todos los resultados de la consulta

                            print("Medicamentos almacenados.")

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] #me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*columnas)) #Me imprime la lista anterior con espacios determinados

                            for i in results:
                                print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<10}".format(*i)) #imprimr bonitas las filas de la tabla

                            lote = fu.validacionInt('\nIngresar número de Lote a eliminar: ')# Solicitar número de lote para eliminar

                            sql_eliminar = f"DELETE FROM Medicamentos WHERE Lote = {lote}" # Consulta SQL para eliminar los registros con el número de lote especificado

                            cursor.execute(sql_eliminar)# Ejecuta la consulta de eliminación

                            # Actualizar, cerrar el cursor y la conexión
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                            print('Medicamento eliminado correctamente.')
                            #MELO
                
                        elif menu_medicamentos == 6:
                            print('Usted ha escogido (6): Volver al menu principal.\n')
                            break

                        else:
                            print('Opcion invalida, ingrese una opcion valida.\n')
                            continue
                        break
            
                #MENU PROVEEDORES
                elif menu_principal==2:
                    print('\nUsted ha escogido (2): Proveedores.\n')

                    while True:
                        menu_proveedores=int(input("""Menu: 
    1 - Ingresar nuevo proveedor.
    2 - Actualizar informacion de  un proveedor.
    3 - Buscar proveedor.
    4 - Ver informacion de todos los proveedores.
    5 - Eliminar la informacion de un proveedor.
    6 - Volver al menu principal.
Ingrese la opcion que desea: """))
                        
                        if menu_proveedores==1:
                            print('Usted ha escogido (1): Ingresar nuevo proveedor.\n')

                            #Realizamos nuevamente la conexion a la base de datos.
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor() #esto es para poder manipular en la base de datos.
                            
                            #Pedir info del provedor
                            codigo = fu.validacionInt('Ingresar codigo: ')
                            Nombre_proveedor = fu.validacion_nombreC('Ingresar nombre del proveedor: ')
                            apellido_proveedor = fu.validacion_nombreC('Ingresar apellido del proveedor: ')
                            id_proveedor = fu.validacionInt('Ingresar documento de ID: ')
                            entidad_proveedor = fu.validacion_nombreC('Entidad del proveedor: ')
                            

                            #aqui le decimos la forma en la que vamos a guardar los inputs
                            insertar_sql = '''INSERT INTO Proveedores (
                                Codigo ,
                                Nombre, 
                                Apellido, 
                                Documento, 
                                Entidad)
                                VALUES (%s, %s, %s, %s, %s)'''
                    
                            #metemos los inputs en una tupla 
                            values = (str(codigo),Nombre_proveedor, apellido_proveedor,str(id_proveedor),entidad_proveedor)

                            #ejecutamos la opcion cursor he insertamos los inputs
                            cursor.execute(insertar_sql,values) 

                            #Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerramos el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            print('\nProveedor cargado exitosamente.\n')
                            #MELO

                        elif menu_proveedores == 2:
                            print('Usted ha escogido (2): Actualizar informacion de  un proveedor.\n')

                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            # Obtener datos de entrada del usuario
                            documento_proveedor = fu.validacionInt('Ingrese el documento del proveedor que desea actualizar: ')  

                            update = f"SELECT * FROM Proveedores WHERE Documento LIKE '{documento_proveedor}'"
                            cursor.execute(update)
                            results = cursor.fetchall()

                            for i in results:
                                print('Proveedor encontrado, ingrese los datos a actualizar')

                                # Pedir información del proveedor
                                nuevo_codigo = fu.validacionInt('Ingresar código: ')
                                nuevo_nombre = fu.validacion_nombreC('Ingresar nombre: ')
                                nuevo_apellido = fu.validacion_nombreC('Ingresar apellido: ')
                                nuevo_entidad_proveedor = fu.validacion_nombreC('Entidad del proveedor: ')

                                # Consulta SQL para actualizar información del proveedor
                                sql = '''UPDATE Proveedores
                                        SET Codigo = %s,
                                            Nombre = %s,
                                            Apellido = %s,
                                            Entidad = %s
                                        WHERE Documento LIKE %s'''

                                # Valores a actualizar en la tabla Proveedores
                                values = (str(nuevo_codigo),nuevo_nombre, nuevo_apellido, nuevo_entidad_proveedor,documento_proveedor)

                                # Ejecutar la consulta SQL parametrizada con los valores
                                cursor.execute(sql, values)

                            # Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()

                            print('Proveedor actualizado correctamente!')
                            #MELO
                            
                        elif menu_proveedores == 3:
                            print('Usted ha escogido (3): Buscar un proveedor.\n')

                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            while True:
                                # Obtener datos de entrada del usuario
                                documento_proveedor = fu.validacionInt('Ingrese el documento del proveedor que desea buscar: ')  

                                update = f"SELECT * FROM Proveedores WHERE Documento LIKE '{documento_proveedor}'"
                                cursor.execute(update)
                                results = cursor.fetchall()


                                if results != []:
                                    print('\nProveedor encontrado!\n')

                                    # Imprimir encabezados de columnas
                                    columnas = [columna[0] for columna in cursor.description] # Me entrega una lista con los nombres de las columnas
                                    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*columnas)) # Me imprime la lista anterior con espacios determinados

                                    for i in results:
                                        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*i)) # Imprimir filas de la tabla de manera formateada


                                    break
                                else:
                                    print('Proveedor no encontrado, intentelo de nuevo!\n')
                                    continue
                                
                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO

                        elif menu_proveedores == 4:
                            print('Usted ha escogido (4): Ver informacion de proveedores.\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()
                            sql = "SELECT * FROM Proveedores"

                            cursor.execute(sql)
                            results = cursor.fetchall()

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] #me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*columnas)) #Me imprime la lista anterior con espacios determinados

                            for i in results: #Recorre cada fila de la tabla
                                print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*i)) #Imprime cada elemento de la fila con el mismo espacio de los nombres de las columnas

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO

                        elif menu_proveedores == 5:
                            print('Usted ha escogido (5): Eliminar .\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            sql_seleccionar = "SELECT * FROM Proveedores" # Consulta SQL para seleccionar todos los registros de la tabla Proveedores

                            cursor.execute(sql_seleccionar) # Ejecuta la consulta de selección

                            results = cursor.fetchall() # Obtiene todos los resultados de la consulta

                            print("Proveedores almacenados.")

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] # Me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*columnas)) # Me imprime la lista anterior con espacios determinados

                            for i in results:
                                print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*i)) # Imprimir filas de la tabla de manera formateada

                            # Obtener datos de entrada del usuario
                            # Obtener datos de entrada del usuario
                            Documento_proveedor = fu.validacionInt('Ingrese el documento del proveedor que desea buscar: ')

                            # Consulta SQL para eliminar los registros con el documento especificado
                            sql_eliminar = f"DELETE FROM Proveedores WHERE Documento = {Documento_proveedor}"

                            cursor.execute(sql_eliminar) # Ejecutar la consulta de eliminación

                            # Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()

                            print('Proveedor eliminado correctamente.')
                            
                        elif menu_proveedores == 6:
                            print('Usted ha escogido (6): Volver al menu principal.\n')
                            break
                        else:
                            print('Ingrese una opcion valida.\n')
                            continue
                        break

                #MENU UBICACIONES 
                elif menu_principal==3:
                    print('\nUsted ha escogido (3): Ubicaciones.\n')

                    while True:
                        menu_ubicaciones=int(input("""Menu:
    1 - Ingresar nueva ubicación.
    2 - Actualizar información de  una ubicación.
    3 - Buscar una ubicación.
    4 - Ver informacion de todos las ubicaciónes.
    5 - Eliminar una ubicacion. 
    6 - Volver al menu principal.
Ingrese la opcion que desea: """))
                    
                        if menu_ubicaciones == 1:
                            print('Usted ha escogido (1): Ingresar nueva ubicación.\n')

                            # Realizamos nuevamente la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            codigo = fu.validacionInt('Ingresar codigo: ')
                            fu.mostrar_ubicaciones()
                            nombre_ubicacion = fu.validacion_nombreC('Ingresar nombre de la ubicacion: ')
                            telefono_ubicacion = fu.validacionInt('Ingresar telefono: ')

                            # Aquí le decimos la forma en la que vamos a guardar los inputs
                            insertar_sql = '''INSERT INTO Ubicaciones (
                                Codigo,
                                `Nombre de la ubicacion`, 
                                Telefono)
                                VALUES (%s, %s, %s)'''

                            # Metemos los inputs en una tupla 
                            values = (codigo, nombre_ubicacion, telefono_ubicacion)

                            # Ejecutamos la opción cursor e insertamos los inputs
                            cursor.execute(insertar_sql, values)

                            # Confirmar los cambios en la base de datos
                            cnx.commit()

                            # Cerramos el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            print('\nUbicación cargada exitosamente.\n')


                        elif menu_ubicaciones == 2:
                            print('Usted ha escogido (2): Actualizar informacion de  una ubicación.\n')


                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            # Obtener datos de entrada del usuario
                            codigo_ubicacion = fu.validacionInt('Ingresar codigo de la ubicacion: ')

                            update = f"SELECT * FROM Ubicaciones WHERE Codigo LIKE '{codigo_ubicacion}'"
                            cursor.execute(update)
                            results = cursor.fetchall()

                            for i in results:
                                print('Ubicacion encontrada, ingrese los datos a actualizar.')

                                nuevo_nombre_ubi = input('Ingresar nuevo nombre: ')
                                nuevo_telefono_ubicacion = fu.validacionInt('Ingresar nuevo telefono: ')

                                # Consulta SQL para actualizar información de un medicamento
                                sql = '''UPDATE Ubicaciones
                                        SET `Nombre de la ubicacion` = %s,
                                            telefono = %s
                                        WHERE Codigo LIKE %s'''


                                # Valores a actualizar en la tabla Medicamentos
                                values = (nuevo_nombre_ubi, str(nuevo_telefono_ubicacion),codigo_ubicacion)

                                # Ejecutar la consulta SQL parametrizada con los valores
                                cursor.execute(sql, values)

                                # Confirmar los cambios en la base de datos
                                cnx.commit()

                                # Cerrar el cursor y la conexión
                                cursor.close()
                                cnx.close()
                                print('Ubicacion actualizada correctamente!')
                                #MELO

                        elif menu_ubicaciones == 3:
                            print('Usted ha escogido (2): Buscar una ubicación\n')

                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            while True:
                                # Obtener datos de entrada del usuario
                                codigo_ubicacion = fu.validacionInt('Ingrese código de la ubicación: ')

                                # Consulta SQL para buscar la ubicación por código
                                sql_select = f"SELECT * FROM Ubicaciones WHERE Codigo = '{codigo_ubicacion}'"

                                cursor.execute(sql_select) # Ejecutar la consulta de selección
                                results = cursor.fetchall() # Obtener los resultados de la consulta

                                if results:
                                    # Imprimir encabezados de columnas
                                    columnas = [columna[0] for columna in cursor.description] # Me entrega una lista con los nombres de las columnas
                                    print("{:<10} {:<25} {:<10}".format(*columnas)) # Me imprime la lista anterior con espacios determinados

                                    for i in results:
                                        print("{:<10} {:<25} {:<10}".format(*i)) # Imprimir filas de la tabla de manera formateada


                                    break
                                else:
                                    print('Ubicacion no encontrada, intentelo de nuevo!\n')
                                    continue

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO

                        elif menu_ubicaciones == 4:
                            print('Usted ha escogido (4): Ver informacion de las ubicaciónes.\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()
                            sql = "SELECT * FROM Ubicaciones"

                            cursor.execute(sql)
                            results = cursor.fetchall()

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] #me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<25} {:<10}".format(*columnas)) #Me imprime la lista anterior con espacios determinados

                            for i in results: #Recorre cada fila de la tabla
                                print("{:<10} {:<25} {:<10}".format(*i)) #Imprime cada elemento de la fila con el mismo espacio de los nombres de las columnas

                            # Cerrar el cursor y la conexión
                            cursor.close()
                            cnx.close()
                            #MELO

                        elif menu_ubicaciones==5:
                            print('Usted ha escogido (5): Eliminar.\n')

                            # Establecer la conexión a la base de datos
                            cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
                            cursor = cnx.cursor()

                            sql_seleccionar = "SELECT * FROM Ubicaciones" # Consulta SQL para seleccionar todos los registros de la tabla Ubicaciones

                            cursor.execute(sql_seleccionar) # Ejecuta la consulta de selección

                            results = cursor.fetchall() # Obtiene todos los resultados de la consulta

                            print("Ubicaciones almacenadas.")

                            # Imprimir encabezados de columnas
                            columnas = [columna[0] for columna in cursor.description] # Me entrega una lista con los nombres de las columnas
                            print("{:<10} {:<25} {:<10}".format(*columnas)) # Me imprime la lista anterior con espacios determinados

                            for i in results:
                                print("{:<10} {:<25} {:<10}".format(*i)) # Imprimir filas de la tabla de manera formateada

                            # Obtener datos de entrada del usuario
                            codigo_ubicacion = fu.validacionInt('Ingresar codigo de la ubicacion: ')

                            sql_eliminar = f"DELETE FROM Ubicaciones WHERE Codigo LIKE '{codigo_ubicacion}'"
                            cursor.execute(sql_eliminar)
                            results = cursor.fetchall()

                            # Guardar,cerrar el cursor y la conexión
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                            print('Ubicacion eliminada correctamente.')
                            #MELO

                        elif menu_ubicaciones == 6:
                            print('Usted ha escogido (6): Volver al menu principal.\n')
                            break
                        else:
                            print('Ingrese una opcion valida.\n')
                            continue
                        break

                elif menu_principal == 4:
                    print('Usted ha escogido (4): Salir.')
                    break
                else:
                    print('Ingrese una opcion valida.')
                    continue
       
        # Cerrar el cursor y la conexión
        cursor.close()
        cnx.close()
        break
    break
#FIN DEL CODIGO

