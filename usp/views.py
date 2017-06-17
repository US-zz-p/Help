from flask import render_template, make_response #, session, g  # request, redirect, url_for
from usp import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/p01/')
def p01():
    return render_template('p01.html')


@app.route('/p02/')
def p02():
    return render_template('p02.html')


@app.route('/p03/')
def p03():
    return render_template('p03.html')


@app.route('/p04/')
def p04():
    # session.clear()
    # session['session1'] = 'value of session1'
    resp = make_response(render_template('p04.html'))
    resp.set_cookie('cookie1', 'value of cookie1')
    resp.set_cookie('sessionID', '', expires=0)
    return resp
