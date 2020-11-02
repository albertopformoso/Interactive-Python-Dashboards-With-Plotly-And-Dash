import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd, numpy as np

app = dash.Dash()
colors = {'background': '#111111', 'text': '#7FDBFF'}


app.layout = html.Div(children=[
             html.H1('Hello Dash!', style={'textAlign': 'center',
                                           'color': colors['text']}),
             dcc.Graph(id='example',
                       figure=dict(data=[{'x': [1, 2, 3], 'y':[4, 1, 2], 'type':'bar', 'name':'SF'},
                                         {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}],
                                   layout={'plot_bgcolor': colors['background'],
                                           'paper_bgcolor': colors['background'],
                                           'font': {'color': colors['text']},
                                           'title': 'BAR PLOTS!'}))
], style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server()