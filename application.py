import io

import plotly.graph_objects as go

import dash

from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from flask import Flask, send_file, request

import layout
import config
import index_string



# Variable name below should be `application` for AWS Elastic Beanstalk
application = Flask(__name__)

@application.route('/feature1/')
def app_feature1():
    return {'Hello': 'feature1'}



dashapp = dash.Dash(
    __name__,
    server=application,
    url_base_pathname='/',
    meta_tags=config.META_TAGS,
    external_stylesheets=config.external_stylesheets,
    suppress_callback_exceptions=True
)

dashapp.index_string = index_string.index_string

dashapp.title = 'Dash on Flask: Minimal Example'
dashapp.layout = layout.layout


@dashapp.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_color(color):
    plotly_figure = go.Figure(
        data=go.Bar(y=[2, 3, 1], marker_color=color))
    return plotly_figure



if __name__ == '__main__':
    application.run(debug=False)
