import pandas as pd
import os

# Verifica e carrega arquivos de despesas e receitas
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", parse_dates=["Data"])
    df_receitas = pd.read_csv("df_receitas.csv", parse_dates=["Data"])




else:
    data_structure = {'valor': [], 'Efetuado': [], 'Fixo': [], 'Data': [], 'Categoria': [], 'Descrição': []}
    df_despesas = pd.DataFrame(data_structure)
    df_receitas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv", index=False)
    df_receitas.to_csv("df_receitas.csv", index=False)



    

# Verifica e carrega categorias
if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv")
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv")
    cat_receita = df_cat_receita['Categoria'].tolist()
    cat_despesa = df_cat_despesa['Categoria'].tolist()
else:
    cat_receita = ["Salário", "Investimento", "Comissão"]
    cat_despesa = ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]
    df_cat_receita = pd.DataFrame({"Categoria": cat_receita})
    df_cat_despesa = pd.DataFrame({"Categoria": cat_despesa})
    df_cat_receita.to_csv("df_cat_receita.csv", index=False)
    df_cat_despesa.to_csv("df_cat_despesa.csv", index=False)
