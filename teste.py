from AllWhatsPy import AllWhatsPy, PseudoAWP



# @PseudoAWP
# def funcao_para_pseudoAWP():
#    awp = AllWhatsPy()
#    msg = ['Mensagem de Envio','Teste']

#    dados_agregacao = {
#       'objeto' : awp,
#       'iter_ctt' : [21169549849489, 21959061623, 'lucas lourenco'],
#       'mensagem' : msg,
#       'metodo' : 'EMI',
#       'server_host' : True,
#       'calibragem' : False,
#       'anexo': r'utilidades\awpimgg.png'
#       }

#    return dados_agregacao

# funcao_para_pseudoAWP()


# a = 'AllWhatsPy(inicializarTitulo=True, realizar_log=True, JSON_file=True)'
# awp = eval(a)
nome = 'lucas'
msg = f"""
mensagem de envio
para teste 
automatizado do {nome}
"""
awp = AllWhatsPy(inicializarTitulo=True, realizar_log=True, JSON_file=True)
# print(awp.msg.endereco(24754000).retornar())


awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(False, 10))
# awp.ctt.encontrar_usuario(2195906162387456)
# awp.msg.enviar_mensagem_isolada('a')
awp.ctt.encontrar_usuario(21959061623)
awp.msg.enviar_mensagemCP(msg)
# # lista = [21959061623, 216546516544989, 21959061623,21959061623, 216546516544989, 21959061623]

# for i, l in enumerate(lista):
#    awp.ctt.encontrar_usuario(l)
#    awp.msg.enviar_mensagem_paragrafada(['teste1', 'teste2', i])
# awp.ctt.encontrar_usuario(21959061623)
# awp.msg.enviar_mensagem_paragrafada('Mensagem paragrafada para envio')

# # Caso 2
# awp.msg.enviar_mensagem_paragrafada(['Mensagem paragrafada','para envio'])

# # Caso 3
# msg = '''
# mensagem
# paragrafada
# para
# envio
# '''
# awp.msg.enviar_mensagem_paragrafada(msg)
# awp.msg.enviar_mensagem_direta()
# @PseudoAWP
# def awp_script(dados):
#     return dados


# awp = AllWhatsPy(inicializarTitulo=False, realizar_log=True, JSON_file=True)

# msg = ['teste', 'de cria']

# dicio = {
#         'objeto' : awp,
#         'iter_ctt' : [21169549849489, 21959061623, 'lucas lourenco', 
#                       21169549849489, 21959061623, 'lucas lourenco', 
#                       21169549849489, 21959061623],
#         'mensagem' : msg,
#         'metodo' : 'EM',
#         'calibragem' : False,
#         }

# awp.ctt._config_aguarde({'status_bool':True, #consertar este metodo
#                         'quantidade_realizacao':3,
#                         'tempo_cooldown':10}
# )

# awp_script(dicio)


# awp.conexao(server_host=True, popup=False, calibragem=False, show_off=True)

# awp.ctt.encontrar_usuario(21959061623)
# awp.msg.enviar_mensagem_isolada('teste')
# awp.msg.analise.ultima_mensagem_chat()

# awp.ctt.encontrar_usuario(2195906162464893)
# awp.ctt.encontrar_usuario(21959061623)
# # # awp.msg.enviar_mensagem_por_link(21959061623,'testezinho legal')
# # awp.ctt.encontrar_usuario(21984273613)
# # # awp.ctt.encontrar_usuario(91469414144944)
# # # awp.ctt.encontrar_usuario(21959061623)

# for i in range(2):
#     awp.ctt.chat_abaixo()
#     awp.ctt.chat_acima()

# awp.utilidade.marcar_como_nao_lida()
# # # awp.utilidade.arquivar_chat()


# print(awp.InferenciaAWP.contato)
# print(awp.InferenciaAWP.lista_contatos)
# print(awp.InferenciaAWP.contatosInexistentes)
# print(awp.InferenciaAWP.mensagem)
# # input()
# # awp.desconectar()

# awp.ctt.encontrar_usuario(91469414144944)
# awp.ctt.encontrar_usuario(21959061623)
# awp.msg.enviar_mensagem_isolada([texto, texto_descrip])

# texto = 'Lucas e o criador do AWP, AllWhatsPy'
# key = 5

# with awp.criptografia.CifraDeCaesar(texto, key, 'c') as caesarC:
#     texto_caesar_c = caesarC.retornar()
# print(texto_caesar_c, '\n')

# with awp.criptografia.CifraDeCaesar(texto_caesar_c, key, 'd') as caesarD:
#     texto_caesar_d = caesarD.retornar()
# print(texto_caesar_d, '\n')
    


# textolegal = 'lucas eh legalzao, po!'
# with awp.criptografia.CifraDeVigenere(textolegal, 'lalaland','c') as vigenereC:
#     texto_vigenere_c = vigenereC.retornar()
# print(texto_vigenere_c,'\n')

# with awp.criptografia.CifraDeVigenere(texto_vigenere_c, 'lalaland','d') as vigenereD:
#     texto_vigenere_d = vigenereD.retornar()
# print(texto_vigenere_d,'\n')


# print(awp.tempo_execucao)


# awp.ctt.encontrar_usuario(21959061623)
# # awp.utilidade.agendamento('13', '09', '24')
# # awp.msg.enviar_mensagem_isolada('teste po 2')
# awp.msg.anexo.enviar_imagem('utilidades/awpimgg.png', 'imagem')
# awp.msg.anexo.enviar_arquivo('utilidades/awpimgg.png','agora, por arquivo')
# # # awp.msg.anexo.enviar_arquivo("texto.txt")
