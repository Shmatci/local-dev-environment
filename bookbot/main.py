import string

def main():
    book_path = "C:/Users/Tammy/Pictures/bootdev/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    counter = count_words(text)

    print(f"-- Begin report of {book_path} ---")
    print(f'There are {counter} words in the file.')
    print("")

    letters = count_letters(text)
    for char in letters:
        print (f"The '{char}' character was found {letters[char]} times")
    print("")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(input_text):
    """
    Counts number of words, given input_text.
    param:
        input_text must be valid string
    returns total number of words in input_text
    """
    counter = 0
    words = input_text.split()
    counter += len(words)
    return counter
    
def count_letters(input_letters):
    """
    Counts how many times each character is found in the given text (input_letters)
    Input text must be a valid string with lowercase letters.
    Returns total number of each char in text.    
    """

    words = input_letters.lower()
    counter = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    abc = list(alphabet)
    letters_count = {}

    for i in abc:
        letters_count[i] = counter
    
    for char in words:
        if char in letters_count:
            letters_count[char] += 1    

    return letters_count


 
main()




