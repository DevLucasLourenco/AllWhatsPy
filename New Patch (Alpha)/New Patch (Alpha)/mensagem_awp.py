from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
import requests


class AWPMensagem():
    """
    Utilizado para o envio de mensagem
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging('AWPMensagem obteve êxito.')
        self.localizacao = Endereco

        
    def enviar_mensagem(self, mensagem):
            if not self.objeto_awp._flag_status():
                raise ConnectionError("Conexão não estabelecida.")
        
            searchbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            try:
                if isinstance(mensagem, list):        
                    mensagem = '\n'.join(mensagem)
                    self.objeto_awp.drive.find_element(By.XPATH,searchbox_xpath).send_keys(mensagem,Keys.ENTER)         
                    
                else:    
                    self.objeto_awp.drive.find_element(By.XPATH, searchbox_xpath).send_keys(mensagem, Keys.ENTER)
                                        
                self.objeto_awp._get_logging(f'Mensagem enviada para {self.objeto_awp._contato}')
                self.objeto_awp._get_logging(f'{self.enviar_mensagem.__name__} finalizou sua execução com êxito.')
                
            except:
                self.objeto_awp._get_logging('Não foi possível enviar a mensagem')
                
            

class Endereco(AWPMensagem):

    def __init__(self, cep: int):
        self.link = 'https://viacep.com.br/ws/{}/json/'
        self.cep = Endereco.tratamento_cep(cep)
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
        try:
            requisicao = requests.get(self.link.format(self.cep)).json()
            rua = requisicao['logradouro'] 
            cidade = requisicao['localidade'] 
            bairro = requisicao['bairro'] 
            uf = requisicao['uf'] 

            self.dados = requisicao, rua, cidade, bairro, uf
            
        except requests.JSONDecodeError:
            
            raise ValueError("Insira um CEP válido")

    def fetch(self):
        return self.dados
  



        
    

    

    
