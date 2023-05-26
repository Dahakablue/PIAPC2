from hash import encrypt_string
from correo import enviocorreo

def escribir2(savefile,datos):
  archivo = open(savefile +"/datos.txt", 'a+')
  var = savefile + "/datos.txt"
  archivo.write("\n" + datos)
  archivo.close()
  encrypt_string(var,savefile)
  enviocorreo(var)