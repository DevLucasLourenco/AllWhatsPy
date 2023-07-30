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

