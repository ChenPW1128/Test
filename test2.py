import datetime
import fileinput
import parser
import sys
import time

if __name__ == '__main__':

    # 参数输入
    date = sys.argv[1]   # 传入日期，格式为：2022-09-25

    num = 0  # 当日请求的总个数
    count = 0  # 当日请求成功的总个数

    with open("log.txt") as file:
        for line in file:
            data_list = line.split(" ")
            st = data_list[3]
            ts = st.replace("[", "")
            timeStruct = time.strptime(ts, "%d/%b/%Y:%H:%M:%S")
            timeStamp = int(time.mktime(timeStruct))
            localTime = time.localtime(timeStamp)
            strTime = time.strftime("%Y-%m-%d %H:%M:%S",localTime)
            if strTime.split(" ")[0] == date:
                num = num + 1
                if data_list[8] == "200":
                    count = count + 1
            else:
                continue

    file.close()

    print(count/num)




