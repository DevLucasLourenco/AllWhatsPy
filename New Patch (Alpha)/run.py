from __init__ import AllWhatsPy



awp = AllWhatsPy()

awp.conexao(True)
# awp.ctt.encontrar_usuario(21959061623)
awp.ctt.encontrar_usuario(21984273613)
awp.ctt.encontrar_usuario(21959061623)
# awp.ctt.chat_abaixo()
# awp.msg.enviar_mensagem('lucas é lindo')
awp.msg.enviar_mensagem(['lucas é lindo', 'e legal'])
# awp.ctt.chat_abaixo(1)
# awp.ctt.chat_acima(2)
# input()



awp.ctt.chat_abaixo()
print(awp.InferenciaAWP.contato)
print(awp.InferenciaAWP.lista_contatos)
print(awp.InferenciaAWP.mensagem)
# input()
# awp.desconectar()



with awp.criptografia('lucas',3,'c') as cript:
    texto = cript.fetch()

with awp.criptografia(texto,5, 'd') as descript:
    texto_descrip = descript.fetch()

print(texto)
print(texto_descrip)
