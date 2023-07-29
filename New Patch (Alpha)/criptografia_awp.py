import logging

class AWPCriptografia():
    """
    Classe desenvolvida para a criptografia quando requisitado.

    Args:
        mensagem (str): referente à mensagem a qual será criptografada.
        chave (int): a chave para criptografar e descriptografar a mensagem.
        metodo (str): Selecione entre "c" e "d", para criptografar e descriptografar respectivamente.
    """
    logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='event.log', format='%(asctime)s - %(levelname)s - %(message)s')

    # criar depois um log com todas as criptografias feitas até então. ex {0:xlaxaslkxa xlapxla, 1: duhasudsad uhasudsuad}
    def __init__(self, mensagem, chave_numeral, metodo: str):
        logging.info('AWPCriptografia foi iniciado com êxito.')
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
        
        
        
    def fetch(self):
        if self.metodo == 'c':
            logging.info(f"AWPCriptografia está criptografando a mensagem: {self.mensagem[:50]}")
            logging.info(f"AWPCriptografia criptografou a mensagem para: {self.resultado[:50]}")
        elif self.metodo == 'd':
            logging.info(f"AWPCriptografia está descriptografando a mensagem: {self.mensagem[:50]}")
            logging.info(f"AWPCriptografia descriptografou a mensagem para: {self.resultado[:50]}")
        return self.resultado
        

    def __apos_conclusao_decorator():
        def descriptografia():
            ...
            
        return descriptografia
            

