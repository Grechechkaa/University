# Телефонная книга
d = {}


def format_texta(a):
    for i in range(len(a)):  # остальные буквы имени и фамилии мелкие
        for j in range(1, len(a[i])):
            if ord(a[i][j]) >= 1040 and ord(a[i][j]) <= 1071:
                a[i] = a[i].replace(a[i][j], chr(ord(a[i][j]) + 32), a[i].count(a[i][j]))
    for i in range(len(a)):
        if ord(a[i][0]) >= 1072 and ord(a[i][0]) <= 1103:  # первая буква имени большая
            a[i] = a[i].replace(a[i][0], chr(ord(a[i][0]) - 32), 1)
    return a


def make_contact(d):
    a = input('Введите имя, фамилию в формате *Имя Фамилия* : ').split()
    proverka_na_2_elementa = True  # проверка на то, что введены имя, фамилия
    proverka_na_true_name_familia = True   # проверка на то, что в имени и фамилии одни буквы
    if len(a) != 2 or a[0].isalpha() == 0 or a[1].isalpha() == 0:
        proverka_na_true_name_familia = False
        proverka_na_2_elementa = False
        while proverka_na_true_name_familia == False and proverka_na_2_elementa == False:
            a = input('Неправильно ввели данные! Пожалуйста, проверьте, чтобы в имени и фамилии не было символов кроме букв, введите повторно: ').split()
            if len(a) == 2 and a[0].isalpha() and a[1].isalpha():
                proverka_na_true_name_familia = True
                proverka_na_2_elementa = True
    b = input('Введите номер телефона пользователя: ')
    proverka_na_true_number = True  # проверка на то, что введен правильный номер
    # внизу лютейшая проверка на то, если в номере не (11 символов и первая 8ка и все элементы цифры)
    # или же не (12 элементов и первая +7 и после плюса не одни цифры)
    if (not ((len(b) == 11 and b[0] == '8' and b.isdigit()) or (len(b) == 12 and b[0:2] == '+7' and b[1:].isdigit()))):
        proverka_na_true_number = False
        while proverka_na_true_number == False:
            b = input('Неправильно ввели номер! Пожалуйста, проверьте, чтобы в номере кроме цифр не было посторонних символов, введите повторно: ')
            if ((len(b) == 11 and b[0] == '8' and b.isdigit()) or (len(b) == 12 and b[0:2] == '+7' and b[1:].isdigit())):
                proverka_na_true_number = True
    if b[0] == '8':  # подгон под стандарт +7...
        b = b.replace('8', '+7', 1)
    format_texta(a)
    d[a[0] + ' ' + a[1]] = b
    print('Контакт успешно добавлен!')
    return d


def delete_contact(d):
    a = input('Введите имя и фамилию в формате: *Имя Фамилия*, чтобы удалить номер: ').split()
    proverka_na_2_elementa = True  # проверка на то, что введены имя, фамилия
    is_name_in_d = True  # проверка, что есть в словаре такой пользователь
    format_texta(a)
    if len(a) != 2 or (a[0] + ' ' + a[1] not in d): # если мы видим, что элемента уже не два или такого нет в словаре, то заходим в вайл
        proverka_na_2_elementa = False
        is_name_in_d = False
        while proverka_na_2_elementa == False and is_name_in_d == False: # пока пользователь не введёт правильно имя и фамилию, напоминаем
            a = input('Такого пользователя нет, проверьте и введите имя и фамилию ещё раз в формате: *Имя Фамилия*, чтобы удалить номер: ').split()
            format_texta(a)
            if len(a) == 2 and a[0] + ' ' + a[1] in d:
                proverka_na_2_elementa = True
                is_name_in_d = True
    del d[a[0] + ' ' + a[1]]
    print('Номер успешно удалён!')
    return d


def watch_contact(d):
    return print(d)


def change_contact(d):
    a = input('Введите имя и фамилию в формате *Имя Фамилия*, чтобы изменить номер: ').split()
    proverka_na_2_elementa = True  # проверка на то, что введены имя, фамилия
    is_name_in_d = True
    format_texta(a)
    if len(a) != 2 or (a[0] + ' ' + a[1] not in d):
        proverka_na_2_elementa = False
        is_name_in_d = False
        while proverka_na_2_elementa == False and is_name_in_d == False:
            a = input('Пользователя не существует или некорректно введены данные, введите в формате *Имя Фамилия*, чтобы изменить номер: ').split()
            format_texta(a)
            if len(a) == 2 and a[0] + ' ' + a[1] in d:
                proverka_na_2_elementa = True
                is_name_in_d = True
    # до этого момента функция работает так же как и функция с удалением номера по имени и фамилии
    b = input('Введите новый номер телефона: ')
    proverka_na_true_number = True  # проверка на то, что введен правильный номер
    # проверка на стандартизацию номера как в первой функции мэйк контакт
    if not ((len(b) == 11 and b[0] == '8' and b.isdigit()) or (len(b) == 12 and b[0:2] == '+7' and b[1:].isdigit())):
        proverka_na_true_number = False
        while proverka_na_true_number == False:
            b = input('Вы неправильно ввели номер, введите его повторно: ')
            if (len(b) == 11 and b[0] == '8' and b.isdigit()) or (len(b) == 12 and b[0:2] == '+7' and b[1:].isdigit()):
                proverka_na_true_number = True
    if b[0] == '8':
        b = b.replace('8', '+7', 1)
    d[a[0] + ' ' + a[1]] = b
    print('Номер успешно изменён!')
    return d


flag = True
print('Меню телефонной книги')
print('1. Создать контакт')
print('2. Удалить контакт по имени')
print('3. Просмотреть контакты')
print('4. Изменить контакт по имени')
print('5. Выход')
# print('Чтобы выйти из любой команды, напишите: выход')
while flag != False:
    komanda = input('Введите номер команды: ')
    if komanda == '1':
        make_contact(d)
    elif komanda == '2':
        delete_contact(d)
    elif komanda == '3':
        watch_contact(d)
    elif komanda == '4':
        change_contact(d)
    elif komanda == '5':
        watch_contact(d)
        print('До свидания!')
        flag = False
    elif komanda.isdigit() == 0 or not int(komanda) in [1, 2, 3, 4, 5]:
        print('Такой команды нет(, попробуйте ещё раз!')
