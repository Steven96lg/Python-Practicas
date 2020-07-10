import os

print('<< MANEJO DE ARCHIVOS EN PYTHON >>\n')
print('Si Desea Crear un Archivo Acontinuacion Escriba => a.')
print('Si Desea Eliminar un Archivo Acontinuacion Escriba => d')
print('Si Desea Leer el Contenido de un Archivo Acontinuacion Escriba => r')
print('Si Desea Sobre Escribir un Archivo Acontinuacion Escriba => w\n')

metodo = input("Que Desea Hacer?: ")

if metodo != 'a' and metodo != 'r' and metodo != 'd' and metodo != 'w':
	print('La Accion no Coincide, por favor Ingrese uno de los Sig Metodos')
	print(' a\n d\n r\n w')
else:
	nameFile = input("Ingrese el Nombre del Archivo que Desea Manipular o Crear: ")
	if metodo == 'a':
		if os.path.exists(nameFile+'.txt'):
			print('El Archivo Ya Existe')
		else:
			file = open(nameFile+'.txt', 'a')
			inpText = input('Ingrese Contenido En Su Archivo: ')
			file.write(inpText)
			print('Su archivo Fue Creado Satisfactoriamente')
			file.close()

	elif metodo == 'r':
		opFile = open(nameFile+'.txt', 'r')
		print(opFile.read())

	elif metodo == 'd':
		if os.path.exists(nameFile+'.txt'):
			os.remove(nameFile+'.txt')
			print('Archivo Eliminado')

		else:
			print('El Archivo Que Desea Elmininar no Existe')

	elif metodo == 'w':
		wFile = open(nameFile+'.txt', 'w')
		newText = input('Ingrese el nuevo Texto que Desea Sobre Escribir: ')
		wFile.write(newText)
		print('Texto Modificado Correctamente')
		wFile.close()
