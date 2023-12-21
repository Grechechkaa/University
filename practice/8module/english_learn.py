import pymorphy3
import pymorphy3_dicts_ru
import translate
from translate import Translator
import csv


def get_words():
    f = open('text.txt', mode="r", encoding="utf8")
    strings = f.read().splitlines()
    f.close()
    strings_list = [strings[i].split(' ') for i in range(len(strings))]
    clear_strings_list = []
    for i in range(len(strings_list)):
        for word in strings_list[i]:
            word = ''.join(filter(str.isalpha, word)).lower()
            if len(word) > 0:
                clear_strings_list.append(word)
    return clear_strings_list


def normal_words(clear_strings_list):
    normal_list = []
    for word in clear_strings_list:
        morph = pymorphy3.MorphAnalyzer()
        normal_list.append(morph.parse(word)[0].normal_form)
    return normal_list


def count_words(normal_list):
    d = {}
    for i in range(len(normal_list)):
        if not normal_list[i] in d:
            d[normal_list[i]] = 1
        else:
            d[normal_list[i]] += 1
    return d


def sort_words(d):
    sorted_d = sorted(d.items(), key=lambda kv: kv[1])
    sorted_d.reverse()
    return sorted_d


def translate_words(sorted_list):
    translate_dictionary = []
    for i in range(len(sorted_list)):
        translation = Translator(from_lang='ru', to_lang="en").translate(str(sorted_list[i][0]))
        translate_dictionary.append([sorted_list[i][0], translation, sorted_list[i][1]])
        print(f'Переведено {i}/{len(sorted_list)}...')
    return translate_dictionary
