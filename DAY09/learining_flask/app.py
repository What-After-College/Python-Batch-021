from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return '''<h1 style="color: red;">hello guys</h1>'''


@app.route("/<name>")
def dyn(name):
    return "hello"+ str(name)


if __name__ == "__main__":
    app.run(debug=True, port=5858)



