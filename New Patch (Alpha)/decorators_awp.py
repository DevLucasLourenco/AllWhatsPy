from errors_awp import AWPConnectionError
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
            if self.objeto_awp._flag_status():
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} finalizou sua execução com êxito.')
            else:
                self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} encontrou uma falha na execução.')
    return wrapper


def conexaoVariante(func):
    def server_login(self, popup: bool = False):
        dados_nome_usuario = os.getlogin()
        os.environ['WDM_LOG'] = '0'
        
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir=C://users/{dados_nome_usuario}/AllWhatsPyHost')
        
        servico = Service(ChromeDriverManager().install())
        self._drive = webdriver.Chrome(service=servico, options=options)
        
        self._drive.maximize_window()
        self._drive.get(r'https://web.whatsapp.com/')
        self._marktime = WebDriverWait(self._drive, 90)
        
        
        while True:
            try:
                self._drive.find_element(By.XPATH, self._ArmazemXPATH.var_aux_xpath)

                self._get_logging(f'Conexão por Server efetuada.')
                self._get_logging(f'<Nome da Pasta: AllWhatsPyHost> | <Usuário: {dados_nome_usuario}>')
                
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
    

    def wrapper(self,*args, **kwargs):
        run = func(self,*args, **kwargs)
        l = next(run)
        if l[0]:
            server_login(self, l[1])
            return
        next(run)
        
    return wrapper
