def decimal(curr_num):
    number_name = ''
    ten = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    teen = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen',\
           7:'seventeen', 8:'eighteen', 9:'ninteen'}
    ty = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninty'}
# единицы
    try:
        if curr_num[1] != '1':
            word = ten[int(curr_num[0])]
            number_name = number_name + word
    # десятки
        elif curr_num[1] == '1':
            word = teen[int(curr_num[0])]
            number_name = number_name + word
        if int(curr_num[1]) in range(2, 10):
            word = ty[int(curr_num[1])]
            number_name = word + ' ' + number_name
    # сотни
        if int(curr_num[2]) in range(1, 10):
            word = ten[int(curr_num[2])]
            number_name = word + ' hungred ' + number_name
    except IndexError: print('Короткое число')
    return number_name

def num_name(number):
    final_number_name = ''
    str_number_rev = str(number)[::-1]
#    print(str_number_rev)
    dec = 0
    dec_name = {1: ' thousand ', 2:' million ', 3:' billion ', 4:' trillion ', 5:' trilliard ',\
               6:' quadrillion ', 7:' quintillion ', 8:' sextillon ', 9:' septillion ', 10:' octallion ',\
               11:' nonallion ', 12:' decallion ', 13:' endecallion ', 14:' dodecalon '}
    while len(str_number_rev) >= (dec * 3 + 1):
# Делим перевернутое число на тройки, добиваем нулями при необходимости и закидываем в decimal
        curr_num = str_number_rev[3*dec:3*dec+3]
#        print(curr_num)
        number_name = decimal(curr_num.ljust(3, '0'))
        if dec == 0:
            final_number_name = number_name
# при необходимости добавляем название тройки: миллион, миллиард и т.д.
        elif dec in range(1, 15):
            final_number_name = number_name + dec_name[dec] + final_number_name
        dec +=1
    print('{0:,}'.format(number).replace(',', '`') + f' = {final_number_name}')
    
if __name__ == '__main__':
    num_name(458621003562365821458852556594667455689517)
