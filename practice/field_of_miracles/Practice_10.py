import os
from pdf2docx import *
from docx2pdf import convert
from PIL import Image
import PySimpleGUI as sg

'''cwd = os.getcwd()
print(cwd)'''


def change_catalog(path: str) -> str:
    '''смена каталога'''
    os.chdir(path)
    return os.getcwd()


def change_pdf2docx(path: str) -> None:
    '''создание нового файла с расширением Docx из PDF'''
    pdf_file = path
    docx_file = path[:-3] + 'docx'
    parse(pdf_file, docx_file)


def change_docx2pdf(path: str) -> None:
    """создание нового файла с расширением PDF из Docx"""
    convert(path)


def compression_image(path: str, compression_k: int) -> None:
    """Сжатие изображения"""
    image_file = Image.open(path)
    image_file.save(f"new {path}", quality=compression_k)


def pdf_in_directory() -> list:
    '''Нахождение файлов в директории с расширением PDF'''
    print('Список файлов с расширением PDF в данном каталоге')
    list_with_pdf = [i for i in os.listdir(path='.') if i[-4:] == '.pdf']
    return list_with_pdf


def docx_in_directory() -> list:
    '''Нахождение файлов в директории с расширением Docx'''
    print('Список файлов с расширением Docx в данном каталоге')
    list_with_docx = [i for i in os.listdir(path='.') if i[-5:] == '.docx']
    return list_with_docx


def images_in_directory() -> list:
    '''Нахождение файлов в директории с расширением "jpeg","jpg","gif","png" '''
    print('Список файлов с расширением "jpeg","jpg","gif","png" в данном каталоге')
    list_with_images = [i for i in os.listdir(path='.') if
                        i[-5:] == '.jpeg' or i[-4:] == '.jpg' or i[-4:] == '.gif' or i[-4:] == '.png']
    return list_with_images


def files_with_start(start_str: str) -> list:
    '''Нахождение файлов с подстрокой в начале названия'''
    list_with_start = [i for i in os.listdir(path='.') if i.startswith(start_str)]
    return list_with_start


def files_with_end(end_str: str) -> list:
    '''Нахождение файлов с подстрокой в конце названия'''
    list_with_end = [i for i in os.listdir(path='.') if i.split('.')[-2].endswith(end_str)]
    return list_with_end


def files_with_str(str: str) -> list:
    '''Нахождение файлов с подстрокой в названии'''
    list_with_str = [i for i in os.listdir(path='.') if str in i]
    return list_with_str


def files_with_expansion(expansion: str) -> list:
    '''Нахождение файлов по расширению'''
    list_with_expansion = [i for i in os.listdir(path='.') if i.endswith(expansion.rstrip())]
    return list_with_expansion


def chosen1(file) -> None:
    '''Выбор 1 в меню. Функция выводит резаультат функции нахождения ПДФ в директории.
    Выводит эти файлы.
    Потом пользователь вводит команду для преобразования.
    если 0, то преобразуются все файлы, если -1, то действие отменяется, и мы возвращаемся в меню.'''
    list_with_pdf = file
    '''for i in range(len(list_with_pdf)):
        print(f"{i + 1}. {list_with_pdf[i]}")
    print()
    number_pdf = input(
        ('Введите номер файла для преобразования в Docx (чтобы преобразовать всё, введите 0; для отмены -1): ')).strip()
    if number_pdf == '0':'''
    print(list_with_pdf)
    for i in range(len(list_with_pdf)):
        change_pdf2docx(list_with_pdf[i])
    '''elif number_pdf == '-1':
        print()
    else:
        change_pdf2docx(list_with_pdf[int(number_pdf) - 1])
        print(f'Преобразование файла {list_with_pdf[int(number_pdf) - 1]} из PDF в Docx прошло успешно!')'''


def chosen2(file) -> None:
    '''Выбор 2 в меню. Функция выводит резаультат функции нахождения Docx в директории.
        Выводит эти файлы.
        Потом пользователь вводит команду для преобразования в PDF.
        если 0, то преобразуются все файлы, если -1, то действие отменяется, и мы возвращаемся в меню.'''
    list_with_docx = file
    '''for i in range(len(list_with_docx)):
        print(f"{i + 1}. {list_with_docx[i]}")
    print()
    number_docx = (
        input(('Введите номер файла для преобразования в PDF (чтобы преобразовать всё, введите 0; для отмены -1): ')))'''
    # if number_docx == '0':
    for i in range(len(list_with_docx)):
        change_docx2pdf(list_with_docx[i])
        # print(f'Преобразование всех файлов в каталоге из Docx в PDF прошло успешно!')
    '''elif number_docx == '-1':
        print()
    else:
        change_docx2pdf(list_with_docx[int(number_docx) - 1])
        print(f'Преобразование файла {list_with_docx[int(number_docx) - 1]} из Docx в PDF прошло успешно!')'''


def chosen3(list_with_images, koef) -> None:
    '''Выбор 3 в меню. Функция выводит результат функции нахождения изображений в директории.
    Выводит эти файлы.
    Потом пользователь вводит команду для сжатия изобржаений.
    если 0, то преобразуются все файлы, если -1, то действие отменяется, и мы возвращаемся в меню.'''
    '''for i in range(len(list_with_images)):
        print(f"{i + 1}. {list_with_images[i]}")
    print()'''
    '''number_images = int(input(('Введите номер файла для сжатия (чтобы сжать всё, введите 0, для отмены -1): ')))
    compression_k = int(input('Введите на сколько надо сжать изображение от 0 до 95: '))'''
    # if number_images == 0:
    for i in range(len(list_with_images)):
        compression_image(list_with_images[i], koef)
    '''print('Все изображения из каталога сжаты!')
    elif number_images == '-1':
        print()
    else:
        compression_image(list_with_images[int(number_images) - 1], compression_k)
        print(f'Изображение {list_with_images[int(number_images) - 1]} успешно сжато!')'''


def delete_file(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
    else:
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(path)


def delete(path: str) -> bool:
    if not os.path.exists(path):
        return False
    delete_file(path)
    return True


def deleted(choose_for_delete: str) -> None:
    '''Программа вызывается от chosen 4.
    Если выбираем 1, то удаляем по началу строки
    2: удаляем все файлы по концу введённой строки
    3: удаляем все файлы с введённой подстрокой
    4: удаляем все файлы по введённому расишрению'''
    if choose_for_delete == '1':
        start_str = input('Введите начало строки, с которой хотите удалить файл: ')
        fws = files_with_start(start_str)
        for i in fws:
            delete(i)
    elif choose_for_delete == '2':
        end_str = input('Введите конец строки, с которой хотите удалить файл: ')
        fwe = files_with_end(end_str)
        for i in fwe:
            delete(i)
    elif choose_for_delete == '3':
        estr = input('Введите подстроку, с которой хотите удалить файл: ')
        fwstr = files_with_str(estr)
        for i in fwstr:
            delete(i)
    elif choose_for_delete == '4':
        expansion = input('Введите расширение, с которым хотите удалить файлы: ')
        fwexpansion = files_with_expansion(expansion)
        for i in fwexpansion:
            delete(i)


def chosen4() -> None:
    '''Интерфейс выбора 4 в главном меню.'''
    print('1. Удалить все файлы, начинающиеся на определенную подстроку')
    print('2. Удалить все файлы, заканчивающиеся на определенную подстроку')
    print('3. Удалить все файлы, содержащие определенную подстроку')
    print('4. Удалить все файлы по расширению')
    choose_for_delete = input('Введите номер команды: ')
    deleted(choose_for_delete)


def show(file, flag=None, koef=None):
    if not flag:
        list1 = []
        arr = set([i.split('.')[-1] for i in file])
        if len(arr) == 1:
            arr = list(arr)[0]
            if arr == 'jpg' or arr == 'png' or arr == 'jpeg':
                list1.append('Произвести сжатие изображений')
            elif arr == 'pdf':
                list1.append('Преобразовать PDF в Docx')
            elif arr == 'docx':
                list1.append('Преобразовать Docx в PDF')
        if len(arr) > 0:
            list1.append('Удалить')
        return list1
    if flag:
        if 'сжатие' in flag:
            chosen3(file, koef)
            return f"Сжатие изображения(-ий) прошло успешно!"
        elif 'PDF в Docx' in flag:
            chosen1(file)
            return f"Преобразование файла(-ов) в каталоге из PDF в Docx прошло успешно!"
        else:
            chosen2(file)
            return f"Преобразование файла(-ов) в каталоге из Docx в PDF прошло успешно!"


def delete(file):
    for i in range(len(file)):
        os.remove(file[i])
    return 'Файл(-ы) удален'


def files_with_str1(str: str, file_list: list) -> list:
    '''Нахождение файлов с подстрокой в названии'''
    list_with_str1 = [i for i in file_list if str in ''.join(i.split())]
    '''list_with_str1 = []
    for i in file_list:
        if ''.join(i.split()).indexOf(str) > 0:
            list_with_str1.append(i)'''
    return list_with_str1


def files_with_start1(start_str: str, file_list: list) -> list:
    '''Нахождение файлов с подстрокой в начале названия'''
    list_with_start = [i for i in file_list if i.startswith(start_str)]
    return list_with_start


def files_with_end1(end_str: str, file_list: list) -> list:
    '''Нахождение файлов с подстрокой в конце названия'''
    list_with_end = [i for i in file_list if i.split('.')[-2].endswith(end_str)]
    return list_with_end


def files_with_expansion1(expansion: str, file_list: list) -> list:
    '''Нахождение файлов по расширению'''
    list_with_expansion = [i for i in file_list if i.endswith(expansion.rstrip())]
    return list_with_expansion


def spin(window):
    layout = [
        [sg.Text("Введите степень сжатия изображения(-ий):")],
        [sg.Spin(values=[x for x in range(1, 96)], readonly=True, key='-SPIN-')],
        [sg.Button('OK', size=(8, 1), key='-OK-')]

    ]
    new_window = sg.Window("Image Koef", layout)

    while True:
        event, values = new_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-OK-":
            window["-SHOW-"].update(
                show(window["-NEW LIST-"].get_list_values(), window["-SHOW-"].get().split('\n')[0],
                     new_window["-SPIN-"].get()))
        new_window.close()


def gms_window():
    layout = [
        [sg.Text("Удаление по подстроке: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE STR--', button_color='red')],
        [sg.Text("Удаление по началу названия: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE START STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE START STR--', button_color='red')],
        [sg.Text("Удалению по концу названия: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE END STR--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE END STR--', button_color='red')],
        [sg.Text("Удаление по расширению: ", expand_y=True, expand_x=True),
         sg.InputText(key='--INPUT DELETE EXP--', enable_events=True)],
        [sg.Button('Удалить', size=(8, 1), key='--DELETE EXP--', button_color='red')],
    ]
    # Возвращаем окно с названием "GMS to Deg", содержащее описанный выше интерфейс
    return sg.Window('GMS to Deg', layout, size=(500, 500), resizable=True, finalize=True)


def office():
    file_list_column = [
        [sg.Text("File Change"), sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse()],
        [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
    ]
    image_viewer_column = [
        [sg.Text("Доступные команды к файлам:")],
        [sg.Text(size=(40, 5), key="-SHOW-")],
        [sg.Listbox(values=[], enable_events=True, size=(40, 10), key="-NEW LIST-")],
        [sg.Button('Действие', size=(8, 1), disabled=True, key="-ENTER-")],
        [sg.Button('Удаление файлов', size=(8, 1), disabled=False, button_color='red', key='-DELETE-')],
        [sg.Button('Убрать', size=(8, 1), disabled=True, key='-CLEAR-')],
        [sg.Button('Убрать все', size=(8, 1), disabled=True, key='-CLEAR ALL-')]
    ]
    '''delete_viewer_column = [

        [sg.Text("Доступно удаление по:")],
        [sg.Text(size=(40, 5), key="-SHOW DELETE-")],

    ]'''
    layout = [[sg.Column(file_list_column), sg.VSeperator(), sg.Column(image_viewer_column), ]]
    # layout1 = [[sg.Column()]]
    window = sg.Window("Image Viewer", layout)
    # window_for_delete = sg.Window("Удаление файлов", layout1)
    new_list = []
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            change_catalog(folder)
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)
        '''try:
            window["-SHOW-"].update(show(values["-FILE LIST-"]))
        except:
            pass'''
        '''if len(window["-SHOW-"].get().split('\n')) == 2:
            window["-ENTER-"].update(disabled=False)
        else:
            window["-ENTER-"].update(disabled=True)
            #window["-SHOW-"].update(show_method(values["-FILE LIST-"]))
        #print(window["-SHOW-"].get().split('\n'))
        if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
            window["-DELETE-"].update(disabled=False)
        else:
            window["-DELETE-"].update(disabled=True)'''
        if event == "-FILE LIST-":
            if values["-FILE LIST-"][0] not in new_list:
                new_list.append(values["-FILE LIST-"][0])
            window["-NEW LIST-"].update(new_list)
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR ALL-"].update(disabled=False)
            if len(window["-SHOW-"].get().split('\n')) == 2:
                window["-ENTER-"].update(disabled=False)
            else:
                window["-ENTER-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
                window["-DELETE-"].update(disabled=False)
            else:
                window["-DELETE-"].update(disabled=True)

        elif event == "-ENTER-":
            if 'сжатие' in window["-SHOW-"].get().split('\n')[0]:
                spin(window)
            else:
                window["-SHOW-"].update(
                    show(window["-NEW LIST-"].get_list_values(), folder + '/' + window["-SHOW-"].get().split("\n")[0]))
            window["-NEW LIST-"].update('')
            new_list.clear()
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)

            folder = values["-FOLDER-"]
            change_catalog(folder)
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)

        elif event == "-DELETE-":
            window_delete = gms_window()
            flag_delete = True
            while flag_delete:
                window1, event1, values1 = sg.read_all_windows()
                if window1 == window_delete:
                    if event1 == '--INPUT DELETE STR--':
                        delete_str = window1['--INPUT DELETE STR--'].get()
                        print(delete_str)
                    elif event1 == sg.WINDOW_CLOSED:
                        window1.close()
                        flag_delete = False
                    elif event1 == '--INPUT DELETE START STR--':
                        delete_start_str = window1['--INPUT DELETE START STR--'].get()
                    elif event1 == '--INPUT DELETE END STR--':
                        delete_end_str = window1['--INPUT DELETE END STR--'].get()
                    elif event1 == '--INPUT DELETE EXP--':
                        delete_exp = window1['--INPUT DELETE EXP--'].get()
                    elif event1 == '--DELETE STR--':
                        fws1 = files_with_str1(delete_str, file_list)
                        for i in fws1:
                            os.remove(i)
                        # print(files_with_str1(delete_str, file_list))
                    elif event1 == '--DELETE START STR--':
                        fwstart1 = files_with_start1(delete_start_str, file_list)
                        for i in fwstart1:
                            os.remove(i)
                        # print(files_with_start1(delete_start_str, file_list))
                    elif event1 == '--DELETE END STR--':
                        fwe1 = files_with_end1(delete_end_str, file_list)
                        for i in fwe1:
                            os.remove(i)
                        # print(files_with_end1(delete_end_str, file_list))
                    elif event1 == '--DELETE EXP--':
                        fwexp1 = files_with_expansion1(delete_exp, file_list)
                        for i in fwexp1:
                            os.remove(i)

                        # print(files_with_expansion1(delete_exp, file_list))

            '''window["-SHOW-"].update('')
            new_list.clear()
            delete(window["-NEW LIST-"].get_list_values())
            window["-NEW LIST-"].update('')
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)
            folder = values["-FOLDER-"]
            file_change.change_catalog(folder)'''
            try:
                file_list = os.listdir(folder)
            except:
                file_list = []
            fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
            window["-FILE LIST-"].update(fnames)

        elif event == "-NEW LIST-":
            window["-CLEAR-"].update(disabled=False)

        elif event == "-CLEAR-":
            new_list.remove(values["-NEW LIST-"][0])
            window["-NEW LIST-"].update(new_list)
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR-"].update(disabled=True)
            if len(window["-NEW LIST-"].get_list_values()) == 0:
                window["-CLEAR ALL-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) == 2:
                window["-ENTER-"].update(disabled=False)
            else:
                window["-ENTER-"].update(disabled=True)
            if len(window["-SHOW-"].get().split('\n')) > 0 and window["-SHOW-"].get().split('\n')[0] != '':
                window["-DELETE-"].update(disabled=False)
            else:
                window["-DELETE-"].update(disabled=True)

        elif event == "-CLEAR ALL-":
            window["-NEW LIST-"].update('')
            new_list.clear()
            window["-SHOW-"].update('\n'.join(show(new_list)))
            window["-CLEAR-"].update(disabled=True)
            window["-CLEAR ALL-"].update(disabled=True)
            window["-ENTER-"].update(disabled=True)
            window["-DELETE-"].update(disabled=True)

        if len(window["-NEW LIST-"].get_list_values()) > 0:
            pass
    window.close()


office()
