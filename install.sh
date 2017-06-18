export FLASK_APP=usp
export FLASK_DEBUG=1

pip install --no-cache-dir --upgrade -e .
# pip install --no-cache-dir --upgrade --force-reinstall -e .
# pip install --upgrade -e . # --no-binary -v

# pip install -r requirements.txt

flask run --host=0.0.0.0 --port=5005
# python -m flask run
# flask shell
