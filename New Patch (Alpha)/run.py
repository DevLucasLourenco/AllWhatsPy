from __init__ import AllWhatsPy



awp = AllWhatsPy()

awp.conexao(server_host=True, popup=True)
# awp.ctt.encontrar_usuario(21959061623)
# awp.ctt.encontrar_usuario(21984273613)
awp.ctt.encontrar_usuario(21959061623)
# awp.msg.enviar_mensagem('lucas é lindo')
# awp.msg.enviar_mensagem(['lucas é lindo', 'e legal'])
awp.ctt.chat_abaixo()
# awp.utilidade.arquivar_chat()
# awp.ctt.chat_acima()
# awp.ctt.chat_abaixo(1)
# awp.ctt.chat_acima(2)
# input()



# awp.ctt.chat_abaixo()
print(awp.InferenciaAWP.contato)
print(awp.InferenciaAWP.lista_contatos)
# print(awp.InferenciaAWP.mensagem)
# input()
# awp.desconectar()

key = 3
with awp.criptografia('lucas', key, 'c') as cript:
    texto = cript.fetch()

with awp.criptografia(texto, key, 'd') as descript:
    texto_descrip = descript.fetch()

print(texto)
print(texto_descrip)

