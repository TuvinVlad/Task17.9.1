array = input('Введите числа через пробел:\n').split()
int_list = [int(item) for item in array]
while True:
    try:
        element = int(input('Введите число:\n'))
        break
    except ValueError:
        print('Необходимо ввести число')

for i in range(len(int_list)):
    for j in range(len(int_list)-i-1):
        if int_list[j] > int_list[j+1]:
            int_list[j], int_list[j+1] = int_list[j+1], int_list[j]


if element in int_list:
    def binary_search(int_list, element, left, right):
        if left > right:
            return False

        middle = (right + left) // 2
        if int_list[middle] == element:
            return middle
        elif element < int_list[middle]:
            return binary_search(int_list, element, left, middle - 1)
        else:
            return binary_search(int_list, element, middle + 1, right)


    element_index = binary_search(int_list, element, 0, len(int_list))
    result = element_index - 1
    print('Номер позиции элемента:', result)

else:
    print('Список не содержит введённого числа')
