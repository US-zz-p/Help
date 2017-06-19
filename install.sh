export FLASK_APP=usp
export FLASK_DEBUG=1

# creating docs
cd sphinx
sphinx-apidoc --output-dir=. --maxdepth=10 --force --separate --private --module-first ..
# make clean html latexpdf
sphinx-build -b html -a -E -j 1 --color . /tmp/usp
# sphinx-build -a -E -b pdf . /tmp/usp
# ln -sf /tmp/usp ../usp/static/doc

cd ..
pip install --no-cache-dir --upgrade -e .
# pip install --no-cache-dir --upgrade --force-reinstall -e .
# pip install --upgrade -e . # --no-binary -v

# pip install -r requirements.txt

flask run --host=0.0.0.0 --port=5005
# python -m flask run
# flask shell
