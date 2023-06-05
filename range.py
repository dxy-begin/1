# range()函数可以用来生成一个连续的整数序列
# 用法1：range(stop)
# 生成0，1，2，………，stop-1的整数
# 只有一个参数时就默认从0开始，间隔为1
print(range(5))  # python3中range()函数的返回值是range迭代器对象
# 可以用list()函数转换为列表
print(list(range(5)))

# 用法2：range(start,stop)
# 生成从start开始到stop-1结束,间隔为1的整数
print(range(1, 5))
print(list(range(1, 5)))

# 用法3：range(start,stop,step)
# 生成从start开始到stop-1结束,间隔为step的整数
print(range(1, 5, 2))
print(list(range(1, 5, 2)))

# 可用于for循环中控制循环次数
for _ in range(10):  # _表示临时变量，后面不需要用到该变量，仅仅表示循环10次
    print("阿琛，love u")
