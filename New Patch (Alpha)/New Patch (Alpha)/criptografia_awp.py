

class AWPCriptografia():
    """
    Classe desenvolvida para a criptografia quando requisitado.

    Args:
        mensagem (str): referente à mensagem a qual será criptografada.
        chave (int): a chave para criptografar e descriptografar a mensagem.
        metodo (str): Selecione entre "c" e "d", para criptografar e descriptografar respectivamente.
    """
    
    # criar depois um log com todas as criptografias feitas até então. ex {0:xlaxaslkxa xlapxla, 1: duhasudsad uhasudsuad}
    def __init__(self, mensagem, chave, metodo: str):
        self.metodo = metodo # c ou d, criptografar e descriptografar respectivamente
        self.mensagem = mensagem
        self.chave = chave
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
                indice = (ord(caractere) - ascii_inicial + chave) % 26
                caractere_criptografado = chr(ascii_inicial + indice)
                self.resultado += caractere_criptografado
                
            else:
                self.resultado += caractere
    
    
    def descriptografar(self, mensagem_criptografada, chave):
        self.criptografar(mensagem_criptografada, -chave)
        
        
    def fetch(self):
        return self.resultado
        
        
        
    def __apos_conclusao_decorator():
        def descriptografia():
            ...
            
        return descriptografia
            
        