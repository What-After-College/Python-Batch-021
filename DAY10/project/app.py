from flask import Flask, render_template, url_for
from imdb import get_movie_details

app=Flask(__name__)

@app.route("/")
def index():
    lis = get_movie_details()
    return render_template("home.html", data = lis)

if __name__ == "__main__":
    app.run(debug=True)