def read_book(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content


def count_words(book_content):
    total_words = book_content.split()

    return len(total_words)


def count_chars(book_content):
    char_count = {}

    for content in book_content:
        content = content.lower()
        char_count[content] = 1 + char_count.get(content, 0)

    return char_count


def char_dict_to_sorted_list(char_count_dict):
    sorted_list = []

    for key, value in char_count_dict.items():
        sorted_list.append({"char": key, "num": value})

    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list


def print_report(file_path, word_count, sorted_list):
    print(f"--- Begin report of {file_path[2:]} ---")
    print(f"{word_count} words found in the document")
    print()

    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"The {char_dict['char']} was found {char_dict['num']} times")

    print("--- End report ---")


def main():
    file_path = "./books/frankenstein.txt"

    book_content = read_book(file_path=file_path)
    word_count = count_words(book_content=book_content)
    char_count_dict = count_chars(book_content=book_content)
    sorted_list = char_dict_to_sorted_list(char_count_dict=char_count_dict)

    print_report(file_path=file_path, word_count=word_count, sorted_list=sorted_list)


main()
