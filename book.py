class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} copies available")

    def update_stock(self, new_stock):
        self.stock = new_stock
        print("Stock updated successfully")



# Additional functions related to book management
def create_book(title, author, price, stock):
    return Book(title, author, price, stock)

def check_stock(book):
    return book.stock
