from __init__ import AllWhatsPy


awp = AllWhatsPy()

awp.conexao(popup=1)


awp.ctt.encontrar_contato()
awp.ctt.encontrar_contato()
awp.msg.enviar_mensagem()
awp.msg.enviar_mensagem()


with awp.criptografia('lucas',3, 'c') as c:
    res = c.fetch()
    print(res)

with awp.criptografia(res, 3, 'd') as c:
    res2 = c.fetch()
    print(res2)

# algum_cep = 00000000
# localizacao = awp.msg.localizacao(algum_cep).fetch()
# print(localizacao)
