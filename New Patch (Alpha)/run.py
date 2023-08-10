from __init__ import AllWhatsPy



awp = AllWhatsPy()

awp.conexao(server_host=True, popup=False)
# awp.ctt.encontrar_usuario(21959061623)
# awp.ctt.encontrar_usuario(21959061623)
# awp.ctt.encontrar_usuario(2195906162464893)
# awp.ctt.encontrar_usuario(21959061623)
# awp.ctt.encontrar_usuario(21984273613)
# awp.ctt.encontrar_usuario(91469414144944)
# awp.ctt.encontrar_usuario(21959061623)

# # awp.ctt.encontrar_contato('Lucas Lourenço')
# # awp.ctt.encontrar_contato('Lucas Lourenço')

# mensagem = """
# Olá!
# Sou o Lucas, criador do AWP.
# """
# # awp.msg.enviar_mensagem_paragrafada(mensagem)

# # awp.msg.enviar_mensagem('lucas é lindo')
# awp.msg.enviar_mensagem(mensagem)

# for i in range(2):
#     awp.ctt.chat_abaixo()
#     awp.ctt.chat_acima()

# # awp.utilidade.arquivar_chat()


# print(awp.InferenciaAWP.contato)
# print(awp.InferenciaAWP.lista_contatos)
# print(awp.InferenciaAWP.contatosInexistentes)
# print(awp.InferenciaAWP.mensagem)
# # input()
# # awp.desconectar()
texto = 'Lucas eh o criador do AWP, AllWhatsPy'
key = 3
with awp.criptografia(texto, key, 'c') as cript:
    texto = cript.fetch()

with awp.criptografia(texto, key, 'd') as descript:
    texto_descrip = descript.fetch()

# awp.ctt.encontrar_usuario(91469414144944)
# awp.ctt.encontrar_usuario(21959061623)
# awp.msg.enviar_mensagem([texto, texto_descrip])

print(texto)
print(texto_descrip)

