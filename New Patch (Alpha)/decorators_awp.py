from errors_awp import *
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def aprovarConexao(func):
    def wrapper(self, *args, **kwargs):
        try:
            if self.objeto_awp._flag_status():
                self.objeto_awp._get_logging(f'AllWhatsPy.{func.__name__}() inicializou.')
                return func(self, *args, **kwargs)
            raise AWPConnectionError        
    
        finally:
            if self.objeto_awp._flag_status():
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} finalizou sua execução com êxito.')
            else:
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} encontrou uma falha na execução.')
    return wrapper



def loginServer(self, func):
    def wrapper(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C://users/Profile AllWhatsPy') 
        servico = Service(ChromeDriverManager().install())
        self.drive = webdriver.Chrome(service=servico, options=options)
        self.drive.maximize_window()
        self.marktime = WebDriverWait(self.drive, 90)


        var_aux_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        while True:
            try:
                self.drive.find_element(By.XPATH, var_aux_xpath)
                self._get_logging('Conexao Efetuada.')
                break

            except:
                self._get_logging('Aguardando Login via QR Code...')
                t.sleep(5)

        self.flag_conection = True   

    return wrapper

