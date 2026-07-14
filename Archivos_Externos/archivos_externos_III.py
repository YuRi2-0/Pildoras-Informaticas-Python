import os

# Creacion de directorio
# os.makedirs("Archivos_Externos\\Prueba_Directorio")

# Cambio de directorio
# os.chdir("Archivos_Externos/Prueba_Directorio")

with open ("Archivos_Externos\\Prueba_Directorio\\segundoArchivo.txt","w",encoding="UTF-8") as archivo_externo:
    archivo_externo.write("Agregamos un titulo a nuestro segundo archivo externo")


# Ruta actual
# print(os.getcwd())