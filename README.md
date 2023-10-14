<h1 align="center">
<br>AllWhatsPy - AWP
</h1>

 
<h1 align="center">
<img src="/utilidades/awpimgg.png" alt="AllWhatsPy" width="350px"/>



<div align="center">
   <img src="https://visitor-badge.laobi.icu/badge?page_id=https://github.com/DevLucasLourenco/AllWhatsPy"> 
   <img src="https://static.pepy.tech/personalized-badge/allwhatspy-awp?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads/Ano">
 <img src="https://static.pepy.tech/personalized-badge/allwhatspy-awp?period=month&units=none&left_color=grey&right_color=blue&left_text=Downloads/Mes">
  <img src="https://static.pepy.tech/personalized-badge/allwhatspy-awp?period=week&units=none&left_color=grey&right_color=blue&left_text=Downloads/Semana">
   <img src="https://img.shields.io/github/stars/devlucaslourenco/allwhatspy">
   <img src="https://img.shields.io/github/commit-activity/y/devlucaslourenco/allwhatspy">
   <img src="https://img.shields.io/github/languages/code-size/devlucaslourenco/allwhatspy">
</div>
</h1>

> PT-BR

>Criado por [Lucas Lourenço](https://github.com/DevLucasLourenco/AllWhatsPy#autor)

>Manutenido por [Lucas Lourenço](https://github.com/DevLucasLourenco/AllWhatsPy#autor)


## Sumário <><><><><><><><><><><><><><><><><>

- [Tutorial](https://github.com/DevLucasLourenco/AllWhatsPy#tutorial-em-v%C3%ADdeo2)
- [AllWhatsPy](https://github.com/DevLucasLourenco/AllWhatsPy#por-que-allwhatspy)
- [Instalação](https://github.com/DevLucasLourenco/AllWhatsPy#come%C3%A7ando-no-allwhatspy)
- [Lista de Tarefa](https://github.com/DevLucasLourenco/AllWhatsPy#objetivos-a-serem-terminados)
- [Exemplos](https://github.com/DevLucasLourenco/AllWhatsPy#exemplos)
- [Códigos](https://github.com/DevLucasLourenco/AllWhatsPy#o-que-voc%C3%AA-pode-fazer-com-allwhatspy)
- [Notas do Criador](https://github.com/DevLucasLourenco/AllWhatsPy#notas-do-criador)
- [Autor](https://github.com/DevLucasLourenco/AllWhatsPy#autor)
- [Contribuição](https://github.com/DevLucasLourenco/AllWhatsPy#contribui%C3%A7%C3%A3o)
- [Erros](https://github.com/DevLucasLourenco/AllWhatsPy#problemas-com-o-allwhatspy)


## Tutorial em Vídeo

<h1 align="center">
 
<a href="https://youtu.be/2Z74Y_V80SA">
<img src="/utilidades/videoicon.gif" alt="Tutorial" width="350px" href=/>
</a>

</h1>


## ⭐ Avalie o Código! ⭐



É de muitíssima importância a `Estrela` que você pode estar dando para colaborar com a `Manutenção` e `Atualização` do código!
Se você utiliza o AllWhatsPy com frequência, gosta da forma que foi desenvolvido, se inspira nele, serei muito grato por sua avaliação!

<h1 align="center">
<a href="https://github.com/DevLucasLourenco/AllWhatsPy/stargazers">
<img src="https://cdn-icons-png.flaticon.com/512/2534/2534324.png" weight= 100 height=100 >
</a>
</h1>



## Autor

<h2>
<p>

[Linkedin](http://linkedin.com/in/lucas-lourenco0312)

</p>


<p>

[Instagram](https://www.instagram.com/lucaslourencoo__/)


</p>
 
<p>
  
Email: dev.lucaslourenco@gmail.com
  
</p>
</h2>




## Por que AllWhatsPy?

À medida que nossa dependência do WhatsApp, seja para fins profissionais ou pessoais, se torna incontestável, surge a inquietação de como otimizar essa aplicação essencial em nossas vidas. A resposta a essa inquietação se materializa na forma do AllWhatsPy, uma biblioteca inovadora e poderosa criada para revolucionar sua experiência de automação de processos no WhatsApp.

Inspirado por notáveis projetos como o [PyWhatsapp](https://github.com/shauryauppal/PyWhatsapp) e o [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit), iniciei uma jornada de exploração, imersão e pesquisa aprofundada nas possibilidades oferecidas por Bots e APIs do WhatsApp. Com um compromisso <b>`inabalável com a qualidade e o aprimoramento`</b> de software, decidi investir meu tempo e energia na criação do AllWhatsPy, um projeto que tem sido desenvolvido de forma exclusiva e independente.

Ao longo desse processo, foram dedicadas milhares de linhas de logs em testes, registrando cada passo do caminho para garantir o funcionamento perfeito da biblioteca. O resultado é uma ferramenta versátil e flexível que permite que você faça literalmente "o que quiser" no WhatsApp, proporcionando um nível inédito de eficiência e automação. O AllWhatsPy é a solução que você estava esperando para elevar a produtividade e a conveniência no uso do WhatsApp, tornando-o uma ferramenta ainda mais indispensável em sua vida.


</br>
</br>
  
## Começando no AllWhatsPy

<div align="center">
   <h2>
      INSTALAÇÃO
   </h2>
</div>

Para a instalação da lib, no terminal faça:

```
pip install -U allwhatspy (<><><><><><><><><><>)
```

Após, chame o pacote. Segue exemplo:

```python
<><><><><><><><><><><><><><><><><>
```


Você também pode estar baixando os arquivos e colar na sua pasta, caso sua máquina esteja tendo problemas em instalar esta lib.

</br>

### Lógica básica:

```mermaid
flowchart LR
  AWPContato  --> AllWhatsPy
  AWPMensagem --> AllWhatsPy
  AWPAudio --> AllWhatsPy
  AWPCriptografia --> AllWhatsPy

  AllWhatsPy ----> awp.msg.enviar_mensagem_por_link 
  AllWhatsPy ----> awp.msg.enviar_mensagem_direta

  awp.msg.enviar_mensagem_por_link ----> awp.desconectar
  awp.msg.enviar_mensagem_direta ----> awp.desconectar

  AllWhatsPy ---> .ctt
  AllWhatsPy --> .criptografia 
  
  .ctt --> awp.ctt.encontrar_contato
  .ctt --> awp.ctt.encontrar_usuario
  
  awp.ctt.encontrar_contato --> .msg
  awp.ctt.encontrar_usuario --> .msg


  .msg ---> awp.msg.enviar_mensagem
  .msg ---> awp.msg.enviar_mensagem_paragrafada

  .msg --> .audio 

  awp.msg.enviar_mensagem_paragrafada --> awp.desconectar
  awp.msg.enviar_mensagem --> awp.desconectar


       
```



## Objetivos a Serem Terminados 

- [x] Criar alternativas para envio de mensagem (Realizado - 19/12/2022)
- [x] Tratar as `except Exception` (Realizado - 21/12/2022)
- [x] Resolver bug na urllib (Realizado - 21/12/2022)
- [x] Alimentar o código com opções alternativas para `awp.conexao()` e  `awp.desconectar()` (Realizado - 21/12/2022)
- [x] Corrigir excepts de `NoSuchElementException`  (Realizado - 22/12/2022)
- [x] Implementar WebDriverWait para melhor responsividade do software (Realizado - 27/12/2022)
- [x] Configurar a entrada de `logs` (Realizado - 28/12/2022)
- [x] Atualizar ActionChains (Realizado - 15/01/2023)
- [x] Terminar `ultimas_mensagens_conversa()` (Realizado - 18/01/2023)
- [x] Explicar todas as fórmulas (Realizado - 21/01/2023)
- [x] Aperfeiçoar a função de `agendamento` (Realizado - 21/01/2023)
- [x] Terminar o `sumário` (Realizado - 21/01/2023)
- [x] Implementar a área de `Exemplos Práticos` (Realizado - 21/01/2023)
- [x] Fazer vídeo e postar no Youtube de explicação para utilizar o código (Realizado - 22/01/2023)
- [x] Implementar exemplos convencionais (Realizado - 23/01/2023) 
- [x] Alterar Imagem da lógica do AWP com Mermaid (Realizado - 23/01/2023)
- [x] Finalizar função `encontrar_numeros_não_salvos()` (Realizado - 25/01/2023)
- [x] Implementação de Classes (Realizado - 12/02/2023)
- [x] Desenvolver um `pip install` para AWP (Realizado - 12/02/2023)
- [x] Atualizar `nome_usuario()` (Realizado - 15/02/2023)
- [x] Atualizar bug da função `desconectar()` (Realizado - 20/02/2023)
- [x] Corrigir bug na função `pegar_foto_contato()` (Realizado - 21/02/2023)
- [x] Atualizar icon do AWP (Realizado - 25/02/2023)
- [x] Atualizar `contato_nome()`
- [x] Realizar a explicação de como começar no AWP
- [ ] Performar criação de pastas com a lib `pathlib` para melhor qualidade de software
- [x] Implementação de Classes, Métodos e Módulos auxiliaers
- [x] Lançamento da Versão Final do AllWhatsPy (Realizado - 10/10/2023)
- [ ] Propagar o erro AWPContatoNaoEncontrado



## 🚨Exemplos🚨   <><><><><><><><><><><><><><><><><><><><>

<details>
<summary>
 🚨Exemplos Práticos🚨
</summary>

<p>

 - [Exemplo Prático - Tratamento de Dados com Execução AWP](/exemplos/TratamentoDeDados-Execução.py)
 
 - [Exemplo Prático - Agendamento em Lista com Execução AWP](/exemplos/ListaDeAgendamentos-ExecucaoAWP.py)
 
 - [Exemplo Prático - Descendo Chats e Retornando as Mensagens](/exemplos/DescendoChatsBuscandoMensagens-ExecuçãoAWP.py)
</p>

</details>


<details>
<summary>
 🚨Exemplos🚨
</summary>

<p>

 - [Exemplo](/exemplos/exemplo.py)
 
 - [Exemplo]()
 
</p>

</details>


<p>

# Utilizando AllWhatsPy 


<details>
<summary style="font-size: 25px">
   Inicialização
</summary>
 
## Instanciando
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
```

> Instancia do objeto AllWhatsPy.

> `inicializarTitulo` (Padrão: True): Este parâmetro booleano determina se o título do aplicativo será inicializado ou não. Quando definido como True, o título será inicializado. Caso seja False, não será exibido. Este parâmetro somente é responsável por apresentar o AWP e o link do github.

>`realizar_log` (Padrão: True): Este parâmetro booleano controla se o AllWhatsPy deve realizar o registro de ações e eventos. Quando definido como True, o AllWhatsPy registrará informações detalhadas sobre as ações realizadas durante a sessão, o que pode ser útil para rastrear e solucionar problemas.

>`JSON_file` (Padrão: True): Este parâmetro booleano determina se as informações da sessão, como contatos, mensagens e configurações, devem ser salvas em um arquivo JSON. Isso pode ser útil para preservar o estado da sessão entre as execuções do programa.

### Ex.: 
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo:bool=True, realizar_log:bool=True, JSON_file:bool=True)
```


## Conexão

```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()
```
>`show_off` (Padrão: True): Este parâmetro booleano controla se a GUI do Google será exibida em tela cheia ou minimizada. Quando True, exibirá em tela cheia. Quando False, minimizado.

>`server_host` (Padrão: False): Este parâmetro booleano determina se a função de conexão armazenará em cache o login feito pelo usuário. Ou seja, basta realizar uma única vez a leitura do QR Code e ela estará armazenada para as próximas instancias do AWP.<p>Diretório onde se encontra o armazenamento: C://users/[Usuário]/AllWhatsPyHost

>`popup` (Padrão: False): Este parâmetro booleano controla se devem ser exibidas janelas pop-up ou notificações durante a conexão. Quando definido como True, o AllWhatsPy pode mostrar janelas pop-up a validação manual do usuário para permissão de continuidade.

>`calibragem` (Padrão: (True, 10)): Este parâmetro é uma tupla que controla a calibração da função de conexão. A primeira parte da tupla (um booleano) indica se a calibração será ativada ou desativada. A segunda parte da tupla (objeto do tipo int) define o tempo da calibração. A calibração é um processo que ajusta e sincroniza os contatos durante a conexão para otimizar o desempenho durante a propagação das funcionalidades do AWP.


### Ex.: 
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))
```

## Desconexão
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.desconectar()
```


## InferênciaAWP

```python 
class InferenciaAWP:
        lista_contatos: list
        contato: str
        mensagem: str
        contatosInexistentes: list
        contato_acessivel: bool
```

>`lista_contatos`: Este atributo é uma lista que armazena os contatos. Automaticamente, ele é preenchido no decorrer da utilização do AWP. 

>`contato`: Este atributo é uma string que armazena o nome do contato atual. Ele é inicializado como uma string vazia e pode ser usado para acompanhar o contato atual durante a inferência.

>`mensagem`: Este atributo é uma string que armazena a mensagem a ser enviada. Ele é inicializado como uma string vazia e pode ser usado para armazenar a mensagem que será enviada durante a inferência.

>`contatosInexistentes`: Este atributo é uma lista que armazena os contatos inexistentes. Ele é inicializado como uma lista vazia e pode ser usado para rastrear os contatos que não existem no sistema.

>`contato_acessivel`: Este atributo é um booleano que indica se o contato é acessível ou não. Ele é inicializado como um booleano e pode ser usado para verificar se o contato é acessível antes de realizar a inferência.


### Ex.: 
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

contato = awp.InferenciaAWP.contato
lista_contatos = awp.InferenciaAWP.lista_contatos
ctt_inexistentes = awp.InferenciaAWP.contatosInexistentes
mensagem = awp.InferenciaAWP.mensagem

print(contato, lista_contatos, ctt_inexistentes, mensagem, sep='\n')
```

>Todas estas variáveis armazenarão suas respectivas colocações. O preenchimento é feito através dos Decorators do AWP automaticamente, de acordo com o passar das action phases do AWP. 

OBS.: Referente a todos estes atributos, ao final, caso o parâmetro do AllWhatsPy referente ao [JSON](https://github.com/DevLucasLourenco/AllWhatsPy#Instanciando) receber um valor booleano True, como é o caso do exemplo, estas informações serão indexadas ao JSON que será criado.

## Explodir Server
```python
from AllWhatsPy import AllWhatsPy


```
</details>



<details>
<summary style="font-size: 25px">
   Contatos
</summary>

# AWPContatos

## Encontrar Usuário
___
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
```
> `contato_destino`: Referente ao usuário que será acessado. Por meio desta, será utilizado através da procura direta com o link do Whatsapp. Visto isso, ao contrário do `awp.encontrar_contato()`, não será possível procurar pelo nome do contato salvo, somente seu respectivo número. **Todavia, este é o método mais preciso**

> Valores que serão aceitos ao parâmetro: str ou int 

### Ex.: 
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(contato_destino=21999999999)
```

## Encontrar Contato
___
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_contato()
```
>`contato_destino`: Referente ao contato que será acessado. Por meio desta, será utilizado a barra de pesquisa para procurar pelo contato. **Somente encontrará contatos salvos**.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_contato(contato_destino='Lucas Lourenço')
# Ou
awp.ctt.encontrar_contato(contato_destino=21999999999)
```

## Deslocamento entre Conversas
___


```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.chat_acima()
awp.ctt.chat_abaixo()
```
>Respectivamente, responsáveis por se deslocar para o contato acima e para o contato abaixo do atual.
 

### Ex.:

```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.chat_acima()
awp.ctt.chat_abaixo()
```
</details>


<details>
<summary style="font-size: 25px">
   Mensagens
</summary>

# AWPMensagem

## Mensagem Separada
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
awp.msg.enviar_mensagem()
```
>`mensagem`: Mensagem que será enviada ao **contato** acessado. Com este método, todo parágrafo possível será executado como uma mensagem separada. Uma lista ou tupla também será executada como uma mensagem separada.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo:bool=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)

# Caso 1
awp.msg.enviar_mensagem('Mensagem por linha')

# Caso 2
awp.msg.enviar_mensagem(['mensagem','por linha'])

# Caso 3
msg = '''
mensagem
por
linha
'''
awp.msg.enviar_mensagem(msg)


# Caso 1
>>> Mensagem por linha

# Caso 2
>>> Mensagem 
>>> por linha

# Caso 3
>>> Mensagem 
>>> por 
>>> linha
```


## Mensagem Paragrafada
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
awp.msg.enviar_mensagem_paragrafada()
```

> `mensagem`: Mensagem que será enviada ao **contato** acessado. Responsável pela paragrafação e concatenação das strings. Com este método, toda string passada mensagem será mesclada à uma única, formando assim o envio de uma única mensagem contendo todo o conteúdo.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)

# Caso 1
awp.msg.enviar_mensagem_paragrafada('Mensagem paragrafada para envio')

# Caso 2
awp.msg.enviar_mensagem_paragrafada(['Mensagem paragrafada','para envio'])

# Caso 3
msg = '''
mensagem
paragrafada
para
envio
'''
awp.msg.enviar_mensagem_paragrafada(msg)


#Caso 1
>>> Mensagem paragrafada para envio

#Caso 2
>>> Mensagem paragrafada 
para envio

#Caso 3
>>> mensagem
paragrafada
para
envio
```

## Mensagem por Link
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.msg.enviar_mensagem_por_link()
```
>`numero`: Número o qual será enviado esta mensagem

>`texto`: Texto que será abrangido pelo `parse.quote`, em prol de tratar e transformar de forma adaptativa ao link, uma API do Whatsapp, a mensagem que será enviada. 

OBS.: Não é aconselhável utilizar este método para muitos números consecutivos. Sujeito a bloqueio de conta.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.msg.enviar_mensagem_por_link(21999999999, 'Mensagem a ser enviada')
```

## Mensagem Direta
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.msg.enviar_mensagem_direta()
```
>`contato`: O nome do contato para o qual você deseja enviar a mensagem.
> 
>`mensagem`: A mensagem que você deseja enviar.

>`selecionar_funcao` (Padrão: 1): Uma opção que permite escolher o formato da mensagem. Use 1 para mensagens por linha ou 2 para mensagens paragrafadas.

>`salvo` (Padrão: True): Um valor booleano que determina se o contato deve ser encontrado na lista de contatos salvos (True) ou usando a função de busca (False).

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.msg.enviar_mensagem_direta(21999999999, 'Hello World', 1, False)
```


# Analise de Mensagens

## Ultima mensagem de um chat
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
ultima_msg = awp.msg.analise.ultima_mensagem_chat()
print(ultima_msg)
```
>Este método é capaz de retornar unicamente a última mensagem de um chat atualmente aberto.


# Envio de Anexos

## Enviar Imagem
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
awp.msg.anexo.enviar_imagem()
```
>`nome_arquivo`: O caminho do arquivo da imagem que você deseja enviar.

>`mensagem`: A mensagem de texto que você deseja incluir com a imagem.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo:bool=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
awp.msg.anexo.enviar_imagem(r'caminho/do/arquivo.jpg-png', 'Hello World')
```

## Enviar Arquivo
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
awp.msg.anexo.enviar_arquivo()
```
>`nome_arquivo`: O caminho do arquivo que você deseja enviar.

>`mensagem`: A mensagem de texto que você deseja incluir com o arquivo.

### Ex.:
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo:bool=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
awp.msg.anexo.enviar_arquivo(r'caminho/do/arquivo.ext', 'Hello World')
```

# Envio de Endereço via CEP
```python
from AllWhatsPy import AllWhatsPy
awp = AllWhatsPy(inicializarTitulo=True, realizar_log=True, JSON_file=True)

endereco = awp.msg.endereco(24754000).retornar()

awp.ctt.encontrar_usuario(21999999999)
awp.msg.enviar_mensagem(endereco)
```
</details>


<details>
<summary style="font-size: 25px">
   Utilidades
</summary>

# Métodos Utilitários

## Arquivar Contato
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
awp.utilidade.arquivar_chat()
```

## Marcar como não Lida
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
awp.utilidade.marcar_como_nao_lida()
```

## Detecção Conta Comercial ou Pessoal
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
resultado = awp.utilidade._comercial_ou_pessoal()
```
>Após a execução do método, será retornado uma das seguintes strings: "C" ou "P", respectiamente condizente à conta Comercial ou Pessoal.

## Agendamento
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy()
awp.conexao()

awp.ctt.encontrar_usuario()
awp.utilidade.agendamento()
```

>`dia_programado`: O dia do mês programado para a execução da tarefa

>`hora_programado`: A hora programada para a execução da tarefa.

>`minuto_programado`: O minuto programado para a execução da tarefa.

OBS.:passar ao parâmetro um objeto do tipo str.

### Ex.: 
```python
from AllWhatsPy import AllWhatsPy

awp = AllWhatsPy(inicializarTitulo=True, realizar_log:bool=True, JSON_file:bool=True)
awp.conexao(show_off=True, server_host=True, popup=False, calibragem=(True, 10))

awp.ctt.encontrar_usuario(21999999999)
awp.utilidade.agendamento(dia_programado="10", hora_programado="15", minuto_programado="30")
```


#



</details>

<details>
<summary style="font-size: 25px">
   Criptografia
</summary>


## Cifra de Caesar




