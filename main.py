# -*- coding: utf-8 -*-

from flask import Flask, render_template, make_response  # request, redirect, session, url_for
from flask_wtf import CSRFProtect
from werkzeug.http import http_date
# from functools import wraps, update_wrapper
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/p01')
def p01():
    return render_template('p01.html')


@app.route('/p02')
def p02():
    return render_template('p02.html')


@app.route('/p03')
def p03():
    return render_template('p03.html')


@app.route('/p04')
def p04():
    # session.clear()
    # session['session1'] = 'value of session1'
    resp = make_response(render_template('p04.html'))
    resp.set_cookie('cookie1', 'value of cookie1')
    resp.set_cookie('sessionID', '', expires=0)
    return resp


# from flask_cache import Cache
# app.config['CACHE_TYPE'] = 'null'
# cache = Cache(app,config={'CACHE_TYPE': 'null'})


@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'public, no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    r.headers['Last-Modified'] = http_date(datetime.now())
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    return r


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# $ python main.py
