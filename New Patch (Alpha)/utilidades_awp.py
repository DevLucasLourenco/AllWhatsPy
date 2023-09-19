from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from decorators_awp import aprovarConexao
import time


class AWPUtilidades:
    def __init__(self, objeto) -> None:
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')


    @aprovarConexao
    def arquivar_chat(self):
        ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
                                                             Keys.SHIFT).send_keys('e').perform()
        
        self.objeto_awp._get_logging(f'{self.objeto_awp.InferenciaAWP.contato} foi arquivado.')
        time.sleep(1)


    @aprovarConexao
    def agendamento(self, dia_programado: str, hora_programado: str, minuto_programado: str):
        def adaptar_item(item):
            
            if item < 10:
                
                return '0' + str(item)
            else:
                return str(item)  

        while True:
            ano, mes, dia, hora, minuto, *_  = time.localtime()

            if adaptar_item(dia) == dia_programado:
                if adaptar_item(hora) == hora_programado:
                    if  adaptar_item(minuto) == minuto_programado:
                        break
                    
            else:
                self.objeto_awp._get_logging(f'No aguardo da hora programada...| Dia:{adaptar_item(dia_programado)}| Hora: {adaptar_item(hora)} | Minuto: {adaptar_item(minuto)}|')
                time.sleep(60)
                
    
    def marcar_como_nao_lida(self):
        ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
                                                             Keys.SHIFT).send_keys('u').perform()

        self.objeto_awp._get_logging(f'{self.objeto_awp.InferenciaAWP.contato} foi marcado(a) como não lido(a).')
        time.sleep(1)


    def _comercial_ou_pessoal(self):
        ...
        #função para ver se o contato é comercial ou pessoal (fácil, só comparar parametros que tem em um e no outro não)