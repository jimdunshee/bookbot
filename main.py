import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted = sort_char_counts(char_counts)
    print_report(book_path, num_words, sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

main()