from app import app
from flask import request, render_template

@app.route("/")
def index():
    return render_template("index.html")

# creating user
#@app.route("/add_reference", methods=["POST"])
#def add_reference():
    #if request.method == "POST":
        #author = request.form["author"]
        #title = request.form["title"]
        #year = request.form ["year"]
        #publisher = request.form ["publisher"]


if __name__ == "__main__":
    app.run(debug=True)