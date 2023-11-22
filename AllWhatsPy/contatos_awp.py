from .decorators_awp import aprovarConexao, executarOrdemTeclas, aguardeCooldown
from .errors_awp import AWPConnectionError
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
   
    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')
        self._status_aguarde:dict[str:bool, str:int, str:int] = {'status_bool':False,
                                                                 'quantidade_realizacao':0,
                                                                 'tempo_cooldown':0}

    @aprovarConexao
    def encontrar_usuario(self, contato_destino):
        time.sleep(0.5)
        
        self.objeto_awp._drive.get(f'https://web.whatsapp.com/send?phone={contato_destino}')
        
        if self.__verificacao_existencia_contato(contato_destino):
            next(self.objeto_awp._generator_info_contato_acessado)
            next(self.objeto_awp._generator_info_contato_acessado)


    @aprovarConexao
    def encontrar_contato(self, contato_destino):
        ActionChains(self.objeto_awp._drive).key_down(Keys.ESCAPE).perform()
        ActionChains(self.objeto_awp._drive).key_up(Keys.ESCAPE).perform()
        
        var_aux_xpath = self.objeto_awp._ArmazemXPATH.var_aux2_xpath
        self.objeto_awp._marktime_func(var_aux_xpath)
        self.objeto_awp._drive.find_element(By.XPATH, var_aux_xpath).send_keys(contato_destino)
    
        time.sleep(3)
        self.objeto_awp._drive.find_element(By.XPATH, var_aux_xpath).send_keys(Keys.ENTER)
        time.sleep(0.5)

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
        
        self.objeto_awp.InferenciaAWP.contato_acessivel = True
        
    
    def __verificacao_existencia_contato(self, contato):
        while True:
            try:
                if self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button/div/div').is_displayed(): #xpath da verificação do numero quando não existe
                    self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button/div/div').click()
                    
                    self.objeto_awp.InferenciaAWP.contatosInexistentes.append(contato)
                    self.objeto_awp._get_logging(f'   Contato {contato} não existe.')
                    self.objeto_awp._get_logging(f'   Lista de contatos inexistentes nesta instância: {self.objeto_awp.InferenciaAWP.contatosInexistentes}')
                    self.objeto_awp.InferenciaAWP.contato_acessivel = False
                    return False
                
            except Exception as e:
                try:
                    if self.objeto_awp._drive.find_element(By.XPATH, self.objeto_awp._ArmazemXPATH.textbox_xpath).is_displayed():# xpath do textbox
                        self.objeto_awp.InferenciaAWP.contato_acessivel = True
                        time.sleep(1)
                        return True
                except:
                    time.sleep(1)

    
    @executarOrdemTeclas
    @aprovarConexao
    def chat_acima(self):
        time.sleep(0.5)
        self.objeto_awp.InferenciaAWP.contato_acessivel = True
        return Keys.CONTROL, Keys.SHIFT, Keys.ALT, '['

    
    @executarOrdemTeclas
    @aprovarConexao
    def chat_abaixo(self):
        time.sleep(0.5)   
        self.objeto_awp.InferenciaAWP.contato_acessivel = True
        return Keys.CONTROL, Keys.SHIFT, Keys.ALT, ']'


    def _config_aguarde(self, dados:dict[bool, int, int]) -> dict:
        if isinstance(dados, dict):
            self._status_aguarde = self._status_aguarde.update(dados)
            