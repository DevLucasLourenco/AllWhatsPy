from decorators_awp import *
from errors_awp import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)


class AWPContatos():
    """
    Classe criada para a realização de tarefas com contatos.
    """
    
    def __init__(self, objeto):
        self.objeto_awp = objeto # usado para acessar os atributos
        self.objeto_awp._get_logging('AWPContatos obteve êxito.')


    @aprovarConexao
    def encontrar_usuario(self, contato_destino):   

        self.objeto_awp._drive.get(f'https://web.whatsapp.com/send?phone={contato_destino}')
        
        textbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        textbox = self.objeto_awp._marktime_func(textbox_xpath)
        textbox.click()

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
            
        
    @aprovarConexao
    def encontrar_contato(self):
               
        ...
        next(self.objeto_awp._generator_info_contato_acessado)
        
        ...
        next(self.objeto_awp._generator_info_contato_acessado)
        
    
    @aprovarConexao
    def __verificacao_existencia_contato(self):
        ...
        
        
    @aprovarConexao
    def _executar_ordem_de_teclas(self, tecla_especial: str, quantidade_fornecida):
        for i in range(quantidade_fornecida):

            ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down(
                                                        Keys.ALT).send_keys(tecla_especial).perform()
            time.sleep(1) 
            



    @aprovarConexao
    def chat_acima(self, quantidade: int = 1):
        time.sleep(1)
        self._executar_ordem_de_teclas(tecla_especial="[", quantidade_fornecida=quantidade)

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)


    @aprovarConexao
    def chat_abaixo(self, quantidade: int = 1):        
        time.sleep(1)
        self._executar_ordem_de_teclas(tecla_especial="]", quantidade_fornecida=quantidade)

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
        