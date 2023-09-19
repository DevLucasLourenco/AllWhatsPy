from errors_awp import AWPConnectionError
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import messagebox
import os 


def aprovarConexao(func):
    def wrapper(self, *args, **kwargs):
        try:
            if self.objeto_awp._flag_status():
                self.objeto_awp._get_logging(f'AllWhatsPy.{func.__name__}() inicializou.')
                return func(self, *args, **kwargs)
            raise AWPConnectionError        
    
        finally:
            if self.objeto_awp._flag_status() or self._drive._flag_status():
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} finalizou sua execução com êxito.')
            else:
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} encontrou uma falha na execução.')
    return wrapper


def executarOrdemTeclas(func):
    def _ordenacao(self, ordem):
        acao = ActionChains(self.objeto_awp._drive)
        for t in ordem:
            acao.key_down(t)
        
        time.sleep(0.5)
        acao.perform()
        time.sleep(0.5)
            
            
    def wrapper(self, *args, **kwargs):
        run = func(self, *args, **kwargs)
        _ordenacao(self, run)
        
        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
        
    return wrapper
    
