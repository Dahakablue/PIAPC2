import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText
#!pip install smtplib

# Crea la conexión SMTP
def enviocorreo(archivo):
  
  server = smtplib.SMTP('smtp.gmail.com', 587)

  correo = 'pruebapiapc2023@gmail.com'
  pas ='holaamlo1234'
  #  Inicia sesión en tu cuenta de Gmail
  server.starttls()

  server.login(correo, pas)

# Definir el remitente y destinatario del correo electrónico
  remitente = "pruebapiapc2023@gmail.com"
  destinatario = "david.serrano.gallo@gmail.com"

# Crear el mensaje del correo electrónico
  mensaje = email.mime.multipart.MIMEMultipart()
  mensaje['From'] = remitente
  mensaje['To'] = destinatario
  mensaje['Subject'] = "Correo electrónico con archivo adjunto"

# Añadir el cuerpo del mensaje
  cuerpo = "Hola,\n\nAdjunto los archivos que se envian desde la herramienta para corraborar tanto su contenido como su hash.\n\nSaludos,\n jesus"
  mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

# Añadir el archivo Excel como adjunto
  ruta_archivo = archivo
  archivo = open(ruta_archivo, 'rb')
  adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
  adjunto.set_payload((archivo).read())
  email.encoders.encode_base64(adjunto)
  adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
  mensaje.attach(adjunto)

# Convertir el mensaje a texto plano
  texto = mensaje.as_string()

# Enviar el correo electrónico
  server.sendmail(remitente, destinatario, texto)

# Cerrar la conexión SMTP
  server.quit()