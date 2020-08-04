from josephus.realise.realise_joseph import RealiseJoseph


def console_joseph():
    file = str(input("请输入文件地址："))
    start = int(input("请输入开始报数的位置："))
    step = int(input("请输入出约瑟夫环的间隔："))
    joseph = RealiseJoseph(file, start, step)
    print(joseph.get_str_result())
