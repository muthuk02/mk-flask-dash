from application import app
from flask import render_template, redirect, url_for, request
import pandas as pd
import plotly.express as px
import plotly.io as pio


@app.route('/')
def index():
    # Load the data
    df = pd.read_csv('world_population.csv')

    # Create a Plotly figure
    fig = px.bar(df, x='Country', y='Population', title='World Population by Country')

    # Convert the figure to HTML
    graph_html = pio.to_html(fig, full_html=False)

    return render_template("index.html", graph_html=graph_html)
