import random
secret_member = random.randint(1,100)
my_set = set()
print('Компьютер загадал число от 1го до 100, попробуйте его отгадать')
while True:
    v = int(input('Введите число : '))
    my_set.add(v)
    if v < secret_member:
        print('Больше')
    elif v > secret_member:
        print('Меньше')
    else:
        print('Вы угадали число')
        break
with open(f'result.txt','w') as file:
    file.writelines(str(my_set))




