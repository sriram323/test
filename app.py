from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker(First container in pipeline)!!"
kkkkkkkjjjjjjj


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
