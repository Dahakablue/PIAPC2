Instalar modulos python
------------------------
pip install -r requirements.txt


Ejecutar
------------------------
python scripts.py


Argumentos opcionales
-------------------------
-a, "ponga la ruta del archivo a escanear" /default=cd ~
-t, "ponga el numero de telefono"
-e, "extencion"
-f, "Escribe en donde se guardaran los archivos" /default="C:\Users\$env:USERNAME"


Detalles
------------------------
El script principal, a través de otros módulos y sus argumentos opcionales podrá obtener:
-La información GPS, tags y metadatos de imágenes (según contengan)
-La posible ciudad de ubicación de un número de celular, así como de su operador telefónico
