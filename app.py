
#grab some of my favourite packages for data and what we will use
import requests
import dash
import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

url = 'http://data.fixer.io/api/latest'
key = '23a6adad66c705a6af5c284c8e1d347e'
brokenkey = '23a6adad66c705a6af5c284c8e1d347e23232323' #was using this for error testing
base = 'EUR' #only base allowed on this api at free tier
sym = 'GBP,USD' #cant be a list documentation was outdated, pass in as one string

#the api call function
def api_call(url, key, syms, base):
    vars = {'access_key': key, 'base':base, 'symbols':syms} #dictionary ordered according to documentation on https://fixer.io/documentation
    resp = requests.get(url, params=vars) #use requests to ping the api
    resp.raise_for_status()
    return resp.json() #retun as json

#make some functions to convert to EUR and back to GBP and USD, seems dumb but we cant use either USD or GBP as a base because we aren't rich.
def convert_curr(num):
    resp = [] #default var, I always do this out of habit
    rates = api_call(url, key, sym, base)
    df = pd.DataFrame(rates) #make it pandas so we can check it easier
    check = df.success[0] #we check to see if it was a success
    check = str(check) #slighty unconventional but one of the quirks of dash is it likes strings
    if check == 'True':
        df = df.rates
        GBP = df['GBP']
        USD = df['USD']
        EUR = num/GBP #convert to EURO
        resp = EUR*USD #convert to USD
        resp = '${:,}'.format(round(resp)) #format it nicely
    elif check == 'False':
        error = df.error
        msg = ' Please Try again'
        Ecode = error['code']
        Etype = error['type']
        Einfo = error['info']
        resp = 'Error code: ' + str(Ecode) + '  Error Type: ' + str(Etype) + ' Info: ' + str(Einfo) + msg
    else:
        resp = 'Something has gone horribly wrong!'
    return resp

#lets make this pretty because why not, make a bootstrap webpage using flask/dash!
#most layouts copied from the basic examples from https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/ for the sake of speed

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col(
                                html.H2('Currency Converter - GBP to USD')
                        )], justify='center'),
                        dbc.Row([
                            dbc.Col(
                                html.P('by James Buck', className = 'text-muted')
                        )], justify='center'),
                    ]),
                    dbc.CardBody(
                     dbc.Row([
                        dbc.Col(
                                dbc.InputGroup([
                                    dbc.InputGroupText('GBP'),
                                    dbc.Input(id="input1", placeholder="enter amount", value=100),
                                    dbc.Button('Calculate',id='btn1')
                                ])
                        )], justify='center'),
                    ),
                    dbc.CardFooter(
                        dbc.Row([
                            dbc.Col(
                                html.H6('answer', id='result', style={'text-align':'center'})
                        )], justify='center'),
                    )
                    ])
    ], className="justify-content-center center-block text-center",
)

#make a callback
@app.callback(
    Output('result', 'children'),
    Input('btn1', 'n_clicks'),
    State('input1','value')
)
def calculate(n, val):
    if n:
        num = int(val)
        resp = convert_curr(num)
        msg = str(resp)
    else:
        msg = 'Try me'
    return msg

if __name__ == "__main__":
    app.run_server(debug=True)
