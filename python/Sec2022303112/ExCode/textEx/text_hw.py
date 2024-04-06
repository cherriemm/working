#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

# 题目十一：摩斯码生成器
def morse_code(usr_str):
    morse = {'A': '. -', 'B': '- . . .', 'C': '- . - .', 'D': '- . .', 'E': '.', 'F': '. . - .',
             'G': '- -.', 'H': '. . . .','I': '. .', 'J': '. - - -', 'K': '- . -', 'L': '. - . .',
             'M': '- -', 'N': '- .', 'O': '- - -', 'P': '. - - .','Q': '- - . -', 'R': '. - .',
             'S': '. . .', 'T': '-', 'U': '. . -', 'V': '. . . -', 'W': '. - -', 'X': '- . . -',
             'Y': '- . - -', 'Z': '- - . .', '1': '. - - - -', '2': '. . - - -', '3': '. . . - -',
             '4': '. . . . -', '5': '. . . . .','6': '- . . . .', '7': '- - . . .', '8': '- - - . .',
             '9': '- - - - .', '0': '- - - - -', 's1': '       ', 's2': '   ',
    }

    i = 0
    ans = ''
    usr_str = usr_str.upper()
    while i < len(usr_str) - 1:
        if usr_str[i] == ' ':
            ans += morse['s1']
        else:
            if usr_str[i+1] != ' ':
                ans += morse[usr_str[i]] + morse['s2']
            else:
                ans += morse[usr_str[i]]
        i += 1
    if usr_str != '':
        ans += morse[usr_str[-1]]

    return ans







# 题目十二：词频统计
def word_freq(path):
    occurences = {}
    filter = ''
    # get the filter list
    with open("../testCase/testData/sight word.txt") as file_object:
        filter = file_object.read().lower()
    filter_list = filter.split()

    with open(path) as file_object:
        content = file_object.read().lower()
        new_content = ''
        i = 0
        # remove special characters
        while i < len(content):
            if content[i] in ['!', '`', '~', '@', '#', '$', '%', '^', '&', '*', ')', '_', '-', '+', '=', '[', ']', '{',
                               '}', '/', '?', ',', '.', ':', '\\', '"', '<', '>', '\n']:
                    new_content += ' '
            elif content[i] == '\'':
                pass
            else:
                new_content += content[i]
            i += 1

        words = new_content.split()
        for i in range(len(words)):
            if words[i] in occurences:
                occurences[words[i]] += 1
            elif words[i] not in filter_list :
                occurences[words[i]] = 1

    occurences = sorted(occurences.items(),reverse=True)
    occurences = sorted(occurences, key=lambda x: -x[1] )

    return occurences[0:10]




# 题目十四：敏感词过滤
def filter_words(user_input):
    with open("../testCase/testData/sensitive.txt") as file_object:
        filter = file_object.read()
        filter = re.sub(r'第.类.*\n', '', filter)
        filter = re.sub(r'\n', ' ', filter)
        filter = filter.split()
        for word in filter:
            if word in user_input:
                user_input = re.sub(word, '*'*len(word), user_input)

        return user_input




if __name__ == '__main__':
    li = morse_code('I love Python')
    print(li)



