import sys, os
from setuptools import setup, find_packages

setup(
    name='usp',
    version='0.1.dev1',
    license='AGPLv3',
    author='John Robson',
    author_email='john.robson@usp.br',
    url='https://usp.herokuapp.com/',
    description=('Flask Tests'),
    long_description='README',
    packages=find_packages(),
    install_requires=[
        'flask',
        'uwsgi',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
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

# classifiers=[

# https://github.com/mitodl/lmod_proxy/blob/master/setup.py
# test_suite="lmod_proxy.tests",
# tests_require=tests_require,
# cmdclass={"test": PyTest},
# zip_safe=False,


if __name__ == '__main__':
    try:
        setup()
        sys.exit(0)
    except SystemExit as e:
        os._exit(0)
