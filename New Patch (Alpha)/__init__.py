import dataclasses
from audio_awp import AWPAudio
from contatos_awp import AWPContatos
from mensagem_awp import AWPMensagem
from criptografia_awp import AWPCriptografia
from errors_awp import *
from decorators_awp import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)
import string
from tkinter import messagebox
from  PIL import Image
from urllib import parse
import urllib.request
import os
import time as t
import logging



class AllWhatsPy: 
    logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='event.log', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger('webdriver_manager').setLevel(logging.CRITICAL)
    flag_conection = False
    
    
    def __init__(self):
        self._get_logging(f"{'—'*15} AllWhatsPy - AWP {'—'*15}")
        
 
        # self._mensagem = None
        # self._contato = None
        
        # self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self)
        self.ctt = AWPContatos(self)
        self.audio = AWPAudio(self)
        self.criptografia = AWPCriptografia
    
        self.drive = None
        self.marktime = None

    
    class InferenciaAWP:
        lista_contatos: list = list()
        contato: str
        mensagem: str


    def __drive_config(self):
        # Abertura padrão do Selenium. 
        servico = Service(ChromeDriverManager().install())  
        self.drive = webdriver.Chrome(service=servico)
        self.drive.maximize_window()
        self.drive.get(r'https://web.whatsapp.com/')
        self.marktime = WebDriverWait(self.drive, 90)

    
    def conexao(self, popup=False):
        self.__drive_config()     

        # Aguardo na realização do login com QR Code
        var_aux_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        while True:
            try:
                self.drive.find_element(By.XPATH, var_aux_xpath)
                self._get_logging('Conexao Efetuada.')
                
                match popup:
                    case True:
                        messagebox.showinfo('Validado','Conexao Efetuada!')
                    case False:
                        pass
                break
            except:
                self._get_logging('Aguardando Login via QR Code...')
                t.sleep(5)

        self.flag_conection = True              


    def desconectar(self):
        self._get_logging('Desconectando Whatsapp...')

        # xpath para abrir os botões de opção, identificar as opções e confirmar respectivamente
        dc_xpath_abrir = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
        dc_xpath_opcoes = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div'
        dc_xpath_confirmar = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div'
        
        # clicar nos botões de opção
        self.drive.find_element(By.XPATH, dc_xpath_abrir).click()
        t.sleep(1)
        
        opcoes = self.drive.find_element(By.XPATH, dc_xpath_opcoes)
        lista_opcoes = opcoes.find_elements(By.TAG_NAME, 'li')
        t.sleep(1)

        # encontrar a opção de desconetar e clicar nela
        for item in lista_opcoes:
            if item.get_attribute('data-testid') == 'mi-logout menu-item':
                item.click()

        # confirmar desconexão
        self.drive.find_element(By.XPATH, dc_xpath_confirmar).click()
    
        
        self.drive.close()
        self._get_logging('Whatsapp Encerrado')        
       

    def __informacoes_contato_acessado(self): # método 'Generator' usado para coexistir com a classe AWPContato. Nela, será usada para alcançar os dados do contato acessado.
        xpath_aux = '//*[@id="main"]/header/div[2]/div/div'
        self._marktime_func(xpath_aux)

        
        while True:
            # Etapa 1
            ctt = self.drive.find_element(By.XPATH, xpath_aux)
            nome = ctt.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span[1]').text

            self.InferenciaAWP.contato = nome
            self.InferenciaAWP.lista_contatos.append(nome)
            yield 1
            
            
            # Etapa 2
            self._get_logging(f"Atual Contato: {self.InferenciaAWP.contato}")
            self._get_logging(f"Lista de contatos acessados nesta instância: ({' — '.join(self.InferenciaAWP.lista_contatos)})")
            yield 2


    def _flag_status(self):
        return self.flag_conection


    def _get_logging(self, item_log):
        logging.info(item_log) 
        
        
    def _marktime_func(self, objeto):
        res = self.marktime.until(
                    EC.presence_of_element_located(
                        (By.XPATH, objeto)
                        )
                    )
        return res
    
    
    def _tratamento_log_func(self, metodo):
        return f'{__class__.__name__}'+'.'+f'{metodo.__name__}'+'()'


