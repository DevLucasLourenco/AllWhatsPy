from decorators_awp import aprovarConexao
from errors_awp import AWPConnectionError
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
import requests
import time


class AWPMensagem():
    """
    Utilizado para o envio de mensagem
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging('AWPMensagem obteve êxito.')
        self.localizacao = Endereco


    @aprovarConexao
    def enviar_mensagem(self, mensagem: str):
            if isinstance(mensagem, int) or isinstance(mensagem, float):
                mensagem = str(mensagem)

            self.objeto_awp.InferenciaAWP.mensagem = mensagem
            textbox = self.objeto_awp._ArmazemXPATH.textbox_xpath
            try:
                if isinstance(mensagem, list):        
                    mensagem = '\n'.join(mensagem)
                    self.objeto_awp._drive.find_element(By.XPATH,textbox).send_keys(mensagem,Keys.ENTER)         
                    
                else:    
                    self.objeto_awp._drive.find_element(By.XPATH, textbox).send_keys(mensagem, Keys.ENTER)
                                        
                self.objeto_awp._get_logging(f'Mensagem enviada para {self.objeto_awp.InferenciaAWP.contato}')
                self.objeto_awp._get_logging(f'Mensagem: {self.objeto_awp.InferenciaAWP.mensagem[:35]}[...]')

            except Exception as e:
                self.objeto_awp._get_logging(f'Não foi possível realizar o envio da mensagem - erro: {e}')

            time.sleep(1)


    # @aprovarConexao
    # def enviar_mensagem_paragrafada(self, mensagem: str):
    #     self.objeto_awp.InferenciaAWP.mensagem = mensagem
    #     textbox = self.objeto_awp._marktime_func(self.objeto_awp._ArmazemXPATH.textbox_xpath)
    #     textbox.click()

    #     for linha in mensagem.split('\n'):
    #         textbox.send_keys(linha)
            
    #         ActionChains(self.objeto_awp._drive).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()

    #         textbox.send_keys(Keys.ENTER)





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


    def get(self):
        return self.dados
  



        
    

    

    
