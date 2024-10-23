import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

from globals import *






# ========= Layout ========= #
layout = dbc.Col([
                html.H1("FINANÇAS PESSOAIS", className="text-primary"),
                html.P("By GRISOTTO", className="text-info"),
                html.Hr(),

#seção de perfil--------------------
dbc.Button(id='botão_avatar',
        children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='avatar', className='perfil_avatar',)
                ], style={'background-color':'transparent', 'border-color':'transparent'}),
    
#seção NOVO--------------------
dbc.Row([
    dbc.Col([
        dbc.Button(color='success', id='open-novo-receita',
            children=['+ Receita'])

    ], width=5),
    dbc.Col([
        dbc.Button(color='danger', id='open-novo-despesa',
            children=['- Despesa'])
            
            
    ],width=6)
      
]),

# Modal Receitas------------------
dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label('Descrição: '),
                dbc.Input(placeholder="Ex.: Dividendos da bolsa, herança...", id="txt_receitas"),
            ], width=6),
            dbc.Col([
                dbc.Label("Valor: "),
                dbc.Input(placeholder="$100,00", id="valor_receita", value="")
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Data: "),
                dcc.DatePickerSingle(id='date-receita',
                                     min_date_allowed=date(2020, 1, 1),
                                     max_date_allowed=date(2030, 12, 31),
                                     date=datetime.today(),
                                     style={"width": "100%"}
                                     ),

            ], width=4),

            dbc.Col([
                dbc.Label("Extras"),
                dbc.Checklist(
                    options=[{"label": "Foi Recebida", "value": 1},
                             {"label": "Receita Recorrente", "value": 2}],
                    value=[1],
                    id='switches-input-receita',
                    switch=True
                )
            ], width=4),

            dbc.Col([
                html.Label('Categoria da receita'),
                dbc.Select(id='select_receita',
                    options=[{'label': i, 'value': i} for i in cat_receita],
                    value=cat_receita[0])
            ], width=4)

        ], style={'margin-top': '25px'}),


        dbc.Row([
            dbc.Accordion([
                dbc.AccordionItem(children=[
                    dbc.Row([
                        dbc.Col([
                            html.Legend("Adicionar categoria", style={'color': 'green'}),
                            dbc.Input(type="text", placeholder="Nova Catergoria...", id="input-add-receita", value=""),
                            html.Br(),
                            dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                            html.Br(),
                            html.Div(id="category-div-add-receita", style={}),
                        ],width=6),

                        dbc.Col([
                            html.Legend('Excluir Categoria', style={'color': 'red'}),
                            dbc.Checklist(
                                id='checkList-select-style-receita',
                                options=[{"label": i, "value": i} for i in cat_receita],
                                value=[],
                                label_checked_style={'color': 'red'},
                                input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange' },  
                            ),

                            dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),

                        ],width=6)

                    ])
                ], title="Adicionar/Remover Catergorias")
            ], flush=True, start_collapsed=True, id='accordion-receita'),

            html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
            dbc.ModalFooter([
                dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),

            ])
        
        ], style={'margin-top': '25px'})
    ])
], style={"background-color": "rgba(17, 140, 79, 0.05)"},
id="modal-novo-receita",
size="lg",
is_open=False,
centered=True,
backdrop=True),

# Modal Despesas------------------
dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
    dbc.ModalBody([ 
dbc.Row([
            dbc.Col([
                dbc.Label('Descrição: '),
                dbc.Input(placeholder="Ex.: Gasolina, Petshop...", id="txt_despesa"),
            ], width=6),
            dbc.Col([
                dbc.Label("Valor: "),
                dbc.Input(placeholder="$100,00", id="valor_despesa", value="")
            ], width=6)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Data: "),
                dcc.DatePickerSingle(id='date-despesa',
                                     min_date_allowed=date(2020, 1, 1),
                                     max_date_allowed=date(2030, 12, 31),
                                     date=datetime.today(),
                                     style={"width": "100%"}
                                     ),

            ], width=4),

            dbc.Col([
                dbc.Label("Extras"),
                dbc.Checklist(
                    options=[{"label": "Foi Recebida", "value": 1},
                             {"label": "Despesa Recorrente", "value": 2}],
                    value=[1],
                    id='switches-input-despesa',
                    switch=True
                )
            ], width=4),

            dbc.Col([
                html.Label('Categoria da despesa'),
                dbc.Select(id='select_despesa',
                           options=[{'label': i, 'value': i} for i in cat_despesa],
                           value=cat_despesa[0])
            ], width=4)

        ], style={'margin-top': '25px'}),


        dbc.Row([
            dbc.Accordion([
                dbc.AccordionItem(children=[
                    dbc.Row([
                        dbc.Col([
                            html.Legend("Adicionar categoria", style={'color': 'green'}),
                            dbc.Input(type="text", placeholder="Nova Categoria...", id="input-add-despesa", value=""),
                            html.Br(),
                            dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                            html.Br(),
                            html.Div(id="category-div-add-despesa", style={}),
                        ],width=6),

                        dbc.Col([
                            html.Legend('Excluir Categoria', style={'color': 'red'}),
                            dbc.Checklist(
                                id='checkList-select-style-despesa',
                                options=[{"label": i, "value": i} for i in cat_despesa],
                                value=[],
                                label_checked_style={'color': 'red'},
                                input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange' },  
                            ),

                            dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),

                        ],width=6)

                    ])
                ], title="Adicionar/Remover Categorias")
            ], flush=True, start_collapsed=True, id='accordion-despesa'),

            html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
            dbc.ModalFooter([
                dbc.Button("Adicionar Despesa", id="salvar_despesa", color="success"),
                dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click"),

            ])
        
        ], style={'margin-top': '25px'})
    ])
], style={"background-color": "rgba(17, 140, 79, 0.05)"},
id="modal-novo-despesa",
size="lg",
is_open=False,
centered=True,
backdrop=True),


#seção NAV--------------------
html.Hr(),
dbc.Nav([
    dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
    dbc.NavLink("Extratos", href="/extratos", active="exact"),
], vertical=True, pills=True, id='nav.buttons', style={"margin-buttom": "50px"}),

], id='sidebar_completa')



# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')

)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
    # Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')

)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    


# Enviar Form receita
@app.callback(
    Output('store-receitas', 'data'),

    Input("salvar_receita", "n_clicks"),

    [
        State("txt_receitas", "value"),
        State("valor_receita", "value"),
        State("date-receita", "date"),
        State("switches-input-receita", "value"),
        State("select_receita", "value"),
        State('store-receitas', 'data')
    ]
)
def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    df_receitas = pd.DataFrame(dict_receitas)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_receitas.loc[df_receitas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_receitas.to_csv("df_receitas.csv")

    data_return = df_receitas.to_dict()
    return data_return




# Enviar Form despesa
@app.callback(
    Output('store-despesas', 'data'),
    Input('salvar_despesa', 'n_clicks'), 
    [
        State('txt_despesa', 'value'),
        State('valor_despesa', 'value'),  # Corrigido para 'valor_despesa'
        State('date-despesa', 'date'),
        State('switches-input-despesa', 'value'),
        State('select_despesa', 'value'),
        State('store-despesas', 'data')
    ]
)
def salve_form_despesa(n, descricao, valor, date, switches, categoria, dict_despesas):
    df_despesas = pd.DataFrame(dict_despesas)

    if n and not(valor == "" or valor is None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if isinstance(categoria, list) and len(categoria) > 0 else None
        recebido = 1 if 1 in switches else 0
        fixo = 1 if 2 in switches else 0

        df_despesas.loc[df_despesas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_despesas.to_csv("df_despesas.csv", index=False)

    data_return = df_despesas.to_dict()
    return data_return



@app.callback(
        [Output("select_despesa", "options"),
        Output('checkList-select-style-despesa', 'options'),
        Output('checkList-select-style-despesa', 'value'),
        Output('store-cat-despesas', 'data')],

        [Input("add-category-despesa", "n_clicks"),
         Input("remove-category-despesa", "n_clicks")],

         [State("input-add-despesa", "value"),
          State('checkList-select-style-despesa', 'value'),
          State('store-cat-despesas', 'data')]

)
def add_category(n, n2, txt, check_delete, data):

    cat_despesa = list(data["Categoria"].values())

    if n and not (txt == " or txt == None"):
        cat_despesa = cat_despesa + [txt] if txt not in cat_despesa else cat_despesa

    
    if n2:
        if len(check_delete) > 0:
            cat_despesa = [i for i in cat_despesa if i not in check_delete]

    opt_despesa = [{"label": i, "value": i} for i in cat_despesa]
    df_cat_despesa = pd.DataFrame(cat_despesa, columns = ["Categoria"])
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    data_return = df_cat_despesa.to_dict()

    return [opt_despesa, opt_despesa, [], data_return]