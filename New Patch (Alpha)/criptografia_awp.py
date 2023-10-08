import logging
from decorators_awp import AWPC_Analytics

class AWPCriptografia():  
    
    def __init__(self, objeto:object, realizar_log:bool):
            self.objeto_awp = objeto
            self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')
            
            LogAWPC.var_validacao_log = realizar_log
            
            
    class CifraDeCaesar():
       
        def __init__(self, mensagem, chave_numeral, metodo: str):
            self.metodo = metodo # c ou d, criptografar e descriptografar respectivamente
            self.mensagem = mensagem
            self.chave = chave_numeral
            self.resultado = ''
            self.objeto_logawp_log = LogAWPC._log

            
        def log_get(self):
            return LogAWPC.var_aux


        def __enter__(self):
            if self.metodo == "c":
                self.criptografar(self.mensagem, self.chave)
            elif self.metodo == "d":
                self.descriptografar(self.mensagem, self.chave)
            return self


        @AWPC_Analytics    
        def __exit__(self, exc_type, exc_val, exc_tb):
            LogAWPC.var_aux = self.resultado, self.__class__.__name__

        
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
            
            return self.resultado
                    
        
        
        def descriptografar(self, mensagem_criptografada, chave):
            self.criptografar(mensagem_criptografada, -chave)
            

        def retornar(self):
            return self.resultado
        
    
    class CifraDeVigenere():

        def __init__(self, mensagem, chave, metodo):
            self.chave = chave
            self.mensagem = mensagem # c ou d, criptografar e descriptografar respectivamente
            self.metodo = metodo
            self.alfabeto = 'abcdefghijklmnopqrstuvwxyz'
            self.resultado = ''
            self.objeto_logawp_log = LogAWPC._log

                    
        def log_get(self):
            return LogAWPC.var_aux


        def __enter__(self):
            if self.metodo == "c":
                self.criptografar(self.mensagem)
            elif self.metodo == "d":
                self.descriptografar(self.mensagem)

            return self


        @AWPC_Analytics
        def __exit__(self, exc_type, exc_value, traceback):
            LogAWPC.var_aux = self.resultado, self.__class__.__name__

        
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


class LogAWPC:
    todas_criptografias: list[str] = list()
    var_aux:tuple[str] = None
    var_validacao_log:bool
    
    
    def _log_primeira_etapa():
        LogAWPC.todas_criptografias.append(LogAWPC.var_aux)
        if LogAWPC.var_validacao_log:
            logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='eventAWP.log', format='%(asctime)s - %(levelname)s - %(message)s')
            return True
        
    def _log(item):
        if LogAWPC._log_primeira_etapa():
            logging.info(item)
        