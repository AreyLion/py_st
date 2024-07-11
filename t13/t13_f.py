def task(string, symb):

#string = input("Введите строку")
#symb = input("Введите символ")

    first_index = string.find(symb)
    second_index = string.find(symb, first_index + 1)
    last_index = string.rfind(symb)

    if first_index == -1:
        return None, None
        #print('Нет такого символа')
        #print('Нет такого символа')
    else:
        if first_index == last_index:
            return string[first_index:], string[first_index:]
            #print(string[first_index:])
            #print(string[first_index:])
        else:
            return string[first_index:second_index+1], string[first_index:last_index+1]
            #print(string[first_index:second_index+1])
            #print(string[first_index:last_index+1])

answ = task("wertt", "t")
print(answ[0])
print(answ[1])