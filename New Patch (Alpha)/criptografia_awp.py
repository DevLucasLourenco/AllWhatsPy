import logging

class AWPCriptografia():  

    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')


    class CifraDeCaesar():
       
        def __init__(self, mensagem, chave_numeral, metodo: str):
            self.metodo = metodo # c ou d, criptografar e descriptografar respectivamente
            self.mensagem = mensagem
            self.chave = chave_numeral
            self.resultado = ''


        def __enter__(self):
            if self.metodo == "c":
                self.criptografar(self.mensagem, self.chave)
            elif self.metodo == "d":
                self.descriptografar(self.mensagem, self.chave)
                
            return self


        def __exit__(self, exc_type, exc_val, exc_tb):
            pass


        def criptografar(self, mensagem, chave):
            self.resultado = ''

            for caractere in mensagem:
                if caractere.isalpha():
                    ascii_inicial = ord('a') if caractere.islower() else ord('A')
                    indice = (ord(caractere) - ascii_inicial + int(chave)) % 26
                    caractere_criptografado = chr(ascii_inicial + indice)
                    self.resultado += caractere_criptografado
                else:
                    self.resultado += caractere
        
        
        def descriptografar(self, mensagem_criptografada, chave):
            self.criptografar(mensagem_criptografada, -chave)
            

        def retornar(self):
            return self.resultado
        

    class CifraDeVigenere:

        def __init__(self, mensagem, chave, metodo):
            self.chave = chave
            self.mensagem = mensagem # c ou d, criptografar e descriptografar respectivamente
            self.metodo = metodo
            self.alfabeto = 'abcdefghijklmnopqrstuvwxyz'
            self.resultado = ''


        def __enter__(self):
            if self.metodo == "c":
                self.criptografar(self.mensagem)
            elif self.metodo == "d":
                self.descriptografar(self.mensagem)

            return self


        def __exit__(self, exc_type, exc_value, traceback):
            pass


        def criptografar(self, mensagem):
            self.resultado = ''
            mensagem = mensagem.lower()
            mensagem_criptografada = ''
            chave_atual = self.chave * (len(mensagem) // len(self.chave)) + self.chave[:len(mensagem) % len(self.chave)]

            for i in range(len(mensagem)):
                if mensagem[i] in self.alfabeto:
                    indice_mensagem = self.alfabeto.index(mensagem[i])
                    indice_chave = self.alfabeto.index(chave_atual[i])
                    indice_criptografado = (indice_mensagem + indice_chave) % 26
                    caractere_criptografado = self.alfabeto[indice_criptografado]
                    mensagem_criptografada += caractere_criptografado
                else:
                    mensagem_criptografada += mensagem[i]
            self.resultado = mensagem_criptografada


        def descriptografar(self, mensagem):
            self.resultado = ''
            mensagem_descriptografada = ''
            chave_atual = self.chave * (len(mensagem) // len(self.chave)) + self.chave[:len(mensagem) % len(self.chave)]

            for i in range(len(mensagem)):
                if mensagem[i] in self.alfabeto:
                    indice_mensagem = self.alfabeto.index(mensagem[i])
                    indice_chave = self.alfabeto.index(chave_atual[i])
                    indice_descriptografado = (indice_mensagem - indice_chave) % 26
                    caractere_descriptografado = self.alfabeto[indice_descriptografado]
                    mensagem_descriptografada += caractere_descriptografado
                else:
                    mensagem_descriptografada += mensagem[i]
            self.resultado = mensagem_descriptografada


        def retornar(self):
            return self.resultado
