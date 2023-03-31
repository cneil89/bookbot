def main():
    file_path = "books/frankenstein.txt"
    generate_report(file_path)

def generate_report(file_path):
    num_words, sorted_list = process_book(file_path)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter in sorted_list:
        if letter["ch"].isalpha():
            print(f"The '{letter['ch']}' character was found {letter['num']} times")
    
    print("--- End report ---")

def process_book(path):
    num_words = 0

    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        f.close()

    letters_d = count_letters(file_contents)
    sorted_list = get_sorted_dict(letters_d)
    return (num_words, sorted_list) 

def count_letters(content):
    letters_dict = {}
    letters_list = []
    for letter in content.lower():
        if letter not in letters_dict:
            letters_dict[letter] = 1
            continue
        letters_dict[letter] += 1

    return letters_dict 

def get_sorted_dict(val_dict):
    sorted_list = []
    for l in val_dict:
        sorted_list.append({"ch": l, "num": val_dict[l]})
    sorted_list.sort(reverse=True, key=lambda x:x["num"])
    return sorted_list

main()