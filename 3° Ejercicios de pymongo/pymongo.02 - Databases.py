import connection as net

print(net.client.list_database_names()) 
#listamos las bases de datos disponibles en el Cluster

mydb1 = net.client["BaseDeMongo"]
print(mydb1)

# mydb1 se combertirá en un acceso directo a la base de datos mydatabase
# esta nos permitirá observar

#Importante, no se verá ningún cambio hasta que se ingrese o exista la base de datos

