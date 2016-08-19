from flask import Flask, render_template, session, make_response, request, redirect, url_for

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

from flask_wtf import CsrfProtect
csrf = CsrfProtect()
csrf.init_app(app)


@app.route('/')
def index():
  #session.clear()
  #session['session1'] = 'value of session1'
  resp = make_response(render_template('maintenance.html'))
  #resp.set_cookie('cookie1', 'value of cookie1')
  #resp.set_cookie('sessionID', '', expires=0)
  return resp


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)
