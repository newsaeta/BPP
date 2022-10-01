def exercise_1(list_num):
    data = [max(num) for num in list_num]
    # print(data)
    return data

def exercise_2(list_num):
    data = list(filter(lambda x: x % 2, list_num))
    print(f'Los números primos de la lista son: {data}')
    return data


if __name__ == '__main__':
    integer_list = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    prime_numbers = [3, 4, 8, 5, 5, 22, 13]
    exercise_1(integer_list)
    exercise_2(prime_numbers)
