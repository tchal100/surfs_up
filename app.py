from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello, World!"
export FLASK_APP=app.py

if_name _=="_name_":
    app.run(hosts="0.0.0.0" debug=true, port=5000)
