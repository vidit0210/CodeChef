a, b = [int(x) for x in input().split()]
cor = a-b
cor_len = len(str(cor))
wr = cor+1
while True:
    if len(str(wr)) == cor_len:
        print(wr)
        break
    wr = cor - 2
