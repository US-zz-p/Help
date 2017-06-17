# -*- coding: utf-8 -*-

from flask import Flask # render_template, make_response, session, g  # request, redirect, url_for
# from functools import wraps, update_wrapper
# from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

import usp.views

# csrf = CSRFProtect()
# csrf.init_app(app)

################################################################################

# from flask_cache import Cache
# app.config['CACHE_TYPE'] = 'null'
# cache = Cache(app,config={'CACHE_TYPE': 'null'})
# @app.route('/')
# @cache.cached(timeout=60)
# def index():

################################################################################

# import tests.requests
# from tests.view_decorator import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# $ python main.py
