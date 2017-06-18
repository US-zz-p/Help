export FLASK_APP=usp
export FLASK_DEBUG=1

# creating docs
cd sphinx
sphinx-apidoc -o . -f ..
sphinx-build -b html . /tmp/sphinx # make html
ln -sf /tmp/sphinx ../usp/static/doc

cd ..
pip install --no-cache-dir --upgrade -e .
# pip install --no-cache-dir --upgrade --force-reinstall -e .
# pip install --upgrade -e . # --no-binary -v

# pip install -r requirements.txt

flask run --host=0.0.0.0 --port=5005
# python -m flask run
# flask shell
