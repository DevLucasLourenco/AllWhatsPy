from AllWhatsPy import AllWhatsPy, PseudoAWP


# lista_ctt_numero = [21959061623, 219999999999987, 21959061623]
lista_ctt_numero = [21959061623]

texto = '''
Teste - {} - {}
endereco: {}
'''

#
AWP = AllWhatsPy()
AWP.conexao(server_host=True)

endereco = AWP.msg.endereco(24020110).retornar()

horario_agendado = AWP.utilidade.Schedule(hora_aguardado=9, minuto_aguardado=22)


for i, cn in enumerate(lista_ctt_numero):

    with AWP.criptografia.CifraDeCaesar(texto.format(cn, i, endereco), 5, 'c') as crpt:
        t1 = crpt.retornar()

    with AWP.criptografia.CifraDeCaesar(t1, 5, 'd') as crpt:
        t2 = crpt.retornar()

    # AWP.ctt.encontrar_usuario(cn)
    AWP.ctt.encontrar_contato(cn)

    AWP.msg.enviar_mensagem_isolada(horario_agendado)
    
    AWP.msg.enviar_mensagem_paragrafada(t2)
    AWP.msg.enviar_mensagemCP(t1)
    AWP.msg.enviar_mensagem_compulsiva(3, [t1, t2])

    AWP.msg.anexo.imagem(r'utilidades/awpimgg.png', 'através do AWP.msg.anexo.imagem()')
    AWP.msg.anexo.arquivo(r'AllWhatsPy/__init__.py')
    

    AWP.msg.enviar_mensagem_isolada('Teste realizado==========')
    
#    
print('Teste')


