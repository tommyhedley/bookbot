def main():
    book_path = 'books/frankenstein.txt'
    print_report(book_path)

def print_report(path):
    text = get_book_text(path)
    title = f'--- Begin report of {path} ---'
    wordcount = get_wordcount(text)
    wordcount_txt = f'{wordcount} words found in the document'
    letter_list = get_letterlist(get_charcount(text))
    letter_list.sort(reverse=True, key=sort_on)
    print(title)
    print(wordcount_txt,'\n')
    for entry in letter_list:
        letter = entry['letter']
        count = entry['count']
        print(f"The '{letter}' character was found {count} times")
    print('\n--- End of report ---')

def sort_on(dict):
    return dict["count"]

def get_letterlist(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({'letter': char,'count': char_dict[char]})
    return char_list

def get_charcount(text):
    lower_text = text.lower()
    words = lower_text.split()
    char_count = {}
    for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count

def get_wordcount(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as book:
        return book.read()

main()