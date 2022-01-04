import pandas as pd
from pandas.io.sql import table_exists
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "" # apagado para privacidade
# Your Auth Token from twilio.com/console
auth_token  = "" #apagado para privacidade
client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'No mês {mes} a meta foi batida pelo vendedor: {vendedor} com o valor de: {vendas}')
        message = client.messages.create(
            to="exemplo", #Número que vai receber o sms
            from_="exemplo",#Número que a twilio gerou para você
            body=f'No mês {mes} a meta foi batida pelo vendedor: {vendedor} com o valor de: {vendas}')
        print(message.sid)