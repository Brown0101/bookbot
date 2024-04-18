def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def get_number_of_words():  
    book_text = get_book_text()  
    return len(book_text.split())

def get_letter_count():
    book_text = get_book_text()
    count_dict = {}

    for letter in book_text:
        if letter.lower() in count_dict:
            count_dict[letter.lower()] += 1
        else:
            count_dict[letter.lower()] = 1

    return count_dict

def sort_on(data_dict):    
    return data_dict["num"]

def get_list_of_dicts(dict):
    build_list = []
    for key, value in dict.items():
        build_list.append({"name": key, "num": value})
    build_list.sort(reverse=True, key=sort_on)
    return build_list

def print_sorted_list(word_count, dict):
    sorted_list = get_list_of_dicts(dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for dict in sorted_list:
        if not dict["name"].isalpha():
            continue
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print("--- End report ---")


def main():
    word_count = get_number_of_words()
    letter_count_dict = get_letter_count()
    print_sorted_list(word_count, letter_count_dict)

if __name__ == "__main__":
    main()
