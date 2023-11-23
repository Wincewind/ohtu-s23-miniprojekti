from app import app
from flask import jsonify, request, send_from_directory
from services.reference_services import reference_service
import dataprocessing # REFACTOR: routes.py should only use the services class


@app.route("/")
def index():
    return app.send_static_file("index.html")

# adding reference


@app.route("/add_reference", methods=["POST"])
def add_reference():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        publisher_address = request.form["publisher_address"]

        print(author, title, year, publisher, publisher_address)

        if dataprocessing.add_book(author, title, year,
                                   publisher, publisher_address):
            return jsonify({"message": "Reference added"})
        else:
            return jsonify({"message": "Error occurred when adding reference"})

@app.route("/get_all_references")
def get_all_references():
    return reference_service.get_all_references()

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('build', path)


if __name__ == "__main__":
    app.run(debug=True)
