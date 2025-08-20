# Coleta de Dados

Este repositório reúne os notebooks desenvolvidos durante o módulo de 
**Coleta de Dados** do curso de Análise de Dados – EBAC.  
O foco foi aprender a acessar, extrair e organizar dados de diferentes 
fontes, estruturadas e não estruturadas, utilizando bibliotecas Python e 
serviços externos.

---

## Objetivo

Demonstrar como coletar dados de forma automatizada e eficiente, respeitando 
a estrutura de cada fonte.  
As atividades envolveram desde web scraping até integração com bancos de 
dados e APIs.

---

## Conteúdo dos Notebooks

### 1. **Web Scraping com Requests, BeautifulSoup e Pandas**

- Requisições HTTP simulando navegadores reais
- Interpretação de HTML com BeautifulSoup
- Extração de títulos, parágrafos, links e tabelas
- Conversão de conteúdo web em DataFrames


### 2. **Geração de Dados Fictícios com Faker**

- Simulação de dados realistas como nome, CPF, endereço, e-mail e telefone
- Uso de `Faker` com localização brasileira (`pt_BR`)
- Exportação para CSV para uso em análises e testes


### 3. **Conexão com Banco de Dados MySQL**

- Acesso a dados reais via `PyMySQL` e `SQLAlchemy`
- Execução de queries SQL e transformação em DataFrames
- Exportação para Excel, CSV e JSON


### 4. **Upload e Download de Arquivos via API**

- Envio de arquivos para GoFile.io usando `requests`
- Recuperação de arquivos via URL pública
- Automação de processos de armazenamento e compartilhamento

---

## Componentes do Projeto

- `requests` – acesso a páginas web e APIs  
- `BeautifulSoup` – interpretação de HTML  
- `Faker` – geração de dados sintéticos  
- `pymysql` e `sqlalchemy` – conexão com banco de dados  
- `pandas` – manipulação e exportação de dados  
- `pathlib` – gerenciamento de caminhos de arquivos


---

## Aprendizados

- A coleta de dados é uma etapa estratégica que exige atenção à estrutura, 
formato e origem das informações.  
- Cada fonte seja ela web, banco, API ou simulação exige uma abordagem 
específica e cuidados técnicos.  
- Automatizar a coleta permite escalar projetos e garantir consistência na 
entrada de dados.  
- Documentar o processo é essencial para reprodutibilidade e colaboração.

---


### Como usar este repositório

Cada notebook pode ser executado individualmente em ambiente Jupyter.  
Os arquivos `.csv`, `.xlsx` e `.json` gerados estão incluídos ou podem 
ser reproduzidos com os scripts disponíveis.


---

### Sobre mim

Sou estudante de Análise de Dados e este módulo faz parte da minha 
jornada prática e técnica na coleta de dados.  
Cada projeto foi construído com dedicação e foco em transformar dados brutos
em informação útil e confiável.
