# Beautiful Soup: Uma biblioteca Python usada para extrair dados de arquivos HTML e XML. Ela cria uma árvore
# de análise a partir das páginas web que podem ser usadas para extrair dados de maneira eficiente.

# Faker: Uma biblioteca Python que permite a geração de dados fictícios, como nomes, endereços,
# números de telefone, entre outros. É útil para criar datasets de teste e realizar simulações.

# lxml: Uma biblioteca Python que fornece uma maneira eficiente e fácil de trabalhar com XML e HTML.
# É frequentemente usada em conjunto com Beautiful Soup para fazer parsing de documentos HTML.

# Pandas: Uma biblioteca Python poderosa e flexível para manipulação e análise de dados.
# Ela oferece estruturas # de dados como DataFrames, que facilitam a manipulação de dados tabulares.

# PyMySQL: Um módulo Python que permite a conexão e interação com bancos de dados MySQL.
# Ele é usado para executar consultas SQL e manipular dados diretamente a partir de scripts Python

# Requests: Uma biblioteca Python que facilita o envio de requisições HTTP.
# É usada para interagir com APIs e baixar conteúdo da web, simplificando o processo de fazer requisições GET e POST.

# Web Scraping: A técnica de extração de dados de websites. Envolve o uso de scripts para coletar informações
# de páginas web, que podem ser usadas para análise de dados ou outras finalidades.

# Modúlo é o conjunto dos códigos, funções, variavéis e classe é uma estrutura de dados como dados int, booleano, etc


# Entendimento da linha 3
# Foi necessário utilizar um cabeçalho "User-Agent" para simular um navegador headers={'User-Agent': 'Mozilla/5.0'})
# Não foi necessário, mas caso estivesse em loop, eu poderia adicionar "time.sleep()"

# Entendimento da linha print(response.text[:600])
texto = 'Extrair msg de texto'

subtexto = texto[:11]
print(subtexto)

subtexto = texto[8:11]
print(subtexto)

subtexto = texto[-5:]
print(subtexto)

# O + serve para concatenar texto


# coleta_dados_outros

# Existem várias formas de criar conexão com python, mas de forma tabulada fica visualmente melhor
# função df.to salva os dados em vários tipos de formato
# index=False é para não criar uma coluna de index nos dados
# Código antigo criado em aula, porém atualmente está gerando erro
    # def df_conexao_mysql(host, user, password, database, table):
#     # Criar conexão
#     conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + database)
#     conn = pymysql.connect(host=host, user=user, password=password, database=database)
#
#     # Executar consulta e salvar em um dataframe
#     query = ' SELECT * FROM ' + table
#     df = pd.read_sql(query, conn)
#
#     # Exibir os resultados
#     print('Tabela MySQL com DataFrame: \n', df.head())

    # Fechar a conexão
    #conn.dispose()
    # conn.close()
    # return df