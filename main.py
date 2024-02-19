def read_book(path_to_book):
    with open(path_to_book) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for i in text:
        letter = i.lower()
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1 
    return letters

def sort_on(dict):
    return dict["count"]

def generate_report(word_count, letter_count):
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    book_text = read_book(book_path)
    print(f"{count_words(book_text)} words in book")
    book_dict = count_letters(book_text)
    book_dict_list = []
    for k, v in book_dict.items():
        if k.isalpha():
            book_dict_list.append({"letter": k, "count": v})
    book_dict_list.sort(reverse=True, key=sort_on)
    for entry in book_dict_list:
        print(f"The {entry['letter']} character appears {entry['count']} times")

def main():
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)
    word_count = count_words(book)
    letter_dict = count_letters(book)
    generate_report(word_count, letter_dict)

    
if __name__ == "__main__":
    main()