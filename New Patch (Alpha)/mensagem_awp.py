import os
import requests
import time
from urllib import parse
from decorators_awp import aprovarConexao
from errors_awp import AWPConnectionError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException)


class AWPMensagem():
    
    def __init__(self, objeto):
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')
        self.localizacao = Endereco
        self.anexo = Anexo(self.objeto_awp)


    @aprovarConexao
    def enviar_mensagem(self, mensagem: str):
        if isinstance(mensagem, int) or isinstance(mensagem, float):
            mensagem = str(mensagem)

        self.objeto_awp.InferenciaAWP.mensagem = mensagem
        textbox = self.objeto_awp._ArmazemXPATH.textbox_xpath

        if isinstance(mensagem, list):        
            mensagem = '\n'.join(mensagem)

        self.objeto_awp._drive.find_element(By.XPATH,textbox).send_keys(mensagem,Keys.ENTER)         
        self.objeto_awp._get_logging(f'Mensagem enviada para {self.objeto_awp.InferenciaAWP.contato}')

        if len(self.objeto_awp.InferenciaAWP.mensagem) > 35:
            self.objeto_awp._get_logging(f'Mensagem: {self.objeto_awp.InferenciaAWP.mensagem[:35]}[...]')
        else:
            self.objeto_awp._get_logging(f'Mensagem: {self.objeto_awp.InferenciaAWP.mensagem[:35]}')
            
        time.sleep(1)


    @aprovarConexao
    def enviar_mensagem_paragrafada(self, mensagem: str):
        self.objeto_awp.InferenciaAWP.mensagem = mensagem

        textbox = self.objeto_awp._marktime_func(self.objeto_awp._ArmazemXPATH.textbox_xpath)
        textbox.click()

        if isinstance(mensagem, list):
            mensagem = '\n'.join(mensagem)
            
        for linha in mensagem.split('\n'):
            textbox.send_keys(linha)
            ActionChains(self.objeto_awp._drive).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()

        textbox.send_keys(Keys.ENTER)
        
        self.objeto_awp._get_logging(f'Mensagem enviada para {self.objeto_awp.InferenciaAWP.contato}')
        
        if len(self.objeto_awp.InferenciaAWP.mensagem) > 35:
            self.objeto_awp._get_logging(f'Mensagem: {self.objeto_awp.InferenciaAWP.mensagem[:35]}[...]')
        else:
            self.objeto_awp._get_logging(f'Mensagem: {self.objeto_awp.InferenciaAWP.mensagem[:35]}')
            
        time.sleep(1)


    @aprovarConexao
    def enviar_mensagem_por_link(self, numero, texto):
        self.objeto_awp.InferenciaAWP.mensagem = texto

        texto =  parse.quote(texto)
        link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
        self.objeto_awp._drive.get(link)
        
        textbox = self.objeto_awp._marktime_func(self.objeto_awp._ArmazemXPATH.textbox_xpath)
        textbox.send_keys(Keys.ENTER)

        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)


    @aprovarConexao
    def enviar_mensagem_direta(self, contato, mensagem: str, selecionar_funcao: int = 1, salvo: bool = True):

        if salvo:
            self.objeto_awp.ctt.encontrar_contato(contato)
        else:        
            self.objeto_awp.ctt.encontrar_usuario(contato)
            
        
        if selecionar_funcao == 1:
            self.objeto_awp.msg.enviar_mensagem(mensagem)
        
        elif selecionar_funcao == 2:
            self.objeto_awp.msg.enviar_mensagem_paragrafada(mensagem)

        else:
            raise ValueError('Valor informado incoerente.')


    def _validar_envio(self): #verifica se a mensagem foi enviada.
        ...
        


class Enquete(AWPMensagem):
    def __init__(self) -> None:
        ...



class Endereco(AWPMensagem):

    def __init__(self, cep: int):
        self.link = 'https://viacep.com.br/ws/{}/json/'
        self.cep = Endereco.tratamento_cep(cep)
        self.run()
    

    @staticmethod
    def tratamento_cep(item):
        item = str(item)
        if '-' in item:
            item =  item.replace('-','')
        
        if '.' in item:
            item = item.replace('.','')

        if len(item) == 8:
            return item


    def run(self):
        try:
            requisicao = requests.get(self.link.format(self.cep)).json()
            rua = requisicao['logradouro'] 
            cidade = requisicao['localidade'] 
            bairro = requisicao['bairro'] 
            uf = requisicao['uf'] 

            self.dados = requisicao, rua, cidade, bairro, uf
            
        except requests.JSONDecodeError:
            raise ValueError("Insira um CEP válido")


    def retornar(self):
        return self.dados


class Anexo():

    def __init__(self, objeto) -> None:
        self.objeto_awp = objeto


    @aprovarConexao
    def enviar_imagem(self, item, mensagem):   # correção.
        item = os.path.realpath(item)
        self.__encontrar_botao_anexo_XPATH()
            
        arquivo = self.objeto_awp._drive.find_element(By.CSS_SELECTOR, "input[type='file']")
        arquivo.send_keys(item)
        time.sleep(2)

        self.__enviar_anexo_XPATH(mensagem)
    
    @aprovarConexao
    def enviar_arquivo(self, nome_arquivo):     ## necessita correção!!!!!!!!!!!!!
        filename = os.path.realpath(nome_arquivo)
        self.__encontrar_botao_anexo_XPATH()

        self.objeto_awp.marktime('//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')
        document_button = self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')
        document_button.send_keys(filename)

        self.__enviar_anexo_XPATH()


    @aprovarConexao
    def __encontrar_botao_anexo_XPATH(self):
        botão_anexo_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
        self.objeto_awp._drive.find_element(By.XPATH, botão_anexo_xpath).click()
        time.sleep(2)
        
        
    @aprovarConexao
    def __enviar_anexo_XPATH(self, *msg):
        inputbox_xpath = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p'
        if msg:
            self.objeto_awp._drive.find_element(By.XPATH, inputbox_xpath).send_keys(msg, Keys.ENTER)
        else:
            self.objeto_awp._drive.find_element(By.XPATH, inputbox_xpath).send_keys(Keys.ENTER)
        time.sleep(1)