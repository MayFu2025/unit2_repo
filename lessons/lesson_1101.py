def base2dec(base:int, num:int): #Only works for converting bases 2~9 into decimal
    index = 0
    sum = 0
    while num > 0:
        d = num % 10 #Extract digit
        b = base**index
        sum += d*b #Multiply the digit by base
        num = num//10 #Move onto next digit
        index += 1 #Move onto next digit
    return sum

print(base2dec(2, 101001))

def dec2base(base: int, num:int): #NOT WORKING
    sum = ""
    while num>0:
        sum += str(num % base)
        num = num // base
    return sum

#print(dec2base(4, 97))