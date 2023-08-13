
class AWPAudio():
    """
    Classe para os serviços de Áudio   
    """

    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')
        

