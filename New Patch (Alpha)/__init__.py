class AllWhatsPy: 
    flag_conection = False
    
    def __init__(self):
        self.mensagem = ...
        self.mensagem_criptografada = ...
        self.contato = ...
        
        self.lista_teste = list()
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self) # instanciado para acessar os métodos de envio de mensagem
        self.ctt = AWPContatos(self) # instanciado para acessar os métodos de acessar contatos
        self.audio = AWPAudio(self)
                
        
    def testando(self):
        print('de awp executando em mensagem')
        
        
    def conexao(self):
        self.flag_conection = True


    def __informacoes_contato_acessado(self): # método 'Generator' usado para coexistir com a classe AWPContato. Nela, será usada para alcançar os dados do contato acessado.
        xpath = ...
        while True:
            # Etapa 1
            dados = ... # drive.find_element(By.XPATH, xpath).text
            print('info1')
            yield 1
            
            # Etapa 2
            self.__lista_informacoes_contato_aberto.append(dados)
            print('info2')
            yield 2
        
        
    def exportar_txt(objeto): # qual atributo a pessoa decidir
        ...
        
        
        
class AWPMensagem(AllWhatsPy):
    """Utilizado para o envio de mensagem

    Args:
        AllWhatsPy (_type_): _description_
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos; mudar isto. criar um método onde receba o valor e faça a relação de atribuição aos atributos, não realizar diretamente com o objeto_awp
        print('mensagem')
        super().testando()
        self.objeto_awp.lista_teste.append('a')
        
    def enviar_mensagem(self):
        print('aa')
        
        
        
class AWPContatos(AllWhatsPy):
    """Utilizado para encontrar contatos

    Args:
        AllWhatsPy (_type_): _description_
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos
        print('contatos')
        print(self.flag_conection)
        ...
        
        
    def encontrar_contato(self):
        ...
        next(self.objeto_awp._generator_info_contato_acessado)
        
        ...
        
        next(self.objeto_awp._generator_info_contato_acessado)
    
        
    def __verificacao_existencia_contato(self):
        ...
        
        
class AWPCriptografia():
    """...

    Args:
        object (_type_): _description_
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



class AWPAudio(AllWhatsPy):

    def __init__(self, objeto):
        self.objeto_awp = objeto
        
        
        
class Shoot:
    ...
        
        
        
if __name__=="__main__":
    
    awp = AllWhatsPy()
    print(awp.lista_teste)
    awp.ctt.encontrar_contato()
    awp.ctt.encontrar_contato()
    
    chave = 90
    with AWPCriptografia('Lucas Lourenco', chave, 'c') as c:
        res = c.fetch()
        print(res)

    with AWPCriptografia(res, chave, 'd') as c:
        res2 = c.fetch()
        print(res2)
