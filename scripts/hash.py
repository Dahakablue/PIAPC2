import hashlib
import os 
from valoreshash import eschash
def encrypt_string(archivo,savefile):
  file_objt = open(archivo,"rb")
  file = file_objt.read()
  Hash = hashlib.sha512(file)
  Hashed = Hash.hexdigest()
  file_objt.close()
  eschash(Hashed,savefile)

  
  
  

  
