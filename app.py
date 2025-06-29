from flask import Flask, request, jsonify
from models import view_books, add_book, update_book, delete_book, init_db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Return the instructions for using the API."""
    return "Welcome to the Book API! Use /books to get a list of books."

@app.route('/books', methods=['GET'])
def get_books():
    if request.method == 'GET':
        dictionary_books = []

        for book in view_books():
            book_dict = {
                "id": book[0],
                "title": book[1],
                "author": book[2]
            }

        dictionary_books.append(book_dict)

        return jsonify(dictionary_books), 200

@app.route('/books/<int:book_id>', methods=['GET', 'DELETE'])
def manage_book(book_id):
    # Search for the book with the given ID
    indexed_book = search_book(book_id, view_books())

    # If the book is not found
    if indexed_book is None:
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'GET':
        return jsonify(indexed_book), 200
    elif request.method == 'DELETE':
        delete_book(book_id)
        return jsonify({"message": "Book Successfully Deleted"}), 200

def search_book(book_id, books):
    indexed_book = None

    for book in books:
        if book[0] == book_id:
            indexed_book = {"id": book[0],
                "title": book[1],
                "author": book[2]
            }

    return indexed_book

@app.route('/books/<title>/<author>', methods=['POST'])
def post_book(title, author):
    if request.method == 'POST':
        new_book = add_book(title, author)
        return jsonify({"message": "Book added successfully!", 
                "data": new_book, "location" : f"books/{new_book['id']}"}), 201
    
@app.route('/books/<int:book_id>/<new_title>/<new_author>', methods=['PUT'])
def put_book(book_id, new_title, new_author):
    if request.method == 'PUT':
        update_book(book_id, new_title, new_author)
        updated_book = {'id': book_id, 'title': new_title, 'author': new_author}
        return jsonify({"message": "Book updated successfully!", 
                "data": updated_book}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
