def main():
    report("books/frankenstein.txt")

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_unique_characters(text):
    lowercase_text = text.lower()
    characters = {}
    for character in lowercase_text:
        if character.isalpha():
            characters[character] = characters.get(character, 0) + 1
    return characters

def report(path):
    print(f"{'=' * 5} Report for {path} {'=' * 5}")
    text = read_file(path)
    word_count = count_words(text)
    print(f"The book has {word_count} words.")
    print()
    sorted_characters = sorted(count_unique_characters(text).items(), key=lambda x: x[1], reverse=True)
    for character, count in sorted_characters:
        print(f"The character '{character}' was found {count} times")
    print()
    print(f"{'=' * 5} End of Report {'=' * 5}")


main()