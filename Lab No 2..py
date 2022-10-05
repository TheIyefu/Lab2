import csv
import os
import time
def esc(code):
    return f'\u001b[{code}m'

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

#1. Флаг Нидерландов
def create_flag_netherlands(y, x):
    """ Функция, которая создает флаг Нидерландов"""
    flag = ''
    for i in range(y):
        for j in range(x):
            if i < y//3:
                flag += RED
            elif i < 2*y//3:
                flag += WHITE
            else:
                flag += BLUE
            flag += ' '
        flag += f'{END}\n'
    return flag

print(f'1. принт флага Нидерландов\n{create_flag_netherlands(6, 36)}')

#2.сгенерированный узор, № 3
def create_pattern(x,a):
    """генерирует узор, x - высота, a - количество циклов"""
    pattern = ''
    y = a*x
    for i in range(x):
        for j in range(y):
            if j>x-1 and j%x == 0:
                continue
            if j>x-1:
                times = j // x
                j = j-(times*x)
            if i == j or i+j == x-1:
                pattern += f'{WHITE}   {END}'
            else:
                pattern += '   '
        pattern += '\n'
    print(pattern)

print('2. Сгенерированный Узор, № 3')
create_pattern(7, 2)


#3.Cоздает график функции, f(x) = 2x
def create_graph(y,x):
    """ это создает график функции f(x) = 2x, где y = f(x)"""
    graph = ''
    for i in range(y, -3, -1):
        for j in range(-1, x+1, 1):
            if j == -1 and i > -1:
                graph += f' {i}|'
            elif i == -2 and j != -1:
                graph += f' {j} '
            elif i == -1 and j == -1:
                graph += '   '
            elif i == -1:
                graph += '---'
            elif i == 2*j and i>= 0 and j>= 0:
                graph += '\33[31m * '
                graph += END
            else:
                graph += f'   '
        graph += '\n'
    print(graph)

print('3. График функции, f(x) = 2x')
create_graph(9,9)

#4.Cоздает гистограмму на основе условия № 3
def get_percent():
    """Bычисляет процент записей из csv-файла и создает список"""
    to_1990 = 0
    from_1990 = 0
    with open('books-en.csv', 'r') as csv_file:
        table = list(csv.reader(csv_file, delimiter=';'))
        for row in table:
            if row == table[0]:
                continue
            if len(row[3]) <= 4:
                if int(row[3]) <= 1990:
                    to_1990 += 1
                else:
                    from_1990 += 1
    from_1990_percent = round(100*from_1990/len(table), 2)
    to_1990_percent = round(100*to_1990/len(table), 2)
    data = [['<=1990',to_1990_percent],[' >1990',from_1990_percent]]
    return data

def create_histogram(entries):
    """строит гистограмму на основе результатов"""
    graph = ''
    for i in range(len(entries)-1,-3,-1):
        for j in range(0,110,10):
            if j == 0 and i>= 0:
                graph += f'      |\n{entries[i][0]}|'
                number_of_timmes = int(entries[i][1])//10
                graph += RED
                graph += '    '*number_of_timmes
                graph += f'{END}{entries[i][1]}%'
            elif i <= -1 and j== 0:
                graph +='      '
            elif i == -1 and j> 0:
                graph += f'----'
            elif i == -2 and j> 0:
                graph += f' {j} '
        graph += '\n'
    print(graph)

percents = get_percent()
print('4. Гистограмма процентного количества книг до 1990 года и после')
create_histogram(percents)

#анимация с использованием os.system('cls')
def animate(x):
    """функция, которая создает анимацию, где x - размер"""
    for i in range(x):
        line = ''
        for j in range(x):
            if i == 0 or j == 0 or j == x - 1 or i == x - 1:
                line += f'{BLUE}   {END}'
            else:
                line += '   '
        print(line)
        time.sleep(0.2)
    os.system('cls')
    for i in range(x):
        line = ''
        for j in range(x):
            if i == x // 2 or j == x // 2:
                line += f'{BLUE}   {END}'
            else:
                line += '   '
        print(line)
        time.sleep(0.2)
    os.system('cls')
    for i in range(x):
        line = ''
        for j in range(x):
            if i == j or i + j == x - 1:
                line += f'{BLUE}   {END}'
            else:
                line += '   '
        print(line)
        time.sleep(0.2)
    os.system('cls')

print('5. анимация')
animate(15)