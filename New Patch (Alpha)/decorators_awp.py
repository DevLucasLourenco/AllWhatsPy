from errors_awp import AWPConnectionError
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)


def eventual_erro(func):
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)

        except AWPConnectionError:
            raise AWPConnectionError

        except (Exception, NoSuchElementException, UnexpectedAlertPresentException) as e:
            self.objeto_awp._get_logging(f'Ocorreu um erro durante a execução de {f"{self.objeto_awp.atual_funcao}"} — Erro: {e}. Tempo de Execução AWP: {self.objeto_awp.tempo_execucao}')
            self.objeto_awp._get_logging(f"{'':=^40}")
            raise
    return wrapper


def aprovarConexao(func):
    @eventual_erro
    def wrapper(self, *args, **kwargs):
        if self.objeto_awp._flag_status():
            self.objeto_awp._alterar_funcao_em_execucao(f'AllWhatsPy.{func.__name__}()')
            
            self.objeto_awp._get_logging(f'AllWhatsPy.{func.__name__}() inicializou.')
            func(self, *args, **kwargs)
            self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} finalizou sua execução com êxito.')
            return
        raise AWPConnectionError
    return wrapper


def executarOrdemTeclas(func):
    def _ordenacao(self, ordem):
        acao = ActionChains(self.objeto_awp._drive)
        for t in ordem:
            acao.key_down(t)
        
        time.sleep(0.5)
        acao.perform()
        time.sleep(0.5)    
            
    def wrapper(self, *args, **kwargs):
        run = func(self, *args, **kwargs)
        _ordenacao(self, run)
        
        next(self.objeto_awp._generator_info_contato_acessado)
        next(self.objeto_awp._generator_info_contato_acessado)
        
    return wrapper


def PseudoAWP(func):
    def validacao_dados(self):
        ...
        
    def wrapper(self, *args, **kwargs):
        inf = func(self, *args, **kwargs)
    return wrapper

    #aqui colocar parâmeetros para serem usados. O usuário enviará através de uma função os dados.
    #ex:
    # @ExecutarAWPPadronizacao
    # def run():
    #    dicio = {
    #        objeto : self,
    #        iter_ctt : [],
    #        mensagem : '',
    #        metodo : '',
    #    }
    #    return dicio


