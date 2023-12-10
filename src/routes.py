from app import app
from flask import jsonify, request, send_from_directory
from services.reference_services import reference_service


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/add_reference", methods=["POST"])
def add_reference():
    if request.method == "POST":
        # changed request.form["field"] to this to add a default empty string
        authors = request.form.get("authors", "")
        title = request.form.get("title", "")
        year = request.form.get("year", "")
        publisher = request.form.get("publisher", "")
        publisher_address = request.form.get("publisher_address", "")
        journal = request.form.get("journal", "")
        volume = request.form.get("volume", "")
        number = request.form.get("number", "")
        pages = request.form.get("page", "")
        type = request.form.get("type", "")

        if reference_service.add_book(title, type, authors, year,
                                      publisher, publisher_address,
                                      journal, volume, number,
                                      pages):
            return jsonify({"message": "Reference added"}), 201
        else:
            return jsonify({"message": "Error occurred when adding reference"}), 501


@app.route("/get_all_references")
def get_all_references():
    return reference_service.get_all_references()


@app.route("/delete_references", methods=["POST"])
def delete_references():
    if request.method == "POST":
        refs_to_remove = request.get_json()
        if reference_service.delete_books_by_id(refs_to_remove):
            return jsonify({"message": "Deletion succesful"}), 201
        else:
            return jsonify({"message": "Error occurred when deleting reference(s)"}), 501


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('build', path)


if __name__ == "__main__":
    app.run(debug=True)
