def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_count = {}

    for char in text.lower():
        if char not in chars_count:
            chars_count[char] = 0
        chars_count[char] += 1
    
    return chars_count

def sort_on(dict):
    return dict["count"]

def sort_chars_count(words_count):
    sorted_chars_count = []

    for char in words_count:
        if char.isalpha():
            sorted_chars_count.append({"char": char, "count": words_count[char]})

    sorted_chars_count.sort(reverse=True, key=sort_on)

    return sorted_chars_count