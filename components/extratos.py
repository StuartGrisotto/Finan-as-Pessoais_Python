import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

# =========  Layout  =========== #
layout = dbc.Col([

       dbc.Row([
           html.Legend('Tabela de Dispesas'),
           html.Div(id='tabela-despesas', className='dbc')
       ]),

       dbc.Row([
           dbc.Col([
               dcc.Graph(id='bar-graph', style={'margin-right': '20px'})
           ],width=9),

           dbc.Col([
               dbc.Card(
                   dbc.CardBody([
                       html.H4("Despesas"),
                       html.Legend("R$ 4400", id="valor_despesa_card", style={'front-size': '60px'}),
                       html.H6("Total de despesas"),
                   ], style={'text-align': 'center', 'padding-top': '30px'})
               )
           ], width=3)
           ])
       ], style={'paddin': '10px'})

# =========  Callbacks  =========== #
# Tabela
# Tabela
@app.callback(
    Output('tabela-despesas', 'children'),
    Input('store-despesas', 'data')
)
def imprimir_tabela (data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    tabela = dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
        filter_action="native",    
        sort_action="native",       
        sort_mode="single",  
        selected_columns=[],        
        selected_rows=[],          
        page_action="native",      
        page_current=0,             
        page_size=10,                        
    ),

    return tabela




@app.callback(
    Output('bar-graph', 'figure'),

    [Input('store-despesas', 'data'),]
)
def bar_chart(data):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum() [["valor"]].reset_index()
    
    graph = px.bar(df_grouped, x='Categoria', y='valor', title = "Despesas Gerais")
    graph.update_layout(paper_bgcolor = 'rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    return graph

@app.callback(
    Output('valor_despesa_card', 'children'),

    [Input('store-despesas', 'data'),]
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = df['valor'].sum()

    return f"R$ {valor}"