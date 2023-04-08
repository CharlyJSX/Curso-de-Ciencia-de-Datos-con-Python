# -*- coding: utf-8 -*-

#Librerias de sistema a utilizar
import smtplib, ssl
import pandas as pd 

#Credenciales de Gmail
usermail = "" 
password = ""

#Configuración SMPT con el Servidor de Gmail
ssl_context = ssl.create_default_context()
server = smtplib.SMTP_SSL('Smtp.gmail.com', 465, context=ssl_context)

#Uso de Credenciales del Gmail
server.login(usermail, password)

#Lectura de Archivo
df = pd.read_excel("archivo.xlsx")

try:
    #Recorremos el archivo de Excel
    for i in df.index:
        #correo = 
        nota1 = df['cuestionario1'][i]
        nota2 = df['practica1'][i]
        nota3 = df['practica2'][i]
        nota4 = df['practica3'][i]
        nota5 = df['examen'][i]

        notafinal = df['nota'][i]
        asistencia = df['asistencia'][i]*100 + "%"

        estado = df['estado'][i]
        message = """\
        Subject: Asunto
        Cuerpo del Mensáje
        """

        result = server.sendmail(usermail, df['correo'][i], message)
        print("Enviado al "+ df['correo'][i])

except:
    print("Error al Enviar el mensaje")

server.quit()