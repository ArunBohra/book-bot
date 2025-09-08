import sys
from stats import get_num_words, count_characters, sort_char_counts


def get_book_text(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()
    except Exception as e:
        print(e)


def print_report(file_name, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")

    for item in char_count:
        print(f"{item['name']}: {item['num']}")


def analyse_file(file_name):
    file_contents = get_book_text(file_name)

    num_words = get_num_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_chars = sort_char_counts(char_count)
    print_report(file_name, num_words, sorted_chars)


def main():
    try:
        if (len(sys.argv) != 2):
            raise Exception("Usage: python3 main.py <path_to_book>")
        else:
            file, file_path = sys.argv
            analyse_file(file_path)
            sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)


main()

