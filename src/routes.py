from app import app
from flask import jsonify, request, send_from_directory
from services.reference_services import reference_service


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/add_reference", methods=["POST"])
def add_reference():

    if request.method == "POST":
        authors = request.form["authors"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        publisher_address = request.form["publisher_address"]

        print(authors, title, year, publisher, publisher_address)

        if reference_service.add_book(authors, title, year,
                                      publisher, publisher_address):
            # Frontend response still wrong ('Reference added!') even after statuscodes
            return jsonify({"message": "Reference added"}), 201
        else:
            # Frontend response still wrong ('Reference added!') even after statuscodes
            return jsonify({"message": "Error occurred when adding reference"}), 501


@app.route("/get_all_references")
def get_all_references():
    return reference_service.get_all_references()


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('build', path)


if __name__ == "__main__":
    app.run(debug=True)
