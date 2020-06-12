from flask import Flask, render_template, url_for


app = Flask(__name__)

lis = ['shivam', 'harleen', 'arpita', 'sushant', 'anjali']

@app.route("/")
def index():
    return render_template('home.html', lis=lis)



if __name__ == "__main__":
    app.run(debug=True, port=5858)



