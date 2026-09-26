class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"

class Book_Manager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.author.lower() == book.author.lower():
                return False
        self.books.append(book)
        return True

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def search_book(self, title):
        title_clean = title.strip().lower()
        found_books = []
        for book in self.books:
            if title_clean == book.title.lower():
                found_books.append(book)
        return found_books

    def delete_book(self, title):
        title_clean = title.strip().lower()
        for book in self.books:
            if title_clean == book.title.lower():
                self.books.remove(book)
                return 'book removed successfully'
        return 'book not found'

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty! Try again.")
            
def main():
    manager = Book_Manager()
    while True:
        print('\n==== BOOK MANAGER ====')
        print('1. add book')
        print('2. show book')
        print('3. search book')
        print('4. delete book')
        print('5. Exit')

        choice = input('Choose operation: ').strip()
        if choice == '1':
            title = get_non_empty_input('Enter book title: ')
            author = get_non_empty_input('Enter author: ')
            while True:
                year = input('Enter year: ').strip()
                if year.isdigit():
                    year = int(year)
                    break
                print('Invalid year! Try again')
            
            book = Book(title, author, year)
            if manager.add_book(book):
                print('Book added successfully!')
            else:
                print(f'Error: Book by author "{author}" already exists!')
                
        elif choice == '2':
            manager.show_books()
        elif choice == '3':
            title = get_non_empty_input('Enter title: ')
            results = manager.search_book(title)
            if results:
                for book in results:
                    print(book)
            else:
                print('book not found')
        elif choice == '4':
            title = get_non_empty_input('Enter title: ')
            print(manager.delete_book(title))
        elif choice == '5':
            print('Goodbye!!!')
            break
        else:
            print('Invalid choice!')

main()