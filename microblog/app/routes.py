#!/usr/bin/env python3

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Michael'}
    posts = [
        {
            'author': {'username':'Julie'},
            'body': 'It has rained all the week!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'We will go hiking this weekend.'
        },
        {
            'author': {'username':'James'},
            'body': 'watch out the hurricane!'
        }
    ]
    return render_template('index.html', user = user, posts = posts)



