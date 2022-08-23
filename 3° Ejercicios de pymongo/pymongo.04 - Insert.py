import connection as net

db = net.client.test

mydb = net.client["mydatabase"] 
#Seleccionamos la base de datos

mycol = mydb["customers"]
#Seleccionamos la colección


mydict = { "name": "Manuel", "address": "San Salvador" }
#Generamos el dicciónario de Python para ingresarlo

x = mycol.insert_one(mydict)
#Insertamos el primer registro

print(x.inserted_id)
#Nos devolverá el ID del documento ingresado