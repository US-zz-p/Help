from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

from flask_wtf import CsrfProtect
csrf = CsrfProtect()
csrf.init_app(app)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True, threaded=True)
