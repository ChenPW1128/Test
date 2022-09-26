
if __name__ == '__main__':

    re = "domain1.com"
    num = 0

    with open("log.txt") as file:   # 从文件中读取日志数据
        for line in file:           # 逐行进行判断
            if re in line:
                num = num + 1       # 满足条件，num加1
            else:
                continue

    file.close()

    print(num)
