from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import dashboards, extratos, sidebar



# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row({
        dbc.Col([
            dbc.Location(id='url'),
            sidebar.layout
        ], nd=2, style={'background=color': 'red', 'heigth': '1080px'}),
        dbc.Col({
            content
        }, nd=10, style={'background=color': 'blue', 'heigth': '1080px'})
    })



], fluid=True,)

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboard':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)