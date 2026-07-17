import os
os.system("clear")

# Abrir archivos con open()

path = "C:/Users/Pens Computacional/Desktop/CURSO PYTHON/Archivos/ "
pedir_absoluto = path.strip + "texto.txt"

archivo = open ('texto.txt', "r")
# open (nombre_archivo, modo)

# nombre_archivo=str
# modo : str ->

# r-> solo lectura
# w -> escritura, crea el archivo o lo sobrescrive si ya existe
# a -> crea el archivo sino existe, si existe agrega al finalsin borrar lo que habia
# x-> creacion exclusiva , errorerror si ya existe
# r+ -> lectura y escritura , error si no existe


print(archivo.read())

archivo.close