from collections import Counter

def main():
    book_path = ("books/frankenstein.txt")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counter_dict = dict(amount_of_characters(text))
    print(f"{num_words}")
    print(f"{counter_dict}")

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


main()