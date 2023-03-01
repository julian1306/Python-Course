#def calculadora(*args, **kwargs):
  #suma = 0
  #if 'operacion' in kwargs:
    #if kwargs['operacion'] == 'suma':
      #for arg in args:
        #suma += arg
    #elif kwargs['operacion'] == 'resta':
      #for arg in args:
        #suma -= arg
  #return suma


#operacion = input('Ingrese la operacion a realizar (suma/resta): ')
#print(calculadora(30, 100, 80, 30, 22, 5, operacion = operacion))




#file=open("C:\\Users\julian\Desktop\Curso python\Clase 8\paraLeer.txt","r")




from email import message
import keyword
from multiprocessing import connection
from email.mime.multipart import MIMEMultipart


import smtplib

my_email = "julian.garcia1306@gmail.com"
password = "hvmscbsxqtnfdaef"
#password = "NvidiaRtx2070!!"


connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = password)

message = 'Subject: {}\n\n{}'.format("topu", "sos un trolo")

connection.sendmail(from_addr= my_email, to_addrs = "brianmondino@gmail.com", message )
connection.close

