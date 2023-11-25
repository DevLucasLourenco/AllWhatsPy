from selenium.common.exceptions import NoSuchElementException

class AWPConnectionError(ConnectionError):
    def __init__(self, menssagem="Conexão ao AWP não estabelecida."):
        self.message = menssagem
        super().__init__(self.message)
        
        
class AWPContatoNaoEncontrado(NoSuchElementException):
    def __init__(self, menssagem="Contato não encontrado. Impossível realizar métodos da classe AWPMensagem"):
        self.message = menssagem
        super().__init__(self.message)


class AWPHorarioUltrapassado(RuntimeError):
    def __init__(self, menssagem="Variável de prosseguimento validada como False. -> Horário Agendado Ultrapassado, não será possível continuar"):
        self.message = menssagem
        super().__init__(self.message)