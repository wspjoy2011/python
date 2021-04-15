def generate_permutations(n:int, m:int, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    else:
        for digit in range(n+1):
            prefix.append(digit)
            generate_permutations(n, m-1, prefix)
            prefix.pop()


generate_permutations(3, 3)


def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    else:
        gen_bin(m-1, prefix+'0')
        gen_bin(m-1, prefix+'1')
        gen_bin(m-1, prefix+'2')


gen_bin(10)
