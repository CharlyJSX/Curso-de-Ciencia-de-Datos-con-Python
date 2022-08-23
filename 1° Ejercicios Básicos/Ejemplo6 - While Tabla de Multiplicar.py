print("Ingrese un numero")
numero = int(input())
i = 1
while i <= numero :
  print("Tabla del: ", i)
  j = 1
  while j <= 10:
    print(i," x ", j, " = ", (i*j))
    j+=1
  i+=1