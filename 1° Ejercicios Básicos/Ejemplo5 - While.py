i = 1  #Iniciación de la Variable

while i < 6 and i != 3:  #Evaluamos y recorremos el Ciclo si es Verdadera la Condición
  print(i)
  i += 1      #Incremento de la variable vinculada a la condición

print()

i = 0
while i < 10:

  i += 1

  if i == 6:
    break

  if (i%2) == 0:
    continue

  print(i)

print()

i = 1
while i < 6: 
  print(i) 
  i += 1

else: 
  print("i is no longer less than 6")