from errors_awp import AWPConnectionError
import time
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
)


def eventual_erro(func):
    def wrapper(self, *args, **kwargs):
        try:
            f = func(self, *args, **kwargs)
            return f
            
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
            f = func(self, *args, **kwargs)
            self.objeto_awp._get_logging(f'{self.objeto_awp._tratamento_log_func(func)} finalizou sua execução.')
            return f
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
    def _deteccao_metodo(obj, item):
        metodo_resolucao = {
                "EM" : obj.msg.enviar_mensagem,
                "EMP" : obj.msg.enviar_mensagem_paragrafada, ## necessário correção. manda todas as msgs para uma única pessoa. (mt importante!!!)
                }
        try:
            return metodo_resolucao[item]
            
        except KeyError:
            raise KeyError(f"Método não aceito. Opções: {', '.join(list(metodo_resolucao.keys()))}") 


    def validacao_dados(dicio: dict):
        relacao = {
                "objeto" : None,
                "iter_ctt": None,
                "mensagem" : None,
                "metodo" : "EMP",
                "calibragem" : [True, 10],
                "server_host" : True,
        }
        if isinstance(dicio, dict):
            objeto = dicio.get('objeto')
            lista_contatos = dicio.get('iter_ctt')
            mensagem = dicio.get('mensagem')
            metodo = _deteccao_metodo(objeto, dicio.get('metodo'))

            relacao.update(dicio)
            return relacao #prototipo!! revisar tudo 
            
        else:
            raise TypeError(f'O objeto {dicio.__name__} do tipo {type(dicio)} é inválido. Passe um objeto do tipo dict para o parâmetro requisitado.')
        
    def wrapper(*args, **kwargs):

        inf = func(*args, **kwargs)
        inf = validacao_dados(inf)
        objeto, lista_contatos, mensagem, metodo = inf
        
        alfabeto_maiusculo = [l for l in string.ascii_uppercase]
        alfabeto_minusculo = [l for l in string.ascii_lowercase]

        objeto.conexao(server_host=True, popup=False, calibragem=[True, 10])
        for ctt in lista_contatos:
            if (alfabeto_maiusculo in ctt) or (alfabeto_minusculo in ctt):
                objeto.ctt.encontrar_contato(ctt)    
            else:
                objeto.ctt.encontrar_usuario(ctt)
                
            if objeto.InferenciaAWP.contato_acessivel:
                metodo(mensagem)
                
    return wrapper
