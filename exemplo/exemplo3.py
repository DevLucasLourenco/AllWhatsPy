from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(realizar_log=False, JSON_file=False)
senha = 5

with awp.criptografia.CifraDeCaesar('Mensagem para criptografia', senha, 'c') as m:
    msg_criptografada = m.retornar()
print(msg_criptografada)


with awp.criptografia.CifraDeCaesar(msg_criptografada, senha, 'd') as m2:
    msg_descriptografada = m2.retornar()
print(msg_descriptografada)
