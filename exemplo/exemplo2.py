from AllWhatsPy import AllWhatsPy

lista_contatos = ['lucas lourenco','devlucaslourenco','lucas dev']
mensagem = """
Olá, {}!
Espero que esteja aproveitando o AllWhatsPy
"""

awp = AllWhatsPy(JSON_file=False, realizar_log=False)
awp.conexao(server_host=True)

for contato in lista_contatos:
    awp.ctt.encontrar_contato(contato)
    awp.msg.enviar_mensagem_paragrafada(mensagem.format(mensagem))
    

