from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from decorators_awp import aprovarConexao
import time


class AWPUtilidades:
    def __init__(self, objeto) -> None:
        self.objeto_awp = objeto
        self.objeto_awp._get_logging('AWPUtilidades obteve êxito.')


    @aprovarConexao
    def arquivar_chat(self):
        ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
                                                             Keys.SHIFT).send_keys('e').perform()
        
        self.objeto_awp._get_logging(f'{self.objeto_awp.InferenciaAWP.contato} foi arquivado.')
        time.sleep(1)