import sys
import re
import collections

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):    
    text = text.lower()
    words_list = re.sub(r'[^ \nа-яa-z]', '', text).split()
    words_count = 10
    return collections.Counter(words_list).most_common(words_count)


if __name__ == '__main__':
    if len (sys.argv) == 1:
        filepath = input('Enter file path > ')
    else:
        if len (sys.argv) > 2:
            print ("Error: too many parameters are transferred")
            sys.exit (1)
        filepath = sys.argv[1]
        
    text = load_data(filepath)

    most_frequent_words = get_most_frequent_words(text)
    print('10 words with the most frequency (word / frequency):')
    for (num, (word, frequency)) in enumerate(most_frequent_words):
        print(num + 1, ' ', word, ' / ', frequency)