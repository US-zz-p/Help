# -*- coding: utf-8 -*-

from flask import Flask, session, g # render_template, make_response, session, g  # request, redirect, url_for
from flask_wtf import CSRFProtect
# from functools import wraps, update_wrapper


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

csrf = CSRFProtect()
csrf.init_app(app)

import usp.main.requests
import usp.main.views
# from tests.view_decorator import *

################################################################################

# from flask_cache import Cache
# app.config['CACHE_TYPE'] = 'null'
# cache = Cache(app,config={'CACHE_TYPE': 'null'})
# @app.route('/')
# @cache.cached(timeout=60)
# def index():

################################################################################

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# $ python main.py
