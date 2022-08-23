import connection as net

db = net.client.test

mydb = net.client["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one() 
print(x)
#Ver el primer registro que aparezca

print()
for x in mycol.find(): 
  print(x)
#Mostrará todos los documentos del Cluster

print()
for x in mycol.find({},{"_id": 0, "name": 1}): 
  print(x)
# Mostrar los nombres

print()
myquery = {"address":"San Salvador"}  
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
# Mostrar los documentos que en address diga San Salvador

print()
myquery = { "address": { "$gt": "S" } } 
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#Mostrar los documentos donde address inicie con S