import connection as net

db = net.client.test

mydb = net.client["mydatabase"] 
#Acceso a la DB mydatabase

mycol = mydb["customers"]
#Acceso a la colección de Customers

print(mycol)

#Importante, no se verá ningún cambio hasta que se ingrese o exista la base de datos