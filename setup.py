from setuptools import setup, find_packages

setup(
    name='usp',
    version='0.1.dev0',
    url='https://usp.herokuapp.com/',
    author='John Robson',
    author_email='john.robson@usp.br',
    description='Flask Tests',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['flask', ],
)

# https://docs.google.com/presentation/d/1-g0UYgV72jwtyeFLHYqz0Sh56VSiCiGHn5Bu3TW2hUM/

# develop='no-deps',
# packages=['usp'],

# entry_points={ 'invenio.config': ['myoverlay = myoverlay.config'] }

# pip install git+git://github.com/inveniosoftware/invenio@pu#egg=Invenio-dev -e .

# package_data =
#        { 'rocky_server' :        # NOTE: package/folder name, not pip name
#          [ 'templates/*.html'
#          , 'static/favicon.ico'
#          , 'static/*.png'
#          ]
#        }
