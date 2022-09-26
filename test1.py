
if __name__ == '__main__':

    re = "domain1.com"
    num = 0

    with open("log.txt") as file:
        for line in file:
            if re in line:
                num = num + 1
            else:
                continue

    file.close()

    print(num)
