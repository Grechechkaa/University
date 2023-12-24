from random import randint
number = randint(0,100)
p = 0
k = input('введите число: ')
while k != number:
    k = int(input('повтори попытку: '))
    p += 1
    if k < number:
        print('число меньше,чем загадал компьютер')
        
    elif k > number:
        print('число больше,чем загадал компьютер')
    else:
        print('Молодец,угадал ' + str(p) + ' попыток')
        number = randint(0,100)    
            
print(k)
print(number)

