# Переводить з десяткової в двійкову і навпаки

def to_dec(a):
    A = list(a)
    A.reverse()
    b = 0
    for i in range(len(A)):
        b += 2 ** i * A[i]
    return b


def to_bin_arr(a):
    A = int(a)
    b = []
    while A > 0:
       b.append(A % 2)
       A = A // 2

    b.append(0)
    b.reverse()
    return b
