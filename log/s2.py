# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/8/8 14:55

c_list = [1, 2, 3]
i = 4

while len(c_list) != 691951:

    flag = True
    for j in xrange(2, i//2+1):
        if i % j == 0:
            flag = False
            break

    if flag:
        c_list.append(i)
    i += 1
    print(len(c_list))

print(i)
# print(c_list[4], c_list[5], c_list[6])

