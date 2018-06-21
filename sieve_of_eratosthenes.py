seive_erat(massive):
    '''
    Решето Эратосфена. Из сплошной последовательности чисел удаляются все делящиеся на первое простое число 2,
    затем удаляются все числа делящиеся на следующее число, встретившееся в списве, т.е. 3,
    затем на следующее оставшееся, т.е. 5 и т.д.
    '''
    for num in massive:
        for second in massive:
            if second > num:
                if second%num == 0:
                    massive.remove(second)
    return massive
    
if __name__ == '__main__:
    massive = [x for x in range(2, 100)]
    print(seive_erat(massive))
