import argparse
import os
from numgeo import geonum
from guardar import escribir

import subprocess
import logging

#conectando powershell y python mandar a llamar un comando que puede ller todos los puertos a escanear de la ip target para ponerla en un arreglo o en una lista o en un strng y poderlos leer en -p


#funcion en la cual se desplegara el menu
#poner por defecto conectando con powershell el comando Get-Location

def valor_entrada(valordef):
  
    description = "Ejemplo de uso\n-a \"ruta del archivo\"\n-t \"numero de telefono\"\n"
    parser = argparse.ArgumentParser(description="busqueda de metadata en imagenes y geolocalizacion en numero de telefono", epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-a", help="ponga la ruta del archivo a escanear")
    parser.add_argument("-t", help="ponga el numero de telefono", required=True)
    parser.add_argument("-e", help="extencion", default="52")   
    parser.add_argument("-f",help="Escribe en donde se guardaran los archivos", default=valordef)#default "C:\Users\$env:USERNAME"

    args = parser.parse_args()
    try:
      
      if not args.a :
        logging.basicConfig(level=logging.ERROR, filename=valordef + '/error.txt')
        logging.error("argumento vacio")
      else:
        pass
    except:
      pass
      

    v = args.a
    telefono = args.t
    extencion = args.e
    file = args.f
    printMeta(v,file)
    geonum(file,extencion,telefono)

def default():
  comando = "$env:USERNAME"
  lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
  runningProcesses = subprocess.check_output(lineaPS)
  conv = "C:/Users/" + str(runningProcesses.decode())
  x = conv[:-2:]
  valor_entrada(x)







# -*- encoding: utf-8 -*-

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        
        
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

        
        
        
        

        


 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta(ruta,ruta2):
    lista = []
    lista2=[]
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            lista2.append(name)
            
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                lista.append(str(exif['GPSInfo']))
                
                """for metadata in exif:
                    print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    lista2.append(str(exif[metadata]))
                print ("\n")"""
                
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
    convert = str(lista)##remover elementos extranos
    string = convert.replace("[","").replace("]","")
    string2 = string.replace("{","").replace("}","")
    string3 = string2.replace("\"","").replace("\"","")
    escribir(str(lista2),ruta2, string3)

#hash para cada uno de los archivos 


if __name__ == "__main__":
  default()




   

