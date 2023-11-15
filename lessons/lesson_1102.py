# def fromdecimal(num:int, base:int)->str:
#     result=""
#     alpha="abcdefghijklmnopqrstuvwxyz"
#     while num > base:
#         rem = num%base
#         if rem >= 10:
#             rem=alpha[rem-10]
#         result = str(rem) + result
#         num = num//base
#     result += str(num) + result
#     return result

def fromdecimal(num: int, base: int) -> str:
    result = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    while num > 0:
        rem = num % base
        if rem >= 10:
            rem = alpha[rem - 10]
        result = str(rem) + result
        num = num // base
    return result

# Example usage:
print(fomdecimal(162, 16))


# d = {
#     10:'A',
#     11:'B',
#     12:'C',
#     13:'D',
#     14:'E',
#     15:'F',
#     16:'G',
# }
# def fromdecimal2(num:int, base:int)->str:
#     result=""
#     alpha="abcdefghijklmnopqrstuvwxyz"
#     while num > base:
#         rem = num%base
#         if rem >= 10:
#             rem= alpha[rem-10]
#         result = str(rem) + result
#         num = num//base
#     result += str(num) + result
#     return result
#
# print(fromdecimal2(162,16))