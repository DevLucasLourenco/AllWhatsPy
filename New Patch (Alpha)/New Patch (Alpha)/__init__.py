
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
from audio_awp import AWPAudio
from contatos_awp import AWPContatos
from mensagem_awp import AWPMensagem
from criptografia_awp import AWPCriptografia



class AllWhatsPy: 
    flag_conection = False
    
    def __init__(self):
        self.__mensagem = None
        self.__contato = None
        
        self.__LOGGER = None
        
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AWPMensagem(self)
        self.ctt = AWPContatos(self)
        self.audio = AWPAudio(self)
        self.criptografia = AWPCriptografia

        
    def conexao(self):
        self.flag_conection = True

        
        
    def exportar_txt(objeto): # qual atributo a pessoa decidir
        ...
        

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