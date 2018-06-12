def credit_card_validation(card_number):
    print(f'Card number is {card_number}')
    card_number = str(card_number)
    last = len(card_number)-1
    sequence = []
    for number in enumerate(card_number):
        if number[0]%2 == 0: # Берем кажжую вторую цифру
            pre_sum = int(number[1])*2
            if pre_sum >= 10:
                fin_sum = 0
                for digit in enumerate(str(pre_sum)):
                    fin_sum += int(digit[1])
                sequence.append(fin_sum)
            else:
                sequence.append(pre_sum)
        else:
            sequence.append(number[1])
#        print(number)
        if number[0] == last:
            last_num = number[1]
#    print(f'Check digit is {last_num}')
#    print(sequence)
    seq_sum = 0
    for num in sequence[:-1]:
        seq_sum += int(num)   # Складываем без последней цифры, на случай если она удвоилась
    seq_sum += int(last_num)  # Добавляем заведомо не удвоенную последнюю цифру
    if seq_sum%10 == 0:
        print('Card number is valid')
    else:
        print('!!!!Card number is NOT valid!!!!')
