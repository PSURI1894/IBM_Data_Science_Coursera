# dash_app.py - simple Dash app for the assignment
import dash
from dash import html, dcc, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('automobile_sales_20000.csv', parse_dates=['date'])
app = dash.Dash(__name__)
app.title = 'Automobile Sales Recession Dashboard'

app.layout = html.Div([
    html.H1('Automobile Sales Recession Dashboard', id='title'),
    html.Div([
        dcc.Dropdown(id='vehicle-dropdown', options=[{'label':t,'value':t} for t in df['vehicle_type'].unique()], value='Sedan'),
        dcc.Dropdown(id='stat-dropdown', options=[{'label':'Sales Volume','value':'sales_volume'},{'label':'Avg Price','value':'avg_price'}], value='sales_volume')
    ], style={'width':'40%'}),
    html.Div(id='output-div', className='output-container'),
    dcc.Graph(id='main-graph')
])

@app.callback([Output('output-div','children'), Output('main-graph','figure')],
              [Input('vehicle-dropdown','value'), Input('stat-dropdown','value')])
def update(vehicle, stat):
    dff = df[df['vehicle_type']==vehicle]
    fig = px.line(dff, x='date', y=stat, title=f'{vehicle} - {stat} over time')
    summary = f"Selected: {vehicle} | Stat: {stat} | Rows: {len(dff)}"
    return summary, fig

if __name__ == '__main__':
    app.run(debug=True)
