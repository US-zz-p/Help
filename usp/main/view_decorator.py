# http://flask.pocoo.org/docs/latest/views/
# http://flask.pocoo.org/docs/latest/patterns/viewdecorators/
# http://flask.pocoo.org/snippets/category/decorators/
# http://flask.pocoo.org/docs/latest/api/
# http://flask.pocoo.org/docs/latest/patterns/lazyloading/
# http://flask.pocoo.org/snippets/18/
# http://flask.pocoo.org/snippets/56/
# https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
# https://stackoverflow.com/questions/23065247/flask-app-add-url-rule-in-decorator-error
# https://damyanon.net/flask-series-views/
# https://stackoverflow.com/questions/24851241/flask-view-function-mapping-is-overwriting-an-existing-endpoint-function-type
# https://stackoverflow.com/questions/19964079/flask-function-mapping-is-overwriting-an-existing-endpoint-function
# https://stackoverflow.com/questions/28819876/assertionerror-view-function-mapping-is-overwriting-an-existing-endpoint-functi
# https://stackoverflow.com/questions/38458026/assertionerror-view-function-mapping-is-overwriting-an-existing-endpoint-functi
# https://stackoverflow.com/questions/34865873/assertionerror-view-function-mapping-is-overwriting-an-existing-endpoint-functi


from flask import render_template, make_response, g
from flask.views import MethodView
from functools import wraps
from usp import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(401)
def abort(error):
    return make_response('<h1>401 Error</h1>', 401, {'WWWAuthenticate': 'Basic realm="Login Required"'})


def login_check(f):
    print('Function Decorator - Check Login')

    @wraps(f)
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator


def cls_decorator(Cls):
    print('Class Decorator - Check Login')

    @wraps(Cls)
    class decorator(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            pass
    return decorator


# @cls_decorator
class UserAPI(MethodView):
    # decorators = [login_check]

    def get(self, user_id):
        formSub = '<form action="." method="post"><input type="submit" value="Submit"></form>'
        if user_id is None: # return a list of users
            return make_response('<h1>Get A</h1>' + formSub)
        else: # expose a single user
            return make_response('<h1>Get B</h1>' + formSub)

    @login_check
    def post(self): # create a new user
        return make_response('<h1>Post</h1>')

    def delete(self, user_id): # delete a single user
        return make_response('<h1>Delete</h1>')

    def put(self, user_id): # update a single user
        return make_response('<h1>Put</h1>')


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', ])
    app.add_url_rule(url, view_func=view_func, methods=['POST', ])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE'])


register_api(UserAPI, 'user_api', '/users/', pk='user_id')
