from AllWhatsPy import *
import pandas as pd



# Importação de Dados
alunos_ativos1_df = pd.read_excel('planilha1.xlsx')
alunos_ativos2_df = pd.read_excel('planilha2.xlsx')
alunos_ativos3_df = pd.read_excel('planilha3.xlsx')



# Junção de Dados
planilha_df = alunos_ativos1_df.merge(alunos_ativos2_df, how='outer')
planilha_df = planilha_df.merge(alunos_ativos3_df, how='outer')



# Tratamento de Dados
planilha_df['Nome'] = [str(each).title() for each in planilha_df['Nome']]
planilha_df['Celular'] = [str(each).replace('(','').replace(')','').replace('-','') for each in planilha_df['Celular']]
planilha_df = planilha_df.sort_values(by='Nome')
planilha_df = planilha_df[['Nome','Email Nome','Celular']]



texto = ''' Olá, {}!
Estou passando para lembrar que hoje vence o pagamento do seu plano.
Para mais informações, estou aqui para ajudá-lo.
'''
# Execução
conexao()


for i, nome in enumerate(planilha_df['Nome']):
       celular = planilha_df.iloc[i, 2]
       

       
       print(f'{i+1} - {nome} - {celular}')
       encontrar_usuario(celular)
       enviar_mensagem_paragrafada(texto.format(nome))

       
desconectar()
