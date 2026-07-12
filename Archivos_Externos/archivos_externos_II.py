with open("Archivos_Externos\\primerArchivo.txt","r", encoding="UTF-8") as archivo_externo:

	# Leemos la mitad del archivo externo
	# archivo_externo.seek(len(archivo_externo.read())/2)

	# Lectura del documento omitiendo la primera linea
	archivo_externo.seek(len(archivo_externo.readline()))

	print(archivo_externo.read())
