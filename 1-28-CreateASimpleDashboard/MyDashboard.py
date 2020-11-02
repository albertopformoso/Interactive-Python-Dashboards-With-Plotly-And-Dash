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

app.layout = html.Div([dcc.Graph(id='OldFaithful_Scatterplot',
                                 figure=dict(data=[go.Scatter(x=df['X'],
                                                              y=df['Y'],
                                                              mode='markers',
                                                              marker={'size': 6, 'color': 'rgb(51,204,153)'})],
                                             layout=go.Layout(title='Old Faithful Eruptions',
                                                              xaxis={'title': 'Interval to next eruption (min)'},
                                                              yaxis={'title': 'Duration of eruption (min)'},
                                                              hovermode='closest')))
                       ])

if __name__ == '__main__':
    app.run_server()

