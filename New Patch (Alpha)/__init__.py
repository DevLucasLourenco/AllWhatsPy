from audio_awp import AWPAudio
from contatos_awp import AWPContatos
from mensagem_awp import AWPMensagem
from criptografia_awp import AWPCriptografia
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
    flag_conection = False
    
    def __init__(self):
        self.__mensagem = None
        self.__contato = None
        
        
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self)
        self.ctt = AWPContatos(self)
        self.audio = AWPAudio(self)
        self.criptografia = AWPCriptografia
    
        self.drive = None
        self.marktime = None
        

    def __login_requisicao(self):
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C://user/AllWhatsPyProfile')


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
                logging.info('Conexao Efetuada!')
                
                match popup:
                    case True:
                        messagebox.showinfo('Validado','Conexao Efetuada!')
                    case False:
                        pass
                break
            except:
                logging.info('Aguardando Login via QR Code...')
                t.sleep(5)

        self.flag_conection = True       
        

    def __informacoes_contato_acessado(self): # método 'Generator' usado para coexistir com a classe AWPContato. Nela, será usada para alcançar os dados do contato acessado.
        xpath = ...
        while True:
            # Etapa 1
            dados = ... # drive.find_element(By.XPATH, xpath).text
            print('info1')
            yield 1
            
            # Etapa 2
            self.__lista_informacoes_contato_aberto.append(dados)
            print('info2')
            yield 2


    def flag_status(self):
        return AllWhatsPy.flag_conection


    def get_logging(self, item_log):
        logging.info(item_log)
        
        
