from flask import render_template

from app import app
from models.order_list import *

@app.route('/')
def index():
    return render_template('index.html', order_list=orders)

@app.route('/order-1')
def order_1():
    return render_template('order-1.html', order1=order1)