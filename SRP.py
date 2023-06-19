class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content


class BookPrinter:
    def print_book(self, book):
        print(f"Title: {book.get_title()}")
        print(f"Author: {book.get_author()}")
        print("Content:")
        print(book.get_content())


# Usage
book = Book("Python Programming", "John Smith", "Learn Python programming...")
printer = BookPrinter()
printer.print_book(book)
