def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")

    sort_on(num_characters)

    print("--- End report ---")

def get_num_characters(text):
    lowercase_char = text.lower()

    char_counts = {}
    for char in lowercase_char:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(num_characters):
    sorted_char = sorted(num_characters.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char:
        print(f"the '{char}' character was found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()