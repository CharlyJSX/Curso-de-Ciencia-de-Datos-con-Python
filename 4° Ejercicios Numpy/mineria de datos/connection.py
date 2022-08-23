import pymongo

url = "mongodb+srv://DBjoscal:DBjoscal@joscalcluster.yziyn.mongodb.net/test"
client = pymongo.MongoClient(url)

#Usuario con privilegios de lectura y escritura
#Este páso es importante desde Atlas para poder usar comandos de Manipulación de la información 