import sys

def load_data(filepath):
    f = open(filepath)
    text = f.read()
    f.close()
    return text


def get_most_frequent_words(text):
    punctuation_marks = [
        '.', ',', ';', '!', '?',
        ':', '-', '"', '/', '(',
        ')', '[', ']', '{', '}' 
    ]
    
    for s in punctuation_marks:
        text = text.replace(s, '')
    
    text = text.lower()
    
    words_list = text.split()

    most_frequent_words = sorted(
        { word : words_list.count(word) for word in words_list }.items(),
        key = lambda x: x[1],
        reverse = True
    )
    
    return most_frequent_words[:10]
    
    

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
    num = 0
    for (word, frequency) in most_frequent_words:
        num += 1
        print(num, ' ', word, ' / ', frequency)