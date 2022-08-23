#For para manejo de Listas 
fruits = ["apple", "banana", "cherry"]
for value in fruits:
  print("1 - Lista -", value)

#For para manejo de Tuples 
fruits = ("apple", "banana", "cherry")
for value in fruits:
  print("2 - Tuples -",value)  

#For para manejo de Sets 
fruits = {"apple", "banana", "cherry"}
for value in fruits:
  print("3 - Set -",value)    

#For para manejo de Dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for value in thisdict:
  print("4 - Diccionary -", value, " - ", thisdict[value])      