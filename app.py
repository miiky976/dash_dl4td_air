from dash import dcc, html, Dash, callback
from methods import predict, process
from dash.dependencies import Input, Output, State
import pandas as pd

app = Dash()

app.layout = [
    html.H1(children='Just predict', style={'textAlign': 'center'}),
    dcc.Dropdown(predict.models, predict.models[0], id='dropdown-selection'),
    html.Div([
        html.Label(id="lp1"),
        dcc.Input(id="ip1", type="number", min=0),
        html.Label(id="lp2"),
        dcc.Input(id="ip2", type="number", min=0),
        html.Label(id="lp3"),
        dcc.Input(id="ip3", type="number", min=0),
        html.Label(id="lp4"),
        dcc.Input(id="ip4", type="number", min=0),
    ]),
    html.Div([
        html.Label("T"),
        dcc.Input(id="t", type="number"),
        html.Label("AH"),
        dcc.Input(id="ah", type="number", min=0),
        html.Label("RH"),
        dcc.Input(id="rh", type="number", min=0),
        html.Label("Date Time"),
        dcc.DatePickerSingle(id="date"),
        html.Label("Hour"),
        dcc.Input(id="hour", type="number", min=0, max=23)
    ]),
    html.Button("Make prediction", id="predict"),
    html.H1(id="target")
]


@callback(
    [Output('lp1', 'children'),
     Output('lp2', 'children'),
     Output('lp3', 'children'),
     Output('lp4', 'children')
     ],
    Input('dropdown-selection', 'value')
)
def change_labels(value):
    ps = predict.models.copy()
    ps.remove(value)
    return ps


@callback(
    Output('target', 'children'),
    Input('predict', 'n_clicks'),
    [State('dropdown-selection', 'value'),
     State('ip1', 'value'),
     State('ip2', 'value'),
     State('ip3', 'value'),
     State('ip4', 'value'),
     State('t', 'value'),
     State('ah', 'value'),
     State('rh', 'value'),
     State('hour', 'value'),
     State('date', 'date')
     ]
)
def make_prediction(click, drop, p1, p2, p3, p4, t, ah, rh, hour, date):
    if None in [p1, p2, p3, p4, t, ah, rh, date]:
        return "Error"
    # df = pd.DataFrame({
    #    'p1': [p1], 'p2': [p2], 'p3': [p3], 'p4': [p4], 't': [t], 'rh': [rh], 'ah': [ah], 'datetime': [str(date) + " " + str(hour)]
    # })
    df = process.process_input(
        [p1, p2, p3, p4, t, rh, ah, str(date) + " " + str(hour)])
    prediction = predict.predict(df, predict.models.index(drop))
    return str(prediction)


if __name__ == '__main__':
    app.run(debug=True)
