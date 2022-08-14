import dash
from dash import dcc
from dash import html
import plotly.express as px
import quandl

df = quandl.get("WIKI/AAPL.4", start_date="2010-1-1", end_date="2018-12-31")
# print(df)
figura = px.line(df, title="Cotización de Apple: ENERO 2010 - DICIEMBRE 2018")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="APLICACIÓN CON DASH PARA MERCADOS FINANCIEROS"),
    dcc.Graph(figure=figura)])

if __name__ == '__main__':
    app.run_server(debug=True)