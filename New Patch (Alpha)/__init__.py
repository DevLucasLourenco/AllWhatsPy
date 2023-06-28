class AllWhatsPy: 
    flag_conection = False
    
    def __init__(self):
        self.lista_teste = list()
        self.lista_informacoes_contato_aberto = list()
        self.generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self) # instanciado para acessar os métodos de envio de mensagem
        self.ctts = AWPContatos(self) # instanciado para acessar os métodos de acessar contatos
        
        
    def testando(self):
        print('de awp executando em mensagem')
        
        
    def conexao(self):
        self.flag_conection = True


    def __informacoes_contato_acessado(self):
        xpath = ...
        while True:
            # Etapa 1
            dados = ... # drive.find_element(By.XPATH, xpath).text
            yield 1
            
            # Etapa 2
            self.lista_informacoes_contato_aberto.append(dados)
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
        next(self.generator_info_contato_acessado)
        
        ...
        
        next(self.generator_info_contato_acessado)
    
        
    def __verificacao_existencia_contato(self):
        ...
        
        
        
        
if __name__=="__main__":
    awp = AllWhatsPy()
    print(awp.lista_teste)
