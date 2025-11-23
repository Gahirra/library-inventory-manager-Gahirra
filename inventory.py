from book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.filename = "books.txt"
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if book.title.lower() == title.lower():
                results.append(book)
        return results

    def display_all(self):
        if len(self.books) == 0:
            print("No books found.")
        else:
            for book in self.books:
                print(book)

    def save_data(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(book.to_line())

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():  # avoid blank lines error
                        title, author, isbn, status = line.strip().split(",")
                        book = Book(title, author, isbn, status)
                        self.books.append(book)
        except FileNotFoundError:
            self.books = []
