input_str = input("Nhap X, Y: ")
n = [int(x) for x in input_str.split(",")]
rowN = n[0]
colN = n[1]

multilist = [[0 for col in range(colN)] for row in range(rowN)]

for row in range(rowN):
    for col in range(colN):
        multilist[row][col] = row * col

print(multilist)
