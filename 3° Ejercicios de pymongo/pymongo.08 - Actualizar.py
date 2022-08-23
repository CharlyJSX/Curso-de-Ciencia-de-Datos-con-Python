import connection as net

db = net.client.test

mydb = net.client["mydatabase"]
mycol = mydb["customers"]
#Seleccionamos la base de datos y la colección

myquery = { "name": "Manuel" }  
#Coloca los campos y el valor que debe de tener el documento para actualizar

mydoc = mycol.delete_one(myquery)
#Ejecutamos la función para actualizar la primera concordancia

