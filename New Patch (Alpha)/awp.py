
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
    flag_conection = False
    
    def __init__(self, dependencia_mensagem, dependencia_contato, dependencia_audio, dependencia_criptografia):
        self.mensagem = ...
        self.contato = ...
        
        self.lista_teste = list()
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = dependencia_mensagem(self) 
        self.ctt = dependencia_contato(self) 
        self.audio = dependencia_audio(self)
        self.criptografia = dependencia_criptografia

    @staticmethod
    def analise_if_correct(item, checagem='mensagem'):
        item_nome = item.__name__
        
        if checagem == 'mensagem':
            if item_nome == "AWPMensagem":
                return item
            
            raise ValueError(f'Erro na indicação de Dependencia AWP\nDependencia: AWPMensagem\nInformado: {item}')
        
        
        elif checagem == 'contato':
            if item_nome == "AWPContatos":
                return item
            
            raise ValueError(f'Erro na indicação de Dependencia AWP\nDependencia: AWPContato\nInformado: {item}')
        
        
        elif checagem == 'audio':
            if item_nome == "AWPAudio":
                return item
            
            raise ValueError(f'Erro na indicação de Dependencia AWP\nDependencia: AWPAudio\nInformado: {item}')
        
        
        elif checagem == 'criptografia':
            if item_nome == "AWPCriptografia":
                return item
    
            raise ValueError(f'Erro na indicação de Dependencia AWP\nDependencia: AWPCriptografia\nInformado: {item}')
        
        
        else:
            raise RuntimeError('Especifique um tipo de checagem')


    def testando(self):
        print('de awp executando em mensagem')
        
        
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






        


