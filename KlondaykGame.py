# Функция для создания нулевой матрици
def new_matrix(field):
    matrix = [['0']*(field+1) for _ in range(field+1)]
    for i in range(field+1):
        matrix[0][i] = i
        matrix[i][0] = i
    return matrix

# Функция для вывода матрици
def print_matrix(matrix, field):
    for i in range(field+1):
        for m in range(field+1):
            print(matrix[i][m], end=' ')
        print('')

# Создание матрици 11*11
field = 11
matrix = new_matrix(field)

# Формирование границ поля
matrix[0][11] = ''
matrix[11][0] = ''
matrix[11][11] = '—'
matrix[10][11] = '|'
for i in range(1,10):
    matrix[i][11] = ' |'
for i in range(1,12):
    matrix[11][i] = '—'

# Функция проверки поля
def chek_1(x,y,matrix):
    count_1 = 0
    sp_koord = []
    if matrix[y-1][x-1] == 'X':
        count_1 += 1
        sp_koord += str(y - 1) + str(x-1)
    if matrix[y-1][x] == 'X':
        count_1 += 1
        sp_koord += str(y-1) + str(x)
    if matrix[y][x+1] == 'X':
        count_1 += 1
        sp_koord += str(y) + str(x+1)
    if matrix[y][x-1] == 'X':
        count_1 += 1
        sp_koord += str(y) + str(x-1)
    if matrix[y+1][x-1] == 'X':
        count_1 += 1
        sp_koord += str(y+1) + str(x-1)
    if matrix[y+1][x] == 'X':
        count_1 += 1
        sp_koord += str(y+1) + str(x)
    if matrix[y+1][x+1] == 'X':
        count_1 += 1
        sp_koord += str(y+1) + str(x+1)
    if matrix[y+1][x-1] == 'X':
        count_1 += 1
        sp_koord += str(y+1) + str(x-1)
    if count_1 >= 2:
        return 'Вы проиграли!'
    if count_1 == 1:
        return sp_koord
    if count_1 == 0:
        return 'Играем дальше'


# Функция проверки на цифры
def chek_numbers(x,y):
    while y.isdigit() != True or x.isdigit() != True:
        print('Введите цифры в координатак')
        y, x = input('введите координату y: '), input('введите координату x: ')
    return [int(y), int(x)]

# Функция проверки на попадание в поле и на свободную клетку
def chek_float(x,y):
    while ((0 < int(x) <= 10) + (0 < int(y) <= 10)) != 2:
        print('Введите координаты в переделах поля')
        y, x = (input('введите координату y: ')), (input('введите координату x: '))
        while y.isdigit() != True or x.isdigit() != True:
            print('Введите цифры в координатак')
            y, x = input('введите координату y: '), input('введите координату x: ')

    while matrix[int(y)][int(x)] == 'X':
        print('Эта клетка уже зарята')
        y, x = (input('введите координату y: ')), (input('введите координату x: '))
        while y.isdigit() != True and x.isdigit() != True:
            print('Введите цифры в координатак')
            y, x = input('введите координату y: '), input('введите координату x: ')
            while ((0 < int(x) <= 10) + (0 < int(y) <= 10)) != 2:
                print('Введите координаты в переделах поля')
                y, x = (input('введите координату y: ')), (input('введите координату x: '))
        while ((0 < int(x) <= 10) + (0 < int(y) <= 10)) != 2:
            print('Введите координаты в переделах поля')
            y, x = (input('введите координату y: ')), (input('введите координату x: '))
            while y.isdigit() != True or x.isdigit() != True:
                print('Введите цифры в координатак')
                y, x = input('введите координату y: '), input('введите координату x: ')
                while ((0 < int(x) <= 10) + (0 < int(y) <= 10)) != 2:
                    print('Введите координаты в переделах поля')
                    y, x = (input('введите координату y: ')), (input('введите координату x: '))

    return [int(y), int(x)]



#!!!НАЧАЛО ИГРЫ!!!
flag = True
while flag == True:
    # Запрос y и x
    y, x = input('Введите координату y: '), input('введите координату x: ')

    # Проверка координат
    list_1 = chek_numbers(x,y)
    list_2 = chek_float(list_1[0],list_1[1])

    # Записываем координаты
    koord_x, koord_y = list_2[1], list_2[0]


    # Ввод в матрицу
    matrix[koord_y][koord_x] = 'X'

    # Вывод матрицы после хода игрока
    print_matrix(matrix, field)

    # Проверка на проигрыш
    # Первая проверка
    if chek_1(koord_x, koord_y, matrix) == 'Вы проиграли!':
        print('Вы проиграли!')
        flag = False

    if chek_1(koord_x, koord_y, matrix) == 'Играем дальше':
        flag = True

    if chek_1(koord_x, koord_y, matrix) != 'Играем дальше' and chek_1(koord_x, koord_y,matrix) != 'Вы проиграли!':
        # Вторая проверка
        result_after_1_chek = list(map(int, chek_1(koord_x, koord_y, matrix)))
        second_check = chek_1(result_after_1_chek[1], result_after_1_chek[0], matrix)
        if second_check == 'Вы проиграли!':
            print('Вы проиграли!')
            flag = False
