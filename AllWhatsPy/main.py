from .audio_awp import AWPAudio
from .contatos_awp import AWPContatos
from .mensagem_awp import AWPMensagem
from .criptografia_awp import AWPCriptografia, LogAWPC
from .utilidades_awp import AWPUtilidades
from .decorators_awp import PseudoAWP
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import os
import logging
import time 
import json


class AllWhatsPy:
    __tempo_inicial = time.time()
    flag_connection = False

    def __init__(self, inicializarTitulo:bool=True, realizar_log:bool=True, JSON_file:bool=True):
        self.JSON_file = JSON_file
        self.realizar_log = realizar_log
        self._inicializador_log()
        
        AllWhatsPy.__tituloAWP(inicializarTitulo)
        self._get_logging(f"{' AllWhatsPy - AWP ':=^40}")
        
        self.ctt = AWPContatos(self)
        self.msg = AWPMensagem(self)
        self.audio = AWPAudio(self)
        self.utilidade = AWPUtilidades(self)
        self.criptografia = AWPCriptografia(self, self.realizar_log)
        
        self._generator_info_contato_acessado = self.__informacoes_contato_acessado()

        self.show_off = None
        self._drive = None
        self._marktime = None
        self.atual_funcao = None
        self.funcoes_utilizadas: list = list()
        self.dados_nome_usuario = os.getlogin()


    def __del__(self):
        self.__JSON_execucao()
        self._get_logging(f'Tempo de Execução AWP: {self.tempo_execucao}')
        self._get_logging(f"{'':=^40}")

    
    class InferenciaAWP:
        lista_contatos: list = list()
        contato: str = ''
        mensagem: str = ''
        contatosInexistentes: list = list()
        contato_acessivel: bool


    class _ArmazemXPATH:
        textbox_xpath: str = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        var_aux_xpath: str = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        var_aux2_xpath: str = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'


    @property 
    def tempo_execucao(self):  
        return f'{time.time()-AllWhatsPy.__tempo_inicial:.4f}s'
        

    @staticmethod
    def __tituloAWP(item):
        if item:
            print(f"{' AllWhatsPy - AWP ':=^40}")
            print('https://github.com/DevLucasLourenco/AllWhatsPy')


    def conexao(self, show_off:bool=True, server_host: bool=False, popup=False, calibragem: tuple[bool, int]=(True, 10)):
        self.__driveConfigGoogle(server_host, show_off)

        while True:
            try:
                self._drive.find_element(By.XPATH, self._ArmazemXPATH.var_aux_xpath)

                if server_host:
                    self._get_logging(f'Conexão por Server efetuada.')
                    self._get_logging(f'<Nome da Pasta: AllWhatsPyHost> | <Usuário: {self.dados_nome_usuario}>')

                else:
                    self._get_logging('Conexao Efetuada.')
        
                if popup:
                        messagebox.showinfo('Validado','Conexão Efetuada!')
                
                self.__config_calibragem(calibragem)
                break

            except:
                self._get_logging('Aguardando Login...')
                time.sleep(5)

        self.flag_connection = True              
        
    
    def desconectar(self):
        self._get_logging('Desconectando Whatsapp...')

        # xpath para abrir os botões de opção, identificar as opções e confirmar respectivamente
        dc_xpath_abrir = '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span'
        dc_xpath_opcoes = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div'
        dc_xpath_confirmar = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div'
        
        # clicar nos botões de opção
        self._drive.find_element(By.XPATH, dc_xpath_abrir).click()
        time.sleep(1)
        
        opcoes = self._drive.find_element(By.XPATH, dc_xpath_opcoes)
        lista_opcoes = opcoes.find_elements(By.TAG_NAME, 'li')
        time.sleep(1)

        # encontrar a opção de desconetar e clicar nela
        for item in lista_opcoes:
            if item.get_attribute('data-testid') == 'mi-logout menu-item':
                item.click()

        # confirmar desconexão
        self._drive.find_element(By.XPATH, dc_xpath_confirmar).click()
    
        self._drive.close()
        self._get_logging('Whatsapp Encerrado')    


    def explodir_server(self):
        #if server no local:
            #deletar
        ...

    def _IncorporarMediaTempo(self): # func para calcular o tempo médio para cada ação tomada no algoritmo e disponibilisar um .log com estas informações Ex.: MediasAWP.log
        ...        


    def __informacoes_contato_acessado(self): # método 'Generator' usado para coexistir com a classe AWPContato. Nela, será usada para alcançar os dados do contato acessado.
        xpath_aux = '//*[@id="main"]/header'
        self._marktime_func(xpath_aux)

        while True:
            # Etapa 1
            ctt_dados = self._drive.find_element(By.XPATH, xpath_aux)
            nome = ctt_dados.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div').text 

            self.InferenciaAWP.contato = nome
            self.InferenciaAWP.lista_contatos.append(nome)
            yield 
            
            # Etapa 2
            self._get_logging(f"   Atual Contato: {self.InferenciaAWP.contato}")
            self._get_logging(f"   Lista de contatos acessados nesta instância: ({'; '.join(self.InferenciaAWP.lista_contatos)})")
            yield 


    def __driveConfigGoogle(self, validacao_server, show_off):        
        os.environ['WDM_LOG'] = '0'
        servico = Service(ChromeDriverManager().install())  
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])

        if validacao_server:
            options.add_argument(f'user-data-dir=C://users/{self.dados_nome_usuario}/AllWhatsPyHost')
            
        self._drive = webdriver.Chrome(service=servico, options=options)
        self._drive.maximize_window() if show_off else self._drive.minimize_window()
        self._drive.get(r'https://web.whatsapp.com/')
        self._marktime = WebDriverWait(self._drive, 90)


    def __JSON_execucao(self):
        if self.JSON_file:
                _nome_funcoes_set_pre_erro = list(set(self.funcoes_utilizadas))
                _lista_contatos_set_pre_erro = list(set(self.InferenciaAWP.lista_contatos))

                try:
                    dict_para_json: dict = {
                        "Lib": __class__.__name__,
                        "UsuarioAWP": self.dados_nome_usuario,
                        "Contatos": {
                            "Contatos Acessados Unitariamente": _lista_contatos_set_pre_erro,
                            "Contatos Acessados - Ordenado por Execucao": self.InferenciaAWP.lista_contatos,
                            "Contatos Inexistentes": self.InferenciaAWP.contatosInexistentes,
                        },
                        "Mensagem": self.InferenciaAWP.mensagem,
                        "Funcoes": {
                            "Ultima Funcao": self.atual_funcao,
                            "Usuario - Funcoes Utilizadas": _nome_funcoes_set_pre_erro,
                            "Usuario - Funcoes Utilizadas - Ordenado por Execucao": self.funcoes_utilizadas,
                        },
                        "Criptografia": LogAWPC.todas_criptografias,
                        "Tempo Execucao": self.tempo_execucao
                    }

                    json_exportar: dict = json.dumps(dict_para_json, indent=4)
                    with open("AWP.json", "w", encoding='utf-8') as file:
                        file.write(json_exportar)

                    self._get_logging('Arquivo JSON criado.')
                    
                except Exception as e:
                    self._get_logging(f'Falha na criação do arquivo JSON. Erro: {e}')
    

    def __config_calibragem(self, calibragem):
        if isinstance(calibragem, tuple) or isinstance(calibragem, list):
            if calibragem[0]:
                self._get_logging(f'Aguardando {calibragem[1]} segundos para calibragem.')
                time.sleep(calibragem[1])

        elif isinstance(calibragem, bool):
            if not calibragem:
                pass
            else:
                time.sleep(10)
        else:
            raise ValueError('Insira um valor válido para o parâmetro calibragem')


    def _flag_status(self):
        return self.flag_connection


    def _inicializador_log(self):
        if self.realizar_log:
            logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='eventAWP.log', format='%(asctime)s - %(levelname)s - %(message)s')


    def _get_logging(self, item_log):
        if self.realizar_log:
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


    def _alterar_funcao_em_execucao(self, atual_funcao):
        self.atual_funcao = atual_funcao
        self.funcoes_utilizadas.append(atual_funcao)