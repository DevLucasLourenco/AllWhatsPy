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
import os
import time as t
import logging
logging.basicConfig(level=logging.INFO, filename='event.log', format='%(asctime)s - %(levelname)s - %(message)s')



def conexao(popup: int = 1):

    '''
    Função responsável por estabelecer a conexão com o Whatsapp.
     Ela aguardará a realização do login ao QR Code para prosseguir com o
      restante do código.\n
    Por padrão, aparecerá um pop na tela aguardando você clicar no "OK"
     para liberar a progressão do código para as demais fórmulas, 
     entretanto, se você colocar o valor do argumento "popup" para 2, 
     não será exibido e o código dará continuidade sem interrupções\n
    OBS.: O popup por ser útil para nuâncias na conexão que impedem o
     Whatsapp de carregar totalmente.
    '''

    global marktime
    global drive
    

    # Abertura padrão do Selenium. 
    servico = Service(ChromeDriverManager().install())
    drive = webdriver.Chrome(service=servico)
    drive.maximize_window()
    drive.get(r'https://web.whatsapp.com/')
    marktime = WebDriverWait(drive, 90)
    

    # Aguardo na realização do login com QR Code
    var_aux_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    while True:
        try:
            drive.find_element(By.XPATH, 
                                   var_aux_xpath)
            
            logging.info('Conexao Efetuada!')
            
            if popup == 1:
                messagebox.showinfo('Validado','Conexao Efetuada!')
                
            elif popup == 2:
                pass
            break

        except:
            logging.info('Aguardando Login via QR Code...')
            t.sleep(5)



def desconectar(padrao: int = 1):

    '''
    Ao declarar um valor à variável "padrão", você estará indicando qual funcionalidade está sendo realizada. \n
    Caso seja 1, irá encerrar o Whatsapp e fechar a janela.
     Caso seja 2, irá encerrar o Whatsapp mas manterá a janela de QR Code aberta.
    '''

    # será reconhecido a maneira que a desconexão será realizada
    if padrao in [1, 2]:
        
        if padrao == 1:
            possibilidade_desconectar_e_fechar_janela()

        else:
            possibilidade_desconectar_e_manter_janela()
    
    else:
        logging.critical('Não foi possível realizar a desconexão. Valor inserido inválido')



def contato_nome():
    ctt = drive.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div')
    nome = ctt.find_element(By.CLASS_NAME, 'span').text

    return nome



def contato_registrar():

    '''
    Esta função é responsável por registrar o ultimo contato que estava aberto
     e armazená-lo.\n
    ATENÇÃO: Ainda que o computador desligue ou encerre todas as atividades, ainda estará registrado.
    '''

    dados_contato = pegar_dados_contato()
    arquivo_txt_mutavel_insercao('DadosArmazenado', dados_contato)

    logging.info(f'{dados_contato} foi registrado')
    logging.info('contato_registrar_ultimo_aberto() Terminou de Rodar')



def contato_abrir_registrado(padrao = 1):

    '''
    Esta função abrirá o ultimo contato registrado.\n
    Temos duas opções, dando o valor de 1 e 2 para a variável "padrao"\n 
    Por padrão, procurará pelo nome, mas segue as configurações:\n
    Caso seja 1, irá procurar pelo nome.
     Caso seja 2, irá procurar pelo número através do (wa.me)
    '''

    # tratamendo dos dados
    dados_contato = arquivo_txt_mutavel_leitura('DadosArmazenado')
    dados_contato = dados_contato.split(' - ')
    nome_contato, numero_contato = dados_contato
    numero_contato = numero_contato.replace('(','').replace(')','').replace('-','').replace(' ','').strip()

    # selenção da maneira em que irá abrir
    if padrao == 1:
        encontrar_contato(nome_contato)
    elif padrao == 2:
        encontrar_usuario(numero_contato)
    
    logging.info('contato_abrir_registrado() Terminou de Rodar')



def descer_chat_quantidade(quantidade: int):

    '''
    O intuito deste código é descer a quantidade declarada de chats até alcançar a desejada.
    '''
    
    searchhbox_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'

    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, searchhbox_xpath)
        )
    )


    searchhbox = drive.find_element(By.XPATH,searchhbox_xpath)
    searchhbox.send_keys(Keys.ARROW_DOWN)
    
    chat = drive.switch_to.active_element
    
    if quantidade != 1:
        for i in range(quantidade - 1):
            chat.send_keys(Keys.ARROW_DOWN)
            
    else:
        pass
    
    nome_conversa = chat.text.split('\n')[0]
    logging.info(f'Conversa Selecionada: {nome_conversa}')
    logging.info('descer_chat() Terminou de Rodar')
    chat.click()
    


def descer_conversa_origem_atual(quantidade: int = 1):

    '''
    Por padrão, não é necessário acrescentar nenhuma valor na quantidade, pois ele ja irá descer uma conversa por vez.
    '''

    # Sequência de comandos para fazer com que a conversa desça
    for i in range(quantidade):
        ActionChains(drive).key_down(Keys.CONTROL
                                        ).key_down(Keys.SHIFT
                                                    ).key_down(Keys.ALT
                                                            ).send_keys("]"
                                                                        ).perform()

    t.sleep(1)
    

    logging.info('descer_conversa_origem_atual() Terminou de Rodar!')



def subir_conversa_origem_atual(quantidade: int = 1):

    '''
    Por padrão, não é necessário acrescentar nenhuma valor na quantidade, pois ele ja irá subir uma conversa por vez.
    '''
    
    #Sequência  de comandos responsável por estar subindo a conversa atual
    for i in range(quantidade):
        ActionChains(drive).key_down(Keys.CONTROL
                                        ).key_down(Keys.SHIFT
                                                    ).key_down(Keys.ALT
                                                            ).send_keys("["
                                                                        ).perform()

    t.sleep(1)
    

    logging.info('subir_conversa_origem_atual() Terminou de Rodar!')



def encontrar_primeira_conversa(ignorar_fixado = True):

    '''
    Esta função será responsável por abrir a primeira conversa.
     Caso "ignorar_fixado" for True, ele irá verificar se há uma conversa fixada e pular a mesma.
    Se o valor de "ignorar_fixado" for False, irá selecionar o primeiro comentário fixado.
    '''
    
    try: 
        t.sleep(2)
        bar_pesq_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        bar_pesq = drive.find_element(By.XPATH, 
                                          bar_pesq_xpath)
        
        bar_pesq.click()
        bar_pesq.send_keys(Keys.ARROW_DOWN)
        
        chat = drive.switch_to.active_element
        t.sleep(1)

        # Irá verificar se a conversa que foi selecionada é uma das fixadas. 
        # Dependendo da informação dada à função, irá ou não ignorar.
        
        if ignorar_fixado:
            while True:
                
                alerta = False
                dados = chat.find_elements(By.TAG_NAME, "span")

                for item in dados:
                    
                    if "pinned" in item.get_attribute("innerHTML"):
                        alerta = True
                        break
                    

                if not alerta:
                    break
                
                chat.send_keys(Keys.ARROW_DOWN)
                chat = drive.switch_to.active_element
                
            else:
                pass

        nome_conversa = chat.text.split("\n")[0]
        logging.info(f'Conversa Selecionada: "{nome_conversa}"')
        chat.send_keys(Keys.ENTER)


    except Exception as bug:
           logging.info(f'O "Exception" apareceu enquanto encontrava a primeira conversa não fixada: {bug}')
   
    logging.info('encontrar_primeiro_conversa() Terminou de Rodar!')



def encontrar_usuario(destino):

    '''
    Esta função é para contatos não salvos\n Ou para procurar pelo número através da API de procura do Wwhatsapp
    destino = O número do contato o qual você quer abrir a conversa
    '''
    
    # procurará o usuário por link 
    drive.get(f'https://web.whatsapp.com/send?phone={destino}')
    searchbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    
    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, searchbox_xpath)
            )
        )
    
    searchbox = drive.find_element(By.XPATH, 
                                   searchbox_xpath
                                                )
    
    searchbox.click()
    
    logging.info(f'{destino} Encontrado')
    logging.info('encontrar_usuario() Terminou de Rodar!')
            


def encontrar_contato(destino):

    '''
    Esta função é para contatos salvos.\n
    destino = um nome ou número do contato salvo o qual você deseja abrir a conversa
    '''
    
    # procurará pelos contaros salvos 
    try:
        bar_pesq_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
        drive.find_element(By.XPATH, bar_pesq_xpath).clear()
        
        drive.find_element(By.XPATH,
                                    bar_pesq_xpath
                                                ).send_keys(destino,
                                                                    Keys.ENTER)

        t.sleep(1)

        drive.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/span/button/span').click()


        logging.info(f'Contato Salvo Encontrado - {destino}')
        logging.info('encontrar_contato() Terminou de Rodar!')
        
    except:
        logging.warning(f'Contato {destino} Não Encontrado.')
     

     
def enviar_mensagem(mensagem):

    '''
    Esta função irá mandar uma mensagem atrás da outra, ao contrário da "enviar_mensagem_paragrafada()"\n
    que aloca tudo à uma única mensagem e envia no final\n
    mensagem = A mensagem a ser enviada após usar as funções de encontrar contato
    '''

    searchbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    try:
        
        if isinstance(mensagem, list):        
            mensagem = '\n'.join(mensagem)
            drive.find_element(By.XPATH,
                                   searchbox_xpath
                                   ).send_keys(mensagem,
                                               Keys.ENTER)
                                   
            logging.info('Mensagem Enviada')
            logging.info('enviar_mensagem_encadeada() Terminou de Rodar!')
            
        else:
            
            drive.find_element(By.XPATH, 
                                   searchbox_xpath
                                   ).send_keys(mensagem, 
                                               Keys.ENTER)
                                   
            
    except:
        logging.warning('Não foi possível enviar a mensagem')
        pass     
     
    logging.info('enviar_mensagem() Terminou de Rodar!')
        


def enviar_mensagem_paragrafada(mensagem: str):

    '''
    Esta função unifica a mensagem que é para ser enviada, ao contrário da "enviar_mensagem()"\n
    Ela faz com que, caso seja mais de uma linha de mensagem, envie-se uma única mensagem após uni-las\n
    mensagem = A mensagem a ser enviada após usar as funções de encontrar contato
    '''
    
    try:
        inputbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'

        marktime.until(EC.presence_of_element_located(
                                                    (By.XPATH, 
                                                    inputbox_xpath)
                                                                    ))
        
        input_box = drive.find_element(By.XPATH, inputbox_xpath)
        input_box.click()
        
        for linha in mensagem.split('\n'):
            input_box.send_keys(linha)
            ActionChains(drive).key_down(Keys.SHIFT
                                            ).key_down(Keys.ENTER
                                                        ).key_up(Keys.ENTER
                                                                ).key_up(Keys.SHIFT
                                                                        ).perform()
                                                                
        input_box.send_keys(Keys.ENTER)
    
        
    except (NoSuchElementException, Exception) as bug:
        logging.warning(f'Falha no envio da mensagem! - {bug}')
        
    finally:
        logging.info('enviar_mensagem_paragrafada() Terminou de Rodar!')



def enviar_mensagem_por_link(numero, texto):

    '''
    Esta função irá pegar uma funcionalidade do Whatsapp e irá fazer com que se envie através dela! 
    Não há a necessidade de usar o "encontrar_usuario()" ou "encontrar_contato()"
    OBS.: Não use esta função para enviar para muitas pessoas, senão poderá bloquear seu número. 
    
    '''
    
    # é enviada a mensagem utilizando o link do whatsapp
    texto = parse.quote(texto)
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    
    drive.get(link)



def enviar_mensagem_direta(contato, mensagem: str, selecionar_funcao: int = 1, salvo: bool = True):

    '''
    Ela fará com que todo o processo que teria que ser feito com as outras functions não seja necessário
     Tudo será feito por esta única.
    
    contato = O destino da mensagem, seja ela número ou nome.\n
    mensagem = A mensagem que será enviada ao contato.\n
    selecionar_função = Entre 1 e 2, serão as funções enviar_mensagem(), enviar_mensagem_paragrafada() respectivamente.\n
    salvo = Se for True, o contato deverá estar salvo, portanto, o argumemento contato deve ser um número que já está salvo no seu Whatsapp
     Caso contrário, se for False, usará o método por link, o qual deverá ser um número no argumento Contato
    '''


    # Esta é a maneira mais direta de estar realizando o envio de mensagem. Tudo feito em uma só
    if salvo:
        encontrar_contato(contato)
    else:        
        encontrar_usuario(contato)
        
    
    if selecionar_funcao == 1:
        enviar_mensagem(mensagem)
    
    elif selecionar_funcao == 2:
        enviar_mensagem_paragrafada(mensagem)
    
    else:
        messagebox.showinfo('Atenção!', 'Valor inserido está incorreto. Insira 1 ou 2')
        
    logging.info('enviar_mensagem_direta() Terminou de Rodar!')
    

    
def agendamento(dia_programado: str, hora_programado: str, minuto_programado: str):

    '''
    O código tem o intuito de aguardar até as especificações tornarem-se verídicas. 
     Feito isto, liberará os códigos após este à progressão das mesmas.
    '''

    while True:
        data_atual = t.localtime()
        ano, mes, dia, hora, minuto, *_ = data_atual
        
        if adaptar_item(dia) == dia_programado:
            if adaptar_item(hora) == hora_programado:
                if  adaptar_item(minuto) == minuto_programado:
                    logging.info('Aguardo perante o agendamento finalizado.')
                    break
                
        else:
            logging.info(f'No aguardo da hora programada...| Dia:{adaptar_item(dia_programado)}| Hora: {adaptar_item(hora)} | Minuto: {adaptar_item(minuto)}|')
            t.sleep(60)
            
    logging.info('agendamento() terminou de rodar!')


  
def encontrar_attach_XPATH():

    attach_xpath_button = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'   
    drive.find_element(By.XPATH, 
                           attach_xpath_button).click()
    
    t.sleep(5)
    
      
      
def enviar_attach_XPATH():

    inputbox_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'
    drive.find_element(By.XPATH, 
                           inputbox_xpath).send_keys(
                                                    Keys.ENTER)
    
    t.sleep(1)



def enviar_imagem(item):

    '''
    Função responsável pelo envio de imagens. \n
    Basta dizer o nome do arquivo juntamente à sua extensão.
     Ex: NomeArquivo.jpg
    '''
    
    item = os.path.realpath(item)
    
    encontrar_attach_XPATH()
        
    arquivo = drive.find_element(By.CSS_SELECTOR, 
                                     "input[type='file']")
    arquivo.send_keys(item)
    t.sleep(2)
    
    enviar_attach_XPATH()



def enviar_video(video):

    '''
    Checará se o tamanho do arquivo é compatível com o tamanho máximo de envio do 
     Whastapp e, após isso, irá enviar ao destinatário já antes encontrado.
     
    '''
    
    try:     
        nome_arquivo = os.path.realpath(video)
        tamanho_arquivo = os.path.getsize(nome_arquivo)
        x = converter_bytes_para(tamanho_arquivo, "MB")

        # Arquivo menor que 14MB
        if x < 14:
            encontrar_attach_XPATH()

            marktime.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input')
                )
            )
            
            video_button = drive.find_element(By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input')

            video_button.send_keys(nome_arquivo)
            
            
            enviar_attach_XPATH()
            
        else:
            logging.info('O vídeo é maior do que 14MB')

    except(NoSuchElementException, Exception) as bug:
            logging.warning(f"Falha no Envio do Video - {bug}")

    finally:
        logging.info('enviar_video() Terminou de Rodar')
            
            
            
def enviar_arquivo(nome_arquivo):

    try:
        filename = os.path.realpath(nome_arquivo)

        encontrar_attach_XPATH()

        marktime(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')
            )
        )
        
        document_button = drive.find_element(By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-document"]/../input')

        document_button.send_keys(filename)

        enviar_attach_XPATH()

    except(NoSuchElementException, Exception) as bug:
            logging.warning(f"Falha no Envio do Arquivo - {bug}")

    finally:
        logging.info('enviar_arquivo() Terminou de Rodar')
            


def aplicar_filtro():

    '''
    Função responsável por aplicar o filtro.
    '''

    aplicar_filtro_xpath = '//*[@id="side"]/div[1]/div/button/div/span'    
    
    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, aplicar_filtro_xpath)
        )
    )
    
    
    filter_button = drive.find_element(By.XPATH,
                                       aplicar_filtro_xpath)
    filter_button.click()
    logging.info('Filtro Aplicado')
    
    
    
def sair_da_conversa():

    '''
    Função responsável por sair da conversa atualmente aberta.\n
    '''

    inputbox_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    

    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, inputbox_xpath)
        )
    )


    drive.find_element(By.XPATH, 
                        inputbox_xpath
                        ).send_keys(Keys.ESCAPE)
    
        

def arquivo_txt_mutavel_insercao(nome_arquivo, texto):
    
    with open(f'{nome_arquivo}.txt','w') as arquivo:
        arquivo.write(' - '.join(texto))



def arquivo_txt_mutavel_leitura(nome_arquivo):
    
    with open(f'{nome_arquivo}.txt','r') as arquivo:
        texto_arquivo = arquivo.read()
        
    return texto_arquivo



def pegar_dados_contato():

    '''
    Esta função retornará uma lista contendo o nome e o número do contato que está aberto.
    Sendo o índice 0 o nome e o índice 1 o número
    '''

    try:
        titulo_ctt_xpath = '//*[@id="main"]/header/div[2]/div/div/span'
        drive.find_element(By.XPATH, titulo_ctt_xpath).click()

        t.sleep(1)

        nome_contato = drive.find_element(By.XPATH, 
                                            titulo_ctt_xpath).text
        t.sleep(1)

        numero_contato = drive.find_element(By.CLASS_NAME, 
                                            '_10kwi _1BX24 dd2Ow').text


        t.sleep(2)
        
        logging.info(f'{nome_contato} - {numero_contato}')
        logging.info('pegar_dados_contato() Terminou de Rodar')

        return [nome_contato, numero_contato]


    except Exception as bug:
           logging.info(f'O "Exception" apareceu enquanto era adquirido os dados do contato - {bug}')



def apagar_conversa():
    '''
    Através desta função, a conversa atualmente aberta será excluida.
    '''

    nome_contato = contato_nome()

    # Sequência de comandos pra realizar a funcionalidade de apagar a conversa
    ActionChains(drive
                ).key_down(Keys.CONTROL
                                ).key_down(Keys.ALT
                                            ).key_down(Keys.BACKSPACE
                                                                ).perform()

    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div')
        )
    )

    drive.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div').click()

    logging.info(f'A conversa com {nome_contato} foi apagada')
    logging.info('apagar_conversa() Terminou de Rodar')


   
def pegar_foto_contato(nome_imagem):

    '''
    Função responsável por pegar a foto do contato.
    '''
    

    def printscreen_foto(nome_imagem):
        
        drive.save_screenshot(f'{nome_imagem}.png')

        img_xpath = '//*[@id="app"]/div/span[3]/div/div/div[2]/div/div/div/div/img'
        elemento = drive.find_element(By.XPATH, img_xpath)
        posicao = elemento.location
        tamanho = elemento.size

        x = posicao['x']
        y = posicao['y']
        z = x + tamanho['width']
        w = y + tamanho['height']


        imagem = imagem.crop((x,y,z,w))
        imagem.save(f'{nome_imagem}_crop.png')


    info_ctt_xpath = '//*[@id="main"]/header/div[2]/div/div/span'
    
    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, info_ctt_xpath)
        )
    )
    
    info_ctt = drive.find_element(By.XPATH, info_ctt_xpath)
    info_ctt.click()
    
    t.sleep(1)
    
    mini_img_xpath = '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/section/div[1]/div[2]/div/div/img'
    mini_img = drive.find_element(By.XPATH, mini_img_xpath)
    mini_img.click()
    
    t.sleep(1)
    
    printscreen_foto(nome_imagem)
    
    link = drive.find_element(By.XPATH,'//*[@id="app"]/div/span[3]/div/div/div[2]/div/div/div/div/img'). get_attribute('src')
    print(link)
    

    # https://pt.stackoverflow.com/questions/446700/python-download-de-imagem-via-url
    # próximo de terminar



def possibilidade_desconectar_e_fechar_janela():

    logging.info('Desconectando Whatsapp...')


    dc_xpath1 = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/div/span'
    dc_xpath2 = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div'
    
    
    # xpath1
    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, dc_xpath1)
            )
        )


    dc_button = drive.find_element(By.XPATH,
                            dc_xpath1
                            )

    dc_button.click()
    drive.switch_to.active_element
    
    t.sleep(1)
    
    ActionChains(drive).key_down(Keys.ARROW_DOWN
                                    ).key_down(Keys.ARROW_DOWN
                                                ).key_down(Keys.ARROW_DOWN
                                                        ).key_down(Keys.ARROW_DOWN
                                                                   ).send_keys(Keys.ENTER
                                                                        ).perform()
    
    t.sleep(1)
    # xpath2
    marktime.until(EC.presence_of_element_located(
                                            (By.XPATH, dc_xpath2)
                                                                ))
    
    drive.find_element(By.XPATH, 
                            dc_xpath2
                            ).click()
    
    
    drive.close()
    logging.info('Whatsapp Encerrado')
    logging.info('Janela Encerrada')
    messagebox.showinfo('DESCONECTADO','O Whatsapp foi desconectado')   



def possibilidade_desconectar_e_manter_janela():

    logging.info('Desconectando Whatsapp...')
    
    dc_xpath1 = '//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]/div/span'
    dc_xpath2 = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div'
    
    
    # xpath1
    # Aguardando o parâmetro aparecer
    marktime.until(
        EC.presence_of_element_located(
            (By.XPATH, dc_xpath1)
            )
        )


    dc_button = drive.find_element(By.XPATH,
                            dc_xpath1
                            )
    dc_button.click()
    drive.switch_to.active_element
    
    
    
    ActionChains(drive).send_keys(Keys.ARROW_DOWN
                                    ).send_keys(Keys.ARROW_DOWN
                                                ).send_keys(Keys.ARROW_DOWN
                                                        ).send_keys(Keys.ARROW_DOWN, 
                                                                    Keys.ENTER
                                                                        ).perform()
    
    t.sleep(1)

    #xpath2
    marktime.until(EC.presence_of_element_located(
                                            (By.XPATH, dc_xpath2)
                                                                ))
    
    drive.find_element(By.XPATH, 
                            dc_xpath2
                            ).click()
    
    
    
    logging.info('Whatsapp Encerrado')
    logging.info('A Janela Seguirá Aberta')
    messagebox.showinfo('DESCONECTADO','O Whatsapp foi desconectado')



def converter_bytes_para(tamanho, para:str):

        '''Retorna Bytes para: "KB", "MB", "GB", "TB"'''
        
        conv_para = para.upper()
        if conv_para in ["BYTES", "KB", "MB", "GB", "TB"]:
            
            for x in ["BYTES", "KB", "MB", "GB", "TB"]:
                
                if x == conv_para:
                    return tamanho
                
                tamanho /= 1024.0



def adaptar_item(item):
      
    if item < 10:
        
        return '0' + str(item)
    else:
        return str(item)  



def arquivar_conversa():
    
    '''
    Função responsável pelo arquivamento da conversa\n
    Utilizando os comandos do Whatsapp para isso.
    '''

    ActionChains(drive).key_down(Keys.CONTROL
                                        ).key_down(Keys.ALT
                                                    ).key_down(Keys.SHIFT
                                                                ).send_keys('e'
                                                                            ).perform()
    
    dados_contato = pegar_dados_contato()
    nome_contato = dados_contato[0]
    
    
    logging.info(f'Conversa Arquivada - {nome_contato}')
    logging.info('arquivar_conversa() Terminou de Rodar!')



def marcar_como_nao_lida():

    '''
    Este função fará com que a conversa atualmente aberta seja marcada como "não lida"
    '''

    ActionChains(drive).key_down(Keys.CONTROL
                                        ).key_down(Keys.ALT
                                                    ).key_down(Keys.SHIFT
                                                                ).send_keys('u'
                                                                            ).perform()

    dados_contato = pegar_dados_contato()
    nome_contato = dados_contato[0]
    
    
    logging.info(f'Conversa Marcada Como Não Lida - {nome_contato}')
    logging.info('marcar_como_nao_lida() Terminou de Rodar!')



def buscar_contatos_não_lidos():
    'a'
    
#



def lista_ultimas_mensagens_recebidas_de_contatos(quantidade: int = 1):

    '''
    Função responsável para encontrar as últimas mensagens enviadas por cada contato
     de acordo com a quantidade oferecida na aplicação da função\n
    Por padrão, a quantidade é 1, mas basta alterar a mesma que retornará quantas conversas forem pré-determinadas\n
    Esta função retornará um dicionário contendo 2 dados, sendo eles: \n
    1- Key - Nome do contato
    2- Values: tupla - No índice 0 será a hora que a última mensagem foi enviada e no índice 1 será a última mensagem
    '''

    aplicar_filtro()
    
    nome_lista = []
    hora_lista = []
    mensagem_lista = []
    
    for i in range(quantidade):
        
        try:
            searchhbox_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
            
            marktime.until(
            EC.presence_of_element_located(
                (By.XPATH, searchhbox_xpath)
                )
            )

            t.sleep(1)
            searchhbox = drive.find_element(By.XPATH, 
                                            searchhbox_xpath)
            
            searchhbox.send_keys(Keys.ARROW_DOWN)
            
            info = drive.switch_to.active_element
            info2 = info.text.split('\n')
            
            nome, hora, mensagem = info2
            
            nome_lista.append(nome)
            hora_lista.append(hora)
            mensagem_lista.append(mensagem)
            
        except Exception as bug:
            logging.info(f'Não é possível realizar este método para Grupos. - {bug}')
            
            
    informacoes = dict(zip(
                        nome_lista, list(zip(
                                        hora_lista, mensagem_lista))))
    

    logging.info(f'Foi retornado o(s) seguinte(s) valor(s): {informacoes}')

    return informacoes

    

def ultimas_mensagens_conversa():

    '''
    Esta função irá, na conversa atualmente aberta, pegar as mensagens que foram enviadas.
     Em seu início, ela subirá para ser possível de captar mais inforamções e, logo após, irá retornar tudo em um dicionário.

    '''

    def subir_chat():
        '''
        Esta função só irá funcionar dentro da "ultimas_mensagens_conversa()".
         Ela é responsável por subir a conversa para que seja possível recolher mais mensagens.
        '''
        drive.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[3]').click()

        for i in range(20):
            ActionChains(drive).key_down(Keys.PAGE_UP).perform()


    def deploy_dict(padrao, i):
        '''
        Esta função só irá funcionar dentro da "ultimas_mensagens_conversa()".
        Nela, será trabalhado como o dicionário irá trabalhar com os dados para então haver a diferença de uma mensagem enviada, para uma mensagem antecedida por uma citação. 
        '''
    
        if padrao == 1:
            dict_info[i] = {
                            info_contato: (quote, mensagem)
                            }
       

        elif padrao == 2:
            dict_info[i] = {
                            info_contato: mensagem
                            }

        return dict_info



    subir_chat()

    chat_area = drive.find_element(By.ID, 'main')
    parametro = chat_area.find_elements(By.CLASS_NAME, 'copyable-text')

    dict_info = {}
    contato_conversa = []

    contador = 0
    try:
        for i, elemento in enumerate(parametro):

            #Informações que antecedem à mensagem
            pretexto = elemento.get_attribute('data-pre-plain-text')
            
            #Tratamento da Citação
            track_message = elemento.find_elements(By.TAG_NAME, 'div')
            track_message = track_message[-2:]
            track_message = [a.text 
                        for a in track_message]
            
            try:
                quote = track_message[0]
            except:
                pass
            
            #Mensagem Enviada 
            mensagem = elemento.find_element(By.TAG_NAME,'span').text        

            
            contato_conversa.append(pretexto)

            # Execução
            if pretexto == None:
                info_contato = contato_conversa [i - 1]

                if info_contato == None:
                    continue

                
                if quote != mensagem:
                    deploy_dict(1, contador)
                    contador += 1
                    
                else:
                    deploy_dict(2, contador)
                    contador += 1
                        
        else:
            logging.info('As Mensagens Foram Armazenadas.')

    except NoSuchElementException:
        pass
    
    finally:
        logging.info('ultimas_mensagens_conversa() Terminou de Rodar.')
        

    return dict_info



def encontrar_numeros_nao_salvos(intensidade: int = 40):
    '''
    Função responsável por encontrar números que não estão salvos. Irá retornar uma lista 
    '''
       
    
    #separacao das letras
    letras =  string.ascii_letters
    letras = [l for l in letras]


    # Execução
    search_box = drive.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    chat_area = drive.find_element(By.ID, 'pane-side')

    lista = []
    search_box.click()
    t.sleep(1)
    search_box.send_keys(Keys.ARROW_DOWN * 2)

    for i in range(intensidade):
        ActionChains(drive).send_keys(Keys.PAGE_DOWN
        ).perform()

        info_lista = chat_area.find_elements(By.TAG_NAME, 'div')        
        lista.append(l for l in info_lista)


        for i, item in enumerate(info_lista):
            item = item.get_attribute("aria-label")
            if item == 'Lista de conversas':
                item = info_lista[i]
                break

            else:
                pass

        dados = item.text.split('\n')

        lista_auxiliar = []
        for each in dados:
            contador = 0
            if '+' in each and '-' in each:
                for l in letras:
                    if l in each:
                        break
                    else:
                        contador += 1
                        if contador == len(letras):
                            lista_auxiliar.append(each)

    ActionChains(drive).send_keys(Keys.HOME)
                
    # lista_auxiliar = list(set(lista_auxiliar))
    return lista_auxiliar