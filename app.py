gggg
fffffffffffrom flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker(First container in pipeline)!!"
DB_PAssword = "s488323@swe@3$%#"

DB = "s488323@swe@3$%#"  
DB = "s488323@swe@3$%#"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
