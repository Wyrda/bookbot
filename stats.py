from collections import Counter
import sys

def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counter_dict = dict(amount_of_characters(text))
    list_of_dict = [{"char": k, "num": v} for k, v in counter_dict.items()
                    if k.isalpha()
    ]
    list_of_dict.sort(reverse=True, key=sort_on)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_dict:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def amount_of_characters(text):
    lowered_text = text.lower()
    character_count = Counter(lowered_text)
    return character_count


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]