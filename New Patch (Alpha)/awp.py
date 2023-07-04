
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
    
    def __init__(self, dependencia_mensagem: object, dependencia_contato: object, dependencia_audio: object, dependencia_criptografia: object):
        self.mensagem = ...
        self.contato = ...
        
        self.__lista_informacoes_contato_aberto = list()
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()
        
        self.msg = AllWhatsPy.if_dep_correta(dependencia_mensagem(self), checagem='mensagem')
        self.ctt = AllWhatsPy.if_dep_correta(dependencia_contato(self), checagem='contato')
        self.audio = AllWhatsPy.if_dep_correta(dependencia_audio(self), checagem='audio')
        self.criptografia = AllWhatsPy.if_dep_correta(dependencia_criptografia, checagem='criptografia')


    @staticmethod
    def if_dep_correta(item: object, checagem='mensagem'):
        
        if checagem == 'criptografia': # devido ao fato da classe AWPCriptografia não estar instanciada, é realizado esse tratamento especial para ela.
            
            item_nome = item.__name__
            if item_nome == "AWPCriptografia":
                return item
    
            raise ValueError(f'Erro na indicação de Dependencia AWP\nDependencia: AWPCriptografia\nInformado: {item}')
        
        else:
            # as demais classes estão sendo instanciadas, portanto é possível obter retorno de "type(obj).__name__" 
            item_nome = type(item).__name__
            
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
            
            else:
                raise RuntimeError('Especifique um tipo de checagem')

        
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