import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv('titanic.csv')


#input() lo utilicé para hacer pausas y avanzar cuando se presione el teclado

while True: #Generamos el Ciclo repetitivo para el menu
    
    os.system("cls") #Limpieza de pantalla
    print("Menu:")
    print("1. Información de un pasajero por ticket ")
    print("2. Ver Gráfica de pastel de personas que murieron y cuantas sobrevivieron ")
    print("3. Cantidad de sobrevivientes y fallecidos por clase ")
    print("4. Ticket más caro y más barato ")
    print("5. Salir ")

    opcion = input("Ingrese su opción: ") #Capturamos Opción
    
    if opcion == "1":
             
        Numero = input("Digite el número de ticket a buscar ")
        Busqueda = df[df['Ticket'] == Numero]
        print(Busqueda)   
        input()  
           
    elif opcion == "2":
        
        Muertos = df[df['Sobrevivió'] == 0]
        Vivos = df[df['Sobrevivió'] == 1]

        x = np.array([len(Muertos), len(Vivos)])
        mylabels = ["Muertos", "Sobrevivieron"]

        plt.pie(x, labels = mylabels,  autopct="%0.1f %%")
        plt.legend(title = "Sobrevivientes y fallecidos en el Titanic:")
        plt.show()
        input()

    elif opcion == "3":
        
        personas_vivas = df.Clase[df.Sobrevivió == 1].value_counts(sort = False)
        personas_muertas = df.Clase[df.Sobrevivió == 0].value_counts(sort = False)
        tipos = pd.unique(df.Clase)
        tipos = [str(Clase) for Clase in tipos]
        print(tipos)
        x = np.arange(len(tipos))
        plt.bar(x-0.2, personas_vivas, 0.40, color = "blue")
        plt.bar(x+0.2, personas_muertas, 0.40, color = "red")
        plt.xticks(x,tipos)
        plt.title("Sobrevivientes por Clase:")
        plt.xlabel("Clases")
        plt.ylabel("Personas")
        plt.legend(["Personas Vivas", "Personas Muertas"])
        plt.show()
        input()
        
    elif opcion == "4":
        
        Tarifa = df[df['Tarifa'].notnull() & df ['Tarifa'] > 0]

                    
        print("Tickets vendidos: ", len(Tarifa.index))        
        print("Ticket más caro del Titanic: ")        
        print(Tarifa.max())
        print("Ticket más barato del Titanic: ")
        print(Tarifa.min())        
        input()
                
        
    elif opcion == "5":

        print("Saliendo del Sistema")
        break  #saliendo del ciclo repetitivo


    else:

        print("Opción incorrecta")
        input()

        continue     #Continuando el ciclo repetitivo

 