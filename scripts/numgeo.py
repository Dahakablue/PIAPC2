#telefono prueba +34 919931243


import phonenumbers 
from phonenumbers import timezone
from hash import encrypt_string
import folium
from opencage.geocoder import OpenCageGeocode
from correo import enviocorreo
from guardar2 import escribir2

def geonum(savehtml,extencion,parametro):
  from phonenumbers import geocoder
  from phonenumbers import carrier
  key = '5cf29c8ac7bd4833a28cee4b5eaa6c9e'

  numero = phonenumbers.parse('+' + extencion + parametro )

  zona = timezone.time_zones_for_number(numero)

  geo = geocoder.description_for_number(numero, 'en')

  carrier = carrier.name_for_number(numero, 'en')



  geocoder = OpenCageGeocode(key)



  query = str(geo)

  results = geocoder.geocode(query)

  lat = results[0]['geometry']['lat']

  lng = results[0]['geometry']['lng']

  myMap = folium.Map(location=[lat, lng], zoom_start = 9)

  folium.Marker([lat, lng],popup= geo).add_to((myMap))
  myMap.save(savehtml +"/myLocation.html")
  var = savehtml + "/myLocation.html"
  encrypt_string(var,savehtml)
  enviocorreo(var)
  


  datos = (numero,zona, geo, lat, lng)
  datos = str(datos)
  escribir2(savehtml,datos)