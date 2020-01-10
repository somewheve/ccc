import re
from random import choice
from pypinyin import lazy_pinyin

## 如何提示 import pypinyin出错请执行 pip install python-pinyin 
data = []
filename = ["dict.txt", "dict_2.txt"]

for file in filename:
    with open(file, encoding="utf-8") as f:
        data.extend(list(map(lambda x: re.sub("([\u4e00-\u9fa5]*).*", lambda c:c.group(1), x.replace("\t", "").replace("\n", "").replace(" ", "")), f.readlines())))


data_res = list(set(data))

print(f"词库载入完毕，准备进行战斗，当前弹药数量: {len(data_res)}----->")
while True:
    print("Are you ready? N/没有，Y/成功, B/退出 \n")
    choose = input("Your choice: ")
    if choose.upper() == "Y":
        print("let's go !!")
        break

print("提示: 直接输入成语或者最后一次词语的拼音 ~~ 按B结束程序 \n\n")

count = 0

while True:
    temp = []
    inp = input("输入: ").replace(" ", "")
    if inp.upper() =="B":
        print(f"程序结束, 你玩了 {count} 轮游戏")
        break

    if re.match("[\u4e00-\u9fa5]+", inp) is not None:
        """ 中文情况 """
        result = list(map(lambda x: x if x and lazy_pinyin(list(x)[0])[0] == lazy_pinyin(list(inp)[-1])[0] else None, data_res))
        [temp.append(x) if x !=None else 1 for x in result]
        print("匹配结果: ", ", ".join(temp[1:4]))
    else:
        """ 拼音情况 """
        func = lambda d: d if d and lazy_pinyin(list(d)[0])[0] == inp else None
      
        result = [func(x) for x in data_res]

        [temp.append(x) if x !=None else 1 for x in result]
        print("匹配结果: ", ", ".join(temp[1:4]))
    if len(temp) == 0:
        print(f"游戏结束, 你总共玩了{count}")

    count  += 1 

    print("\n")