import connection as net
import os

db = net.client.test

mydb = net.client["mydatabase"]
mycol = mydb["customers"]
#conectamos con la base de datos y con la coleccións
#input() lo utilicé para hacer pausas y avanzar cuando se presione el teclado

while True: #Generamos el Ciclo repetitivo para el menu
    
    os.system("cls") #Limpieza de pantalla
    print("Menu:")
    print("1. Añadir un registro")
    print("2. Ver los registro")
    print("3. Salir")

    opcion = input("Ingrese su opción: ") #Capturamos Opción
    
    if opcion == "1":
        Nombre = input("Digite el Nombre del Clientes: ") #Capturamos el Nombre
        Direccion = input("Digite la dirección: ") #Capturamos el Dirección

        mydict = { "name": Nombre, "address": Direccion } #Creamos diccionario
        x = mycol.insert_one(mydict) #Lo ingresamos a la base
        input()

    elif opcion == "2":
        for x in mycol.find(): #Ciclo repetitivo para imprimir todos los registros
            print(x)    
        input()

    elif opcion == "3":
        print("Saliendo del Sistema")
        input()
        break  #saliendo del ciclo repetitivo

    else:
        print("Opción incorrecta")
        input()
        continue     #Continuando el ciclo repetitivo

 