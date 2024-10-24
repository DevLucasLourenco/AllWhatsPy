from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()

awp.conexao(server_host=True)
awp.ctt.encontrar_usuario(21959061623)
awp.msg.enviar_mensagem('Hello World')
awp.msg.analise.ultima_mensagem_chat()

 