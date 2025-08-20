import pymysql
from sqlalchemy import create_engine
import pandas as pd



def conexao_mysql(host, user, password, database, table):
    # Criar conexão
    conn = pymysql.connect(host=host, user=user, password=password, database=database)

    cursor = conn.cursor()

    # Executar consulta
    query = f" SELECT * FROM {table}  LIMIT 10 "
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exibir os resultados
    print('Tabela MySQL')
    for linha in resultados:
        print(linha)

    # Fechar a conexão
    cursor.close()
    conn.close()


# Criando conexão com dataframe
def df_conexao_mysql(host, user, password, database, table):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, engine)
    print('Tabela MySQL com DataFrame: \n', df.head(10))
    return df


def conexao_excel(path):
    # Ler arquivo Excel
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    # Escrever arquivos CSV
    df.to_csv('dados.csv', index=False)

def conexao_csv(path):
    # Ler arquivo CSV
    df = pd.read_csv(path)
    print('Dados CSV: \n', df.head())

    # Escrever arquivo JSON
    df.to_json('dados.json', orient='records', index=False)


conexao_mysql(
    'localhost',
    'root',
    '',
    'loja_informatica',
    'cliente'
    )

df_cliente = df_conexao_mysql(
    'localhost',
    'root',
    '',
    'loja_informatica',
    'cliente'
    )

df_cliente.to_excel('dados.xlsx', index=False)

conexao_excel('dados.xlsx')

conexao_csv('dados.csv')