class AWPConnectionError(ConnectionError):
    def __init__(self, menssagem="Conexão ao AWP não estabelecida."):
        self.message = menssagem
        super().__init__(self.message)
        
