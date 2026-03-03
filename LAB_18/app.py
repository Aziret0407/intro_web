from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

# Sample data
books_data = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
]

@app.route('/')
def home():
    return '<h1>Welcome to Book Library</h1><p>Visit <a href="/books">/books</a> to see all books</p>'

@app.route('/books')
def list_books():
    return render_template('books.html', books=books_data, title="Book List")

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((b for b in books_data if b["id"] == book_id), None)
    if book:
        return render_template('book.html', book=book, title=book["title"])
    return f'<h1>Book not found</h1><p>Book with ID {escape(str(book_id))} does not exist</p>', 404

@app.route('/greet/<name>')
def greet(name):
    return f'<h2>Hello, {escape(name.capitalize())}!</h2>'

@app.route('/books/<int:year>')
def books_by_year(year):
    filtered = [b for b in books_data if b["year"] == year]
    if filtered:
        return render_template('books.html', books=filtered, title=f"Books from {year}")
    return f'<h1>No books found</h1><p>No books published in {escape(str(year))}</p>', 404

if __name__ == '__main__':
    app.run(debug=True)