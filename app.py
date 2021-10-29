from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import datetime

DEBUG = True
app = Flask(__name__,template_folder='static')
app.config.from_object(__name__)