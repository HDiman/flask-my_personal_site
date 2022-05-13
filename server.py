from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center" >Flask Web Page</h1>'



if __name__ == "__main__":
    app.run(debug=True)

