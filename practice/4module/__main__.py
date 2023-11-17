import __init__
import saver
data_name = input(f'Введите имя файла, В котором надо отсортировать данные')
data = __init__.read_file(data_name)
save_name = input(f'Введите имя файла, В который вы хотите сохранить данные ')
print(f'{saver.save_file(save_name, data)}')