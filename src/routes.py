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

        #Martin: addition attempt to handle additional article inputs starts
        journal = request.form["journal"]
        volume = request.form["volume"]
        number = request.form["number"]
        pages = request.form["pages"]
        #Martin: addition attempt to handle additional article inputs ends

        print(authors, title, year, publisher, publisher_address)

        #Martin: addition attempt to handle insert article to Article table and book into Book table starts
        if journal == volume == number == pages == "":
            if reference_service.add_book(authors, title, year,
                                      publisher, publisher_address):
                return jsonify({"message": "Reference added"}), 201
        elif publisher == publisher_address == "":
            if reference_service.add_article(authors, title, journal, 
                                             year, volume, number, pages):
                return jsonify({"message": "Reference added"}), 201
        #Martin: addition attempt to handle insert article to Article table and book into Book table ends

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
        
        #Martin: addition attempt to delete article starts
        elif reference_service.delete_article_by_id(refs_to_remove):
            return jsonify({"message": "Deletion succesful"}), 201
        #Martin: addition attempt to delete article ends
        
        else:
            return jsonify({"message": "Error occurred when deleting reference(s)"}), 501


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('build', path)


if __name__ == "__main__":
    app.run(debug=True)
