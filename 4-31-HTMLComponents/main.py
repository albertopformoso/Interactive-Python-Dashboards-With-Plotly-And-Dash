import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd, numpy as np

app = dash.Dash()

np.random.seed(42)

df = pd.read_csv('../data/OldFaithful.csv')

app.layout = html.Div(['This is the outermost div!',
                       html.Div(['This is an inner div!'],
                                style={'color': 'red', 'border': '3px red solid'}),
                       html.Div(['Another inner div!'],
                                style={'color': 'blue', 'border': '3px blue solid'})],
                      style={'color': 'green', 'border': '2px green solid'})

if __name__ == '__main__':
    app.run_server()