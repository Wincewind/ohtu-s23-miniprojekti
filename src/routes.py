from app import app
from flask import jsonify, request, send_from_directory
from services.reference_services import reference_service


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/add_reference", methods=["POST"])
def add_reference():
    if request.method == "POST":
        authors = request.form.get("authors", None)
        title = request.form.get("title", None)
        year = request.form.get("year", None, type=int)
        publisher = request.form.get("publisher", None)
        publisher_address = request.form.get("publisher_address", None)
        journal = request.form.get("journal", None)
        volume = request.form.get("volume", None, type=int)
        number = request.form.get("number", None,type=int)
        pages = request.form.get("pages", None)
        ref_type = request.form.get("type", None)

        if reference_service.add_book(title=title, ref_type=ref_type, authors=authors, year=year,
                            publisher=publisher, publisher_address=publisher_address,
                            journal=journal, volume=volume, number=number,
                            pages=pages):
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
