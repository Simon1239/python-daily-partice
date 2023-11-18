# coding:utf-8

"""

"""

num = int(input("请输入杨辉三角打印行数:"))
triangle = []
for i in range(num):
    # row 列表装一行的数据
    row = []
    # 第i行就有i个数字，但索引从0开始，end到end-1结束
    for j in range(0, i+1):
        # 在第i行的第一个和最后一个数字为1
        if j == 0 or j == i:
            row.append(1)
        else:
            # 除了第一和最后一个为1， 其他数字都是上一行的左右两侧数字之和
            # 上一行为[i-1],左右则为[j]和[j-1]
            row.append(triangle[i-1][j]+triangle[i-1][j-1])
    triangle.append(row)

print(triangle)

