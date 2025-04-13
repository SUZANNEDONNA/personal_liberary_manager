import json
import os

LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, "r") as file:
        return json.load(file)

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    isbn = input("Enter ISBN: ")
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn
    }
    
    library = load_library()
    library.append(book)
    save_library(library)
    print("✅ Book added!")

# View all books
def view_books():
    library = load_library()
    if not library:
        print("📚 Library is empty.")
        return

    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) [ISBN: {book['isbn']}]")

# Search for books
def search_books():
    term = input("Enter title or author to search: ").lower()
    library = load_library()
    results = [book for book in library if term in book['title'].lower() or term in book['author'].lower()]
    
    if not results:
        print("🔍 No matching books found.")
        return
    
    for book in results:
        print(f"{book['title']} by {book['author']} ({book['year']}) [ISBN: {book['isbn']}]")

# Delete a book by index
def delete_book():
    view_books()
    try:
        idx = int(input("Enter the number of the book to delete: ")) - 1
        library = load_library()
        if 0 <= idx < len(library):
            removed = library.pop(idx)
            save_library(library)
            print(f"🗑️ Deleted: {removed['title']} by {removed['author']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Menu
def menu():
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
