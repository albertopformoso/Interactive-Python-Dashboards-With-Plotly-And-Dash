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

app.layout = html.Div([
             html.Label('Dropdown'),
             dcc.Dropdown(options=[{'label': 'New York City',
                                    'value': 'NYC'},
                                   {'label': 'San Francisco',
                                    'value': 'SF'},
                                   {'label': 'Arkansas City',
                                    'value': 'AK'}
                                   ],
                          value='NYC'),
             html.Label('Slider'),
             dcc.Slider(min=-10, max=10, step=0.5, value=0,
                        marks={i: i for i in range(-10, 10)}),
             html.P(),
             html.Label('Radio Items'),
             dcc.RadioItems(options=[{'label': 'New York City',
                                      'value': 'NYC'},
                                     {'label': 'San Francisco',
                                      'value': 'SF'},
                                     {'label': 'Arkansas City',
                                      'value': 'AK'}
                                     ],
                            value='NYC')
])

if __name__ == '__main__':
    app.run_server()
