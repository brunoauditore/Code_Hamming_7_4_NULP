import json
import translate


# Кодер


def go(arr):
    r1 = (arr[0] + arr[1] + arr[3]) % 2
    r2 = (arr[0] + arr[2] + arr[3]) % 2
    r3 = (arr[1] + arr[2] + arr[3]) % 2

    result = [r1,r2,arr[0],r3,arr[1],arr[2],arr[3]]
    return result


def to_code(s):
    arrayy = list(s)
    bits_array = []
    for i in range(len(arrayy)):
        bits_array.append(ord(arrayy[i]))

    return bits_array


# Розбиває 1 байт по 4 біта
def rozbivka(arr):
    array = list(arr)
    bits = []
    b = []
    index = 0
    for i in range(len(array) // 4):
        for k in range(4):
            b.append((array[index]))
            index += 1
        bits.append(b)
        b = []

    return bits


file = open('input.txt', 'r')
file_bits = open('bits.txt', 'w')
k = (to_code(file.read()))
f = []
f_roz = []
for i in range(len(k)):
    f.append(translate.to_bin_arr(k[i]))
    f_roz.append(rozbivka(f[i]))



z = []
for i in range(len(f_roz)):
    for j in range(len(f_roz[i])):
         z.append(go(f_roz[i][j]))

to_json = {'array': z}
file_bits.write(json.dumps(to_json))
