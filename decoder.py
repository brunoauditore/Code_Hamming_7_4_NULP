import json
import translate


def invert(x):
    if x == 1:
        return 0
    else:
        return 1


def decode(arr):
    sindrom = []

    sindrom.append((arr[3] + arr[4] + arr[5] + arr[6]) % 2)
    sindrom.append((arr[1] + arr[2] + arr[5] + arr[6]) % 2)
    sindrom.append((arr[0] + arr[2] + arr[4] + arr[6]) % 2)
    print('sindrom: ', sindrom)

    if 1 in sindrom:
        if sindrom == [0, 1, 1]:
            arr[2] = invert(arr[2])

        if sindrom == [1, 0, 1]:
            arr[4] = invert(arr[4])

        if sindrom == [1, 1, 0]:
            arr[5] = invert(arr[5])

        if sindrom == [1, 1, 1]:
            arr[6] = invert(arr[6])

        #sindrom.reverse()
        #index = translate.to_dec(sindrom)
        #arr[index - 1] = invert(arr[index - 1])

    return [arr[2], arr[4], arr[5], arr[6]]


file_bits = open('bits.txt', 'r')
file = open('result.txt', 'w')
result = []
bits = json.loads(file_bits.read())
for i in bits:
    res =(bits['array'])

for j in range(len(res)):
    result.append(decode(res[j]))

print(result)
result_final = []

for g in range(0,len(result),2):
    result_final.append([result[g][0],result[g][1],result[g][2],result[g][3],result[g+1][0],result[g+1][1],result[g+1][2],result[g+1][3]])

print(result_final)
rs = []
string=''
for i in range(len(result_final)):
    rs.append(translate.to_dec(result_final[i]))

for j in range(len(rs)):
    string = string + chr(rs[j])

file.write(string)