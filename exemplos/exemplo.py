from AllWhatsPy import *

lista_numeros = ['21900000000', '21900000000', '21900000000', '21900000000', '21900000000']

img = 'algumaimg.ext'

# exeução
conexao()

for numero in lista_numeros:
    encontrar_usuario(numero)
    enviar_imagem(img)

desconectar()
