class AllWhatsPy: 
    flag_conection = False
    
    def __init__(self):
        self.mensagem = ...
        self.contato = ...
        
        self.lista_teste = list()
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self) # instanciado para acessar os métodos de envio de mensagem
        self.ctt = AWPContatos(self) # instanciado para acessar os métodos de acessar contatos
        
        
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
        self.objeto_awp = objeto # usado para acessar os atributos
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
        
        
class CriptografiaMensagem(AllWhatsPy):
    """Exercido para a aplicação de criptografia à mensagem enviada.

    Args:
        object (_type_): _description_
    """
    
    def __init__(self):
        self.mensagem_criptografada = ""


    def criptografar(self, mensagem, chave):
        

        for caractere in mensagem:

            if caractere.isalpha():
                ascii_inicial = ord('a') if caractere.islower() else ord('A')
                indice = (ord(caractere) - ascii_inicial + chave) % 26
                caractere_criptografado = chr(ascii_inicial + indice)
                self.mensagem_criptografada += caractere_criptografado
            else:
                self.mensagem_criptografada += caractere



    def descriptografar(self, mensagem_criptografada, chave):
        return self.criptografar(mensagem_criptografada, -chave)


        
if __name__=="__main__":
    awp = AllWhatsPy()
    print(awp.lista_teste)
    print(awp.ctt.encontrar_contato())
    print(awp.ctt.encontrar_contato())
    
    c = CriptografiaMensagem()
    c.criptografar("Lucas Lourenco",3)
    print(c.mensagem_criptografada) 
