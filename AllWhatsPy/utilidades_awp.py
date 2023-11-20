from .decorators_awp import aprovarConexao
import time
import locale
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)



class AWPUtilidades:
    def __init__(self, objeto) -> None:
        self.objeto_awp = objeto
        self.objeto_awp._get_logging(f'{__class__.__name__} obteve êxito.')
        locale.setlocale(locale.LC_TIME,'pt_BR')
        


    @aprovarConexao
    def arquivar_chat(self):
        ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
                                                             Keys.SHIFT).send_keys('e').perform()
        
        self.objeto_awp._get_logging(f'    {self.objeto_awp.InferenciaAWP.contato} foi arquivado.')
        time.sleep(1)
        
        
    @aprovarConexao
    def Schedule(self, ano_aguardado:int=None, mes_aguardado:int=None, dia_aguardado:int=None, 
                 hora_aguardado:int=None, minuto_aguardado:int=None):
        
        agora = datetime.now()
        
        schedule_time = {
            'ano':ano_aguardado if ano_aguardado != None else agora.year,
            'mes':mes_aguardado if mes_aguardado != None else agora.month,
            'dia':dia_aguardado if dia_aguardado != None else agora.day,
            'hora':hora_aguardado if hora_aguardado != None else agora.hour,
            'minuto':minuto_aguardado if minuto_aguardado != None else agora.minute,
        }
        
        
        data_programada = datetime(schedule_time.get('ano'), schedule_time.get('mes'), schedule_time.get('dia'),
                                   schedule_time.get('hora'), schedule_time.get('minuto'))
        dif_aguarde = (data_programada - agora).seconds
        
        
        if data_programada > agora:
            self.objeto_awp._get_logging(f'    No aguardo da hora programada...| {dif_aguarde}s até o final do agendamento. — {data_programada.strftime("%A, %d/%m/%Y, %H:%M")}|')
            time.sleep(dif_aguarde)
        else:
            self.objeto_awp._get_logging(f'    Horário agendado ultrapassado.')
        
        return data_programada.strftime("%A, %d/%m/%Y, %H:%M")

    @aprovarConexao
    def agendamento(self, dia_programado: str, hora_programado: str, minuto_programado: str):
        '''
        Descontinuado
        '''
        
        def adaptar_item(item):
            if item < 10:
                return '0' + str(item)
            return str(item)  
        
        
        for each in [dia_programado, hora_programado, minuto_programado]:
            if not isinstance(each, str):
                raise TypeError('Parâmetros de tipos diferentes de <str> não são aceitos.')

        while True:
            ano, mes, dia, hora, minuto, *_  = time.localtime()
            if adaptar_item(dia) == dia_programado:
                if adaptar_item(hora) == hora_programado:
                    if  adaptar_item(minuto) == minuto_programado:
                        break
            else:
                self.objeto_awp._get_logging(f'    No aguardo da hora programada...| Dia:{adaptar_item(dia_programado)}| Hora: {adaptar_item(hora)} | Minuto: {adaptar_item(minuto)}|')
                time.sleep(60)
                

    @aprovarConexao
    def marcar_como_nao_lida(self):
        ActionChains(self.objeto_awp._drive).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(
                                                             Keys.SHIFT).send_keys('u').perform()

        self.objeto_awp._get_logging(f'    {self.objeto_awp.InferenciaAWP.contato} foi marcado(a) como não lido(a).')
        time.sleep(1)


    @aprovarConexao
    def _comercial_ou_pessoal(self):
        try:
            self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="main"]/header').click()
            time.sleep(1)

            self.objeto_awp._drive.find_element(By.XPATH, '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/section/div[2]/div/div/div[2]/span')
            webdriver.ActionChains(self.objeto_awp._drive).send_keys(Keys.ESCAPE).perform()
            
            self.objeto_awp._get_logging(f'    {self.objeto_awp.InferenciaAWP.contato} é uma conta comercial')
            return "C"
        
        except NoSuchElementException as e:
            webdriver.ActionChains(self.objeto_awp._drive).send_keys(Keys.ESCAPE).perform()
            self.objeto_awp._get_logging(f'    {self.objeto_awp.InferenciaAWP.contato} é uma conta pessoal')
            return "P"
        