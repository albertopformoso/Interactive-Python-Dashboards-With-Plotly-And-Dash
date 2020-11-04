import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../data/mpg.csv')

df['year'] = random.randint(-4, 5, len(df)) * 0.10 + df['model_year']

app.layout = html.Div([
    dcc.Graph(id='mpg_scatter',
              figure={
                  'data': [go.Scatter(
                      x=df['year'] + 1900,
                      y=df['mpg'],
                      text=df['name'],
                      hoverinfo='text+x+y',
                      mode='markers')],
                  'layout': go.Layout(
                      title='mpg.csv dataset',
                      xaxis={'title': 'model year'},
                      yaxis={'title': 'miles per gallon'},
                      hovermode='closest')})
])

if __name__ == '__main__':
    app.run_server()
