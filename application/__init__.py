from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


from application import routes

