import pymongo
import os

client = pymongo.MongoClient("mongodb+srv://BaseDeMongo:BaseDeMongo@cluster0.igwlv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
db = client.test

mydb = client["Evaluacion01"] 
mycol = mydb["CE"]

while True: #Generamos el Ciclo repetitivo para el menu
    
    os.system("cls") #Limpieza de pantalla
    print("Menu:")
    print("1. Añadir un registro")
    print("2. Ver los registros")
    print("3. Actualizar un registro")
    print("4. Eliminar un registro")
    print("5. Salir")

    opcion = input("Ingrese su opción: ") #Capturamos Opción
    
    if opcion == "1":
        
        id = input("Digite el ID del Centro Escolar: ") #Capurtamos el id
        Nombre = input("Digite el Nombre del Centro Escolar: ") #Capturamos el Nombre
        Departamento = input("Digite el departamento del Centro Escolar: ") #Capturamos el departamento del CE
        Municipio = input("Digite el municipio del Centro Escolar: ") #Capturamos el munipio del CE

        mydict = { "_id": id, "Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio } #Creamos diccionario
        x = mycol.insert_one(mydict) #Lo ingresamos a la base
        input()

    elif opcion == "2":
        for x in mycol.find(): #Ciclo repetitivo para imprimir todos los registros
            print(x)    
        input()

    elif opcion == "3":
        for x in mycol.find():
            print(x)                 
        
        antiguoid = input("Digite el ID del Centro Escolar: ") 
        myquery = { "_id": antiguoid }
        nuevoid = input("Digite el nuevo ID del Centro Escolar: ") 
        newvalues = { "$set": { "_id": nuevoid } }
        mydoc = mycol.update_one(myquery, newvalues)

        print("ID actualizado correctamente")
        input()
    
     
    elif opcion == "4":
        
        eliminar_id = input("Digite el ID del Centro Escolar que desea eliminar: ") #Capurtamos el id
        myquery = { "_id": eliminar_id }
        mydoc = mycol.delete_one(myquery)
        input()
        #Ejecutamos la función para eliminar la primera concordancia
            

    elif opcion == "5":
        print("Saliendo del Sistema")
        input()
        break  #saliendo del ciclo repetitivo

    else:
        print("Opción incorrecta")
        input()
        continue     #Continuando el ciclo repetitivo

 

