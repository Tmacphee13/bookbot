def read_book(path_to_book):
    with open(path_to_book) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)
    num_words = count_words(book)
    print(f"Number of words in book: {num_words}")
    
if __name__ == "__main__":
    main()
