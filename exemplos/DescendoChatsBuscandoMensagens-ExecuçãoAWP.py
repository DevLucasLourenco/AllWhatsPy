import AllWhatsPy as awp

awp.conexao()
awp.encontrar_primeira_conversa(ignorar_fixado=False)

lista_dados = []
for i in range(10):
    dados = awp.ultimas_mensagens_conversa()
    lista_dados.append(dados)
    
    
print(dados)