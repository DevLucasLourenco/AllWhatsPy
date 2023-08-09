from decorators_awp import aprovarConexao, executarOrdemTeclas
from errors_awp import AWPConnectionError
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
        
        
        textbox = self.objeto_awp._marktime_func(self.objeto_awp._ArmazemXPATH.textbox_xpath)
        textbox.click()

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
            
        
    @aprovarConexao
    def encontrar_contato(self, contato_destino):
        
        var_aux_xpath = self.objeto_awp._ArmazemXPATH.var_aux2_xpath
        self.objeto_awp._marktime_func(var_aux_xpath)
        self.objeto_awp._drive.find_element(By.XPATH, var_aux_xpath).send_keys(contato_destino)
    
        time.sleep(3)
        self.objeto_awp._drive.find_element(By.XPATH, var_aux_xpath).send_keys(Keys.ENTER)
        self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/span/button/span').click()
        time.sleep(0.5)

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
        

    
    @aprovarConexao
    def __verificacao_existencia_contato(self):
        while True:
            try:
                if ...:# xpath do textbox
                    ...
                if ...:# xpath da verificação do numero quando não existe
                    ...
            except:
                time.sleep(1)

  
    @executarOrdemTeclas
    @aprovarConexao
    def chat_acima(self):        
        time.sleep(0.5)   
        return Keys.CONTROL, Keys.SHIFT, Keys.ALT, '['

    
    @executarOrdemTeclas
    @aprovarConexao
    def chat_abaixo(self):     
        time.sleep(0.5)   
        return Keys.CONTROL, Keys.SHIFT, Keys.ALT, ']'
