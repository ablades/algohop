import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import networkx as nx

app = dash.Dash()


if __name__ == '__main__':
    app.run_server(debug=True)
