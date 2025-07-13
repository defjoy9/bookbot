import sys
from stats import get_number_of_words
from stats import get_repeated_chars
from stats import get_dic_convert
from stats import sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if not len(sys.argv) >=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dict = get_repeated_chars(text)
    new_dic = get_dic_convert(chars_dict)
    new_dic.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dic in new_dic:
        key = dic['character']
        value = dic['number']
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

main()