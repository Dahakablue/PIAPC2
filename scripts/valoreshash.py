from correo import enviocorreo


def eschash(datos,savefile):
  archivo = open(savefile +"/hash.txt", 'a+')
  var = savefile + "/hash.txt"
  archivo.write("\n" + datos)
  archivo.close()
  correo(var)
  
  
  
  
def correo(arg):
  enviocorreo(arg)
