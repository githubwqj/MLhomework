#最长字符串
def lcs(a, b):
    a_len = len(a)
    b_len = len(b)
    c = [[0 for i in range(b_len + 1)] for j in range(a_len + 1)]
    flag = [[0 for i in range(b_len + 1)] for j in range(a_len + 1)]
    for i in range(a_len):
        for j in range(b_len):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag

#对辅助矩阵进行输出
def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = 'XYXZYXY'
b = 'XZYZZYX'
c, flag = lcs(a, b)
# for i in c:
#     print(i)
# print('')
# for j in flag:
#     print(j)
# print('')
print("最长子序列为：")
printLcs(flag, a, len(a), len(b))
