from selenium.common.exceptions import NoSuchElementException

class AWPConnectionError(ConnectionError):
    def __init__(self, menssagem="Conexão ao AWP não estabelecida."):
        self.message = menssagem
        super().__init__(self.message)
        
        
class AWPContatoNaoEncontrado(NoSuchElementException):
    def __init__(self, menssagem="Contato não encontrado. Impossível realizar métodos da Classe AWPMensagem"):
        self.message = menssagem
        super().__init__(self.message)
