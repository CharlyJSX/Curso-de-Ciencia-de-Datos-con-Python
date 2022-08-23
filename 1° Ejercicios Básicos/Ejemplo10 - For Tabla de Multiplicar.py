print("Ingrese un numero:")
numero = int(input())

for x in range(1, (numero+1)): 
    
    print("\nTabla del ", x)
    for y in range(1, 11):     
        print(x, " x ", y, " = ", (x*y))

else:
  print("Finally finished!")