import urllib, json

import urllib.request, json 
with urllib.request.urlopen("http://serrannum:2929") as url:
    data = json.loads(url.read().decode())
    jsonNum = json.loads(data)
integer = jsonNum

ones = {'0' : '', '1' : 'satu ', '2' : 'dua ' , '3' : 'tiga ', '4' : 'empat ', '5' : 'lima ', '6' : 'enam ', '7' : 'tujuh ', '8' : 'lapan ', '9' : 'sembilan ' } 
teens = {'0' : 'sepuluh ', '1' : 'sebelas ', '2' : 'dua belas ' , '3' : 'tiga belas ', '4' : 'empat belas ', '5' : 'lima belas ', '6' : 'enam belas ', '7' : 'tujuh belas ', '8' : 'lapan belas ', '9' : ' sembilan belas ' } 
decades = {'0' : '', '1' : 'sepuluh ', '2' : 'dua puluh ' , '3' : 'tiga puluh ', '4' : 'empat puluh ', '5' : 'lima puluh ', '6' : 'enam puluh ', '7' : 'tujuh puluh ', '8' : 'lapan puluh ', '9' : 'sembilan puluh ' }
hundreds = {'0' : '', '1' : 'seratus ', '2' : ' dua ratus ' , '3' : ' tiga ratus ', '4' : ' empat ratus ', '5' : 'lima ratus ', '6' : 'enam ratus ', '7' : 'tujuh ratus', '8' : 'lapan ratus ', '9' : 'semiblan ratus ' } 
coma =  {'3' : 'ribu ', '6' : 'juta ', '9' : 'bilion ' }

word = ''
integer_side = integer 
int_length = len(integer)
integer_change = len(integer)
change = 3
while integer_change > 0:
    #print(integer_change)
    if integer == '0':
        word == 'kosong'
        break
    if integer_side[integer_change-2] == '1':
        for digit in teens:
            if integer_side[integer_change-1] == digit:
                word = teens[digit] + word
    else:
        for digit_1 in ones:
            if integer_side[integer_change-1] == digit_1:
                word = ones[digit_1] + word
        if integer_change > 1:
            for digit_2 in decades:
                if integer_side[integer_change-2] == digit_2:
                    word = decades[digit_2] + word
    if integer_change > 2:
        for digit_3 in hundreds:
            if integer_side[integer_change-3] == digit_3:
                word = hundreds[digit_3] + word
    if integer_change > 3:
        word = coma[str(change)] + word
    
    change = change + 3
    integer_change = integer_change - 3
print(word)
