import Funciones as fu
import mysql.connector

print('Bienvenidos al registro de ususarios.')

while True:
    print('''Menu:
        1 - Agregar un usuario.
        2- Salir.''')
    menu = int(input('Que desea realizar: '))

    if menu == 1:
        #Realizamos nuevamente la conexion a la base de datos.
        cnx = mysql.connector.connect(user='informatica1', password='bio123', host='127.0.0.1', database='informatica1')
        cursor = cnx.cursor() #esto es para poder manipular en la base de datos.

        #Ingresamos los datos a guardar en la base da datos.
        user = fu.validacion_nombreC('Ingresar user: ')
        password = fu.validacioncontraseña('Ingresar password:')
        permiso = fu.validacion_nombreC('Ingresar permiso:')


        #aqui le decimos la forma en la que vamos a guardar los inputs
        insertar_sql = '''INSERT INTO Usuarios (
            user, 
            password, 
            permisos)
            VALUES (%s, %s, %s)'''

        #metemos los inputs en una tupla 
        values = (user,str(password),permiso)

        #ejecutamos la opcion cursor he insertamos los inputs
        cursor.execute(insertar_sql,values) 

        #Confirmar los cambios en la base de datos
        cnx.commit()

        # Cerramos el cursor y la conexión
        cursor.close()
        cnx.close()
        print('\nUsuario cargado exitosamente.\n')

    elif menu == 2:
        print('vuelva pronto.')
        break
    else:
        print('opcion invalida, vuelva a intentarlo.')
        continue
