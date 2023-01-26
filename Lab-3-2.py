# -- coding: utf-8 --
def transpose(a):
    for i in range(rows):
        a[i] = [int(j) for j in input().strip().split(' ')]
    rows_count = len(a)
    
    colums_count = len(a[0])
    new_matrix = [[0] * rows_count for _ in range(colums_count)]
    
    for i in range(rows_count):
        for j in range(colums_count):
            new_matrix[j][i] = a[i][j]
    for row in new_matrix:
        print(*row)


if __name__ == '__main__':
    rows = int(input().strip())
    colums = int(input().strip())
    a = [colums for _ in range(rows)]
    print(transpose(a))