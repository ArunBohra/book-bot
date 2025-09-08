def get_num_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def sort_char_counts(char_counts):
    chars_list = []
    for char in char_counts:
        chars_list.append({ "name": char, "num": char_counts[char] })

    return chars_list

