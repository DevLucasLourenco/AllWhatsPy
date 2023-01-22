import AllWhatsPy as awp

awp.conexao()

awp.encontrar_primeira_conversa(ignorar_fixado=True)

lista = []
for i in range(2):
    dados = awp.ultimas_mensagens_conversa()
    awp.descer_conversa_origem_atual()
    lista.append(dados)

print(lista)
