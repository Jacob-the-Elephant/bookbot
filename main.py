def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    word_dict = letter_count(text)
    ordered_dict = order_dict(word_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document!")
    print()
    summarize(ordered_dict)

def get_book_text(path):  
    with open(path) as f:
        return f.read()

def word_count(string):
    words = string.split()
    return len(words)

def letter_count(string):
    lowered_string = string.lower()
    letters = {}
    for i in lowered_string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def order_dict(dict):
    my_list = list(dict.items())
    sorted_list = sorted(my_list, key=lambda item: item[1], reverse=True)
    filtered_list = [(key, value) for key, value in sorted_list if key.isalpha()]
    return filtered_list

def summarize(tuple):
    for i in tuple:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

main()