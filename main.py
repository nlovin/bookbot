def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = character_count(text)
    sorted_chars = dict(sorted(num_chars.items(), key=sort_on, reverse=True))
    #print(sorted_chars)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{num_words} words found in the document")
    print()
    print_words(sorted_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    lowered_file_contents = file_contents.lower()
    text = list(lowered_file_contents)

    # counting individual characters
    the_count = {}
    for t in text:
        if t in the_count:
            the_count[t] += 1 
        else:
            the_count[t] = 1

    return the_count

def sort_dict(dct):
    sorted_dict = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def print_words(dct):
    for d in dct:
        print(f"The '{d}' character was found {dct[d]} times")

def sort_on(dct):
    return dct[1]


main()