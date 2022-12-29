# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: naive_string_match
# Author: xiaxu
# DATA: 2022/12/28
# Description:朴素的模式匹配算法
# ---------------------------------------------------
"""通过两个循环来匹配，这是最简单的匹配方法，时间复杂度很高"""
def naive_search(s:str,parttern:str) -> list:
    patt_len = len(parttern)
    position = [] #返回一个列表，记录所有匹配的位置
    for i in range(len(s)-patt_len+1): #这里+1是因为要匹配parttern第一个字符
        match_mark = True  #是否匹配到的标记
        for j in range(patt_len):
            if not s[j+i] == parttern[j]: #从parttern的第一个字符开始匹配
                match_mark = False
                break
        if match_mark:
                position.append(i)
    return position


if __name__ == '__main__':
    s = 'hello,python'
    parttern = 'th'
    print(naive_search(s, parttern))

