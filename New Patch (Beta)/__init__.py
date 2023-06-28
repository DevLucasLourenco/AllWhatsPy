class AllWhatsPy:
    flag_conection = False
    def __init__(self):
        self.lista_teste = list()
        self.lista_informacoes_contato_aberto = list()
        self.generator = self.__informacoes_contato_aberto()
        self.msg = AWPMensagem(self) # instanciado para acessar os métodos de envio de mensagem
        self.ctts = AWPContatos(self) # instanciado para acessar os métodos de acessar contatos
        
    def testando(self):
        print('de awp executando em mensagem')
        
    def conexao(self):
        self.flag_conection = True

    def __informacoes_contato_aberto(self):
        # while True:
            xpath = ...
            dados = ... # drive.find_element(By.XPATH, xpath).text
            yield 1
            
            self.lista_informacoes_contato_aberto.append(dados)
            yield 2
        
        
    def exportar_txt(objeto): # qual atributo a pessoa decidir
        ...
        
class AWPMensagem(AllWhatsPy):
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos
        print('mensagem')
        super().testando()
        self.objeto_awp.lista_teste.append('a')
        
        
        
class AWPContatos(AllWhatsPy):
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos
        print('contatos')
        print(self.flag_conection)
        ...
    def encontrar_contato(self):
        ...
        next(self.generator)
        
        ...
        next(self.generator)
        
        
awp = AllWhatsPy()
print(awp.lista_teste)
