export FLASK_APP=usp
export FLASK_DEBUG=true

pip install -e .
# pip install --upgrade -e . # --no-binary -v

# pip install -r requirements.txt

flask run --port 5005
