from awp import AllWhatsPy


class AWPMensagem(AllWhatsPy):
    """
    Utilizado para o envio de mensagem

    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos; mudar isto. criar um método onde receba o valor e faça a relação de atribuição aos atributos, não realizar diretamente com o objeto_awp
        print('mensagem')
        super().testando()
        self.objeto_awp.lista_teste.append('a')
        
    def enviar_mensagem(self):
        print('metodo de mensagem')
        
        



        
        