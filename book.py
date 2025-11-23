class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        else:
            return False

    def return_book(self):
        self.status = "available"

    def to_line(self):
        return f"{self.title},{self.author},{self.isbn},{self.status}\n"

    def __str__(self):
        return self.title + " | " + self.author + " | " + self.isbn + " | " + self.status
