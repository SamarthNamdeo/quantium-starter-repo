# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Morsel": ["pink morsel", "gold morsel", "magenta morsel", "periwinkle morsel", "Oranges"],
    "Amount": [2195,2180, 2395, 4045, 4135],
    "Direction": ["North", "East", "West", "South" , "North"]
})

fig = px.bar(df, x="Morsel", y="Sales($)", color="Direction", barmode = "group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
