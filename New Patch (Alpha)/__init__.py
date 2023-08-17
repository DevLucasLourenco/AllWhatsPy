from audio_awp import AWPAudio
from contatos_awp import AWPContatos
from mensagem_awp import AWPMensagem
from criptografia_awp import AWPCriptografia
from utilidades_awp import AWPUtilidades
from errors_awp import AWPConnectionError
from decorators_awp import aprovarConexao, conexaoVariante
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
import time 



class AllWhatsPy: 
    logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='eventAWP.log', format='%(asctime)s - %(levelname)s - %(message)s')
    flag_conection = False
    
    
    def __init__(self, inicializarTitulo:bool=True):
        AllWhatsPy.__tituloAWP(inicializarTitulo)
        self._get_logging(f"{' AllWhatsPy - AWP ':=^40}")
        
        
        self.ctt = AWPContatos(self)
        self.msg = AWPMensagem(self)
        self.audio = AWPAudio(self)
        self.utilidade = AWPUtilidades(self)
        self.criptografia = AWPCriptografia(self)
    
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
    
        self._drive = None
        self._marktime = None

    
    class InferenciaAWP:
        lista_contatos: list = list()
        contato: str
        mensagem: str
        contatosInexistentes: list = list()


    class _ArmazemXPATH:
        textbox_xpath: str = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        var_aux_xpath: str = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        var_aux2_xpath: str = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'


    @staticmethod
    def __tituloAWP(item):
        if item:
            print(""" ========== AllWhatsPy-AWP ==========""")
            print('https://github.com/DevLucasLourenco/AllWhatsPy')


    @conexaoVariante
    def conexao(self, server_host: bool=False, popup=False, calibragem: tuple[bool, int]=(True, 10)): # Método "Generator" para conexão.
        yield server_host, popup, calibragem
        
        self.__driveConfigGoogle()     
        # Aguardo na realização do login com QR Code
        while True:
            try:
                self._drive.find_element(By.XPATH, self._ArmazemXPATH.var_aux_xpath)
                self._get_logging('Conexao Efetuada.')
                
                if popup:
                        messagebox.showinfo('Validado','Conexão Efetuada!')
                
                self.__config_calibragem(calibragem)
                break

            except:
                self._get_logging('Aguardando Login via QR Code...')
                t.sleep(5)

        self.flag_conection = True              
        yield


    def desconectar(self):
        self._get_logging('Desconectando Whatsapp...')

        # xpath para abrir os botões de opção, identificar as opções e confirmar respectivamente
        dc_xpath_abrir = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
        dc_xpath_opcoes = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div'
        dc_xpath_confirmar = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div'
        
        # clicar nos botões de opção
        self._drive.find_element(By.XPATH, dc_xpath_abrir).click()
        t.sleep(1)
        
        opcoes = self._drive.find_element(By.XPATH, dc_xpath_opcoes)
        lista_opcoes = opcoes.find_elements(By.TAG_NAME, 'li')
        t.sleep(1)

        # encontrar a opção de desconetar e clicar nela
        for item in lista_opcoes:
            if item.get_attribute('data-testid') == 'mi-logout menu-item':
                item.click()

        # confirmar desconexão
        self._drive.find_element(By.XPATH, dc_xpath_confirmar).click()
    
        
        self._drive.close()
        self._get_logging('Whatsapp Encerrado')        


    def explodir_server(self):
        ... 
        

    def __informacoes_contato_acessado(self): # método 'Generator' usado para coexistir com a classe AWPContato. Nela, será usada para alcançar os dados do contato acessado.
        xpath_aux = '//*[@id="main"]/header/div[2]/div/div'
        self._marktime_func(xpath_aux)

        
        while True:
            # Etapa 1
            ctt = self._drive.find_element(By.XPATH, xpath_aux)
            nome = ctt.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span[1]').text

            self.InferenciaAWP.contato = nome
            self.InferenciaAWP.lista_contatos.append(nome)
            yield 
            
            
            # Etapa 2
            self._get_logging(f"Atual Contato: {self.InferenciaAWP.contato}")
            self._get_logging(f"Lista de contatos acessados nesta instância: ({'; '.join(self.InferenciaAWP.lista_contatos)})")
            yield 


    def __driveConfigGoogle(self):
        os.environ['WDM_LOG'] = '0'
        servico = Service(ChromeDriverManager().install())  

        self._drive = webdriver.Chrome(service=servico)
        self._drive.maximize_window()
        self._drive.get(r'https://web.whatsapp.com/')
        self._marktime = WebDriverWait(self._drive, 90)
    

    def __config_calibragem(self, calibragem):
        if isinstance(calibragem, tuple) or isinstance(calibragem, list):
            if calibragem[0]:
                self._get_logging(f'Aguardando {calibragem[1]} segundos para calibragem.')
                time.sleep(calibragem[1])
            else:
                pass
        elif isinstance(calibragem, bool):
            if not calibragem:
                pass
            else:
                time.sleep(10)
        else:
            raise ValueError('Insira um valor válido para o parâmetro calibragem')


    def _flag_status(self):
        return self.flag_conection


    def _get_logging(self, item_log):
        logging.info(item_log) 
        
        
    def _marktime_func(self, objeto):
        res = self._marktime.until(
                    EC.presence_of_element_located(
                        (By.XPATH, objeto)
                        )
                    )
        return res
    
    
    def _tratamento_log_func(self, metodo):
        return f'{__class__.__name__}'+'.'+f'{metodo.__name__}'+'()'
