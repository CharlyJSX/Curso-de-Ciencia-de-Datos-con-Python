def my_function(*tablas):  
  for x in tablas:      
      print("\nTabla del ", x)
      for y in range(1, 11):     
          print(x, " x ", y, " = ", (x*y))
  
  print(tablas)

my_function(3, 2, 5, 4, 5, 9, 10)