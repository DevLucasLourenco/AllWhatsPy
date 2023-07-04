from awp import AllWhatsPy
import requests

class AWPMensagem(AllWhatsPy):
    """
    Utilizado para o envio de mensagem
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos; mudar isto. criar um método onde receba o valor e faça a relação de atribuição aos atributos, não realizar diretamente com o objeto_awp
        self.localizacao = AWPEndereco

        
    def enviar_mensagem(self):
        print('metodo de mensagem')
        



class AWPEndereco(AWPMensagem):

    def __init__(self, cep: int):
        self.link = 'https://viacep.com.br/ws/{}/json/'
        self.cep = AWPEndereco.tratamento_cep(cep)
        self.run()
    

    @staticmethod
    def tratamento_cep(item):
        item = str(item)
        if '-' in item:
            item =  item.replace('-','')
        
        if '.' in item:
            item = item.replace('.','')

        if len(item) == 8:
            return item

    def run(self):
        requisicao = requests.get(self.link.format(self.cep)).json()
        rua = requisicao['logradouro'] 
        cidade = requisicao['localidade'] 
        bairro = requisicao['bairro'] 
        uf = requisicao['uf'] 

        self.dados = requisicao, rua, cidade, bairro, uf


    def fetch(self):
        return self.dados
  



        
    

    

    