# words.py

def print_upper_words(words):
   
    for word in words:
        print(word.upper())

def print_words_starting_with(words, letters):
    
    for word in words:
        if word[0].lower() in letters:
            print(word.upper())

if __name__ == "__main__":
    # Test the functions
    words_list = ["apple", "banana", "Orange", "elephant", "car", "zebra"]
    
    print("Original words:")
    for word in words_list:
        print(word)

    print("\nUppercase words:")
    print_upper_words(words_list)

    print("\nWords starting with 'e':")
    print_words_starting_with(words_list, {'e'})

    print("\nWords starting with 'e' or 'z':")
    print_words_starting_with(words_list, {'e', 'z'})
