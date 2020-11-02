import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd, numpy as np
import plotly.io as pio


# Themes
# ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
# 'ygridoff', 'gridon', 'none']
pio.templates.default = "plotly_white"

app = dash.Dash()

app.layout = html.Div(children=[
             html.H1('Hello Dash!'),
             html.Div('Dash: Web Dashboards With Python'),
             dcc.Graph(id='example',
                       figure=dict(data=[{'x': [1, 2, 3], 'y':[4, 1, 2], 'type':'bar', 'name':'SF'},
                                         {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}],
                                   layout={'title': 'BAR PLOTS!'}))
])

if __name__ == '__main__':
    app.run_server()