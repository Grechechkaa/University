from english_learn import *


def show():
    list = get_words()
    print(list)
    normal_list = (normal_words(list))
    print(normal_list)
    d = count_words(normal_list)
    print(d)
    sorted_list = (sort_words(d))
    print(sorted_list)
    dictionary = translate_words(sorted_list)
    with open('dictionary.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Исходное слово', 'Перевод', 'Количество упоминаний'])
        for i in dictionary:
            writer.writerow(i)
    print('Словарь успешно создан!')


if __name__ == "__main__":
    show()
