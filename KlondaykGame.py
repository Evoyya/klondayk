#!!!СОЗДАНИЕ МАТРИЦЫ(10*10)!!!
# Функция для создания нулевой матрици
def new_matrix(field):
    matrix = [[0]*(field+1) for _ in range(field+1)]
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

# Функция проверки
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


#!!!НАЧАЛО ИГРЫ!!!

flag = True
while flag == True:
    # Запрос y и x
    y, x = int(input('введите координату y: ')), int(input('введите координату x: '))
    # Проверка, попадают ли координаты в поле
    if (0 < x <= 10) and (0 < y <= 10):
        # Запись этих кооринат
        koord_1_x = x
        koord_1_y = y
    else:
        # если координаты выходят за приделы поля, то повторить запрос, пока не поставят фишку в приделы поля
        position = False
        while position == False:
            print('Введите координаты, соответствующие размеру поля')
            y, x = int(input('введите координату y: ')), int(input('введите координату x: '))
            if (0 < x <= 10) and (0 < y <= 10):
                # Запись этих кооринат
                koord_1_x = x
                koord_1_y = y
                position = True
    # Проверка, свободна ли клетка
    if matrix[y][x] != 'X':
        matrix[y][x] = 'X'
    else:
        # Если клетка занята нужно запрашивать координаты, пока игрок не поставит фишку на свободное поле
        position = False
        while position == False:
            print('Эта клетка уже занята, введите координаты повторно')
            y, x = int(input('введите координату y: ')),int(input('введите координату x: '))
            if matrix[y][x] != 'X':
                matrix[y][x] = 'X'
                position = True
                # ВАЖНО тут тоже нужно делать проверку (Проверка 1)
                if chek_1(koord_1_x, koord_1_y, matrix) == 'Вы проиграли!':
                    print('Вы проиграли!')
                    flag = False
                if chek_1(koord_1_x, koord_1_y, matrix) == 'Играем дальше':
                    flag = True
                if chek_1(koord_1_x, koord_1_y, matrix) != 'Играем дальше' and chek_1(koord_1_x, koord_1_y,
                                                                                      matrix) != 'Вы проиграли!':
                    # (Проверка 2)
                    result_after_1_chek = list(map(int, chek_1(koord_1_x, koord_1_y, matrix)))
                    second_check = chek_1(result_after_1_chek[1], result_after_1_chek[0], matrix)
                    if second_check == 'Вы проиграли!':
                        print('Вы проиграли!')
                        flag = False

    # Вывод матрицы после хода игрока
    print_matrix(matrix,field)

    # Первая проверка
    if chek_1(koord_1_x,koord_1_y,matrix) == 'Вы проиграли!':
        print('Вы проиграли!')
        flag = False
    if chek_1(koord_1_x,koord_1_y,matrix) == 'Играем дальше':
        flag = True
    if chek_1(koord_1_x,koord_1_y,matrix) != 'Играем дальше' and chek_1(koord_1_x,koord_1_y,matrix) != 'Вы проиграли!':
        # Вторая проверка
        result_after_1_chek = list(map(int,chek_1(koord_1_x,koord_1_y,matrix)))
        second_check = chek_1(result_after_1_chek[1],result_after_1_chek[0],matrix)
        if second_check == 'Вы проиграли!':
            print('Вы проиграли!')
            flag = False




    

        
        
        
    
    

    
#ЙОУ
