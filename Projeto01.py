# Passo 0 - Entender o desafio que você quer resolver
# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta vendas)
import os
import pandas as pd

lista_arquivo = os.listdir(
    "C:/Users/leona/Downloads/Mini curso Projeto1/Vendas-20250430T004854Z-001/Vendas")
print(lista_arquivo)
# Passo 2 - Importar as bases de dadis de vendas
tabelas = []
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:

        tabela = pd.read_csv(
            f"C:/Users/leona/Downloads/Mini curso Projeto1/Vendas-20250430T004854Z-001/Vendas/{arquivo}")
        tabelas.append(tabela)
tabela_total = pd.concat(tabelas, ignore_index=True)
print(tabela_total)
# Passo 3 - Tratar/Compilar as bases de dados
# Passo 4 - Calcular o produto mais vendido (em quantidade)
# Passo 5 - Calcular o produto que mais faturou (em faturamento)
# Passo 6 - Calcular a loja/cidade qye mais vendeu (em faturamento) - criar um gráfico/dashboard
