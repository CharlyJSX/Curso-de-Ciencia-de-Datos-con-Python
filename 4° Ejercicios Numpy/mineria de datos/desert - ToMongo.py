import connection as net
import quandl
import pandas as pd

db = net.client.test

mydb = net.client["mydatabase"] 
#Seleccionamos la base de datos

mycol = mydb["desert"]
#Seleccionamos la colección


# Observa que se usa pd.read_csv debido a que importamos a pandas como pd
df = pd.read_csv("data/surveys.csv")

df10 = df.head(100)

for i in df10.index: 
     print("Total income in ", df["sex"][i])

df10.reset_index(inplace=True)
data_dict = df10.to_dict("records")

# Insert collection
mycol.insert_many(data_dict)


