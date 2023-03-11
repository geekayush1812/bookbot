path_to_file = 'books/frankenstein.txt'


def count_words_in_text(text):
    words = text.split()
    return len(words)


def unique_char_dict_with_count(text: str):
    text = text.lower()
    char_count_dict = {}
    for char in text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict


def print_unique_char_dict_with_count(char_count_dict: dict[str, int]):
    for char, count in char_count_dict.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


def print_word_count(word_count: int):
    print(f"{word_count} words found in the document")


def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = 0
    unique_char: dict[str, int] = {}
    with open(path_to_file) as f:
        text = f.read()
        word_count = count_words_in_text(text)
        unique_char = unique_char_dict_with_count(text)
    print_word_count(word_count)
    print_unique_char_dict_with_count(unique_char)
    print("--- End report ---")


main()
