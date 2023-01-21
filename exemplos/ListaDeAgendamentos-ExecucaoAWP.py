import AllWhatsPy as awp


# a cada 30 minutos, vai mandar mensagem
hora_list = ['09','10','10','11','11','12']
minuto_lista = ['45','15','45','15','45','15']


awp.conexao()

awp.encontrar_contato('Lucas Lourenco')

for i, minuto in enumerate(minuto_lista):

    awp.agendamento('21', hora_list[i], minuto)
    awp.enviar_mensagem('Vai beber sua água!')

awp.ultimas_mensagens_conversa()

awp.desconectar()