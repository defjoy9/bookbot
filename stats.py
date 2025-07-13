def get_number_of_words(text):
    text = text.split()
    return len(text)

def get_repeated_chars(text):
    repeated_chars = {}

    for char in text.lower():
        if char in repeated_chars:
            repeated_chars[char] += 1
        else:
            repeated_chars[char] = 1
    return repeated_chars

def sort_on(items, value="number"):
        return items[value]

def get_dic_convert(dic):
    new_dic = []
    for key, value in dic.items():
        new_dic.append({'character': key,
                'number': value})
    return new_dic
