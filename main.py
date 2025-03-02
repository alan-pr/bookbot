import sys
from stats import count_words, count_chars, sort_chars_count

def getbooktext(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(text):
    print("    ============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    sorted_count = sort_chars_count(count_chars(text))

    for char_count in sorted_count:
        print(f"{char_count["char"]}: {char_count["count"]}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = getbooktext(sys.argv[1])
    print_report(text)

main()