from AllWhatsPy import AllWhatsPy


awp = AllWhatsPy(JSON_file=False, realizar_log=False)
awp.conexao(server_host=True)

awp.utilidade.agendamento('15', '13', '50')
awp.msg.enviar_mensagem_por_link(21959061623, 'Hello World')

