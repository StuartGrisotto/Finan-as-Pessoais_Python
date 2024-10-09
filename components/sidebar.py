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






# ========= Layout ========= #
layout = dbc.Col([
                html.H1("FPP", className="text-primary"),
                html.P("By GRISOTTO", className="text-info"),
                html.Hr(),

#seção de perfil--------------------
dbc.Button(id='botão_avatar',
        children=[html.Img(src='/assent/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                ], style={'background-color': 'tranparent', 'border-color': 'transparent'}),
    
#seção NOVO--------------------
dbc.Row([
    dbc.Col([
        dbc.Button(color='sucess', id='open-novo-receita',
            children=['+ Receita'])

    ], width=6),
    dbc.Col([
        dbc.Button(color='danger', id='open-novo-despesa',
            children=['+ Despesa'])
            
            
    ],width=6)
      
]),
#seção NAV--------------------
html.Hr(),
dbc.Nav([
    dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
    dbc.NavLink("Extratos", href="/extratos", active="exact"),
], vertical=True, pills=True, id='nav.buttons', style={"margin-buttom": "50px"}),

])



# =========  Callbacks  =========== #
# Pop-up receita