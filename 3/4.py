#coding=utf-8
import re
text=[]
for i in open("4.txt","r").readlines():   #readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表
    text=text+[i.replace("\n","")] #将文本变为一个长串 取消换行
score=0
for k in text:
    for i in range(0,127,1):           #密文在ASCII 0-127中
        str1=[]
        for j in re.findall(".{2}",k): #任意两个字符的字符串 遍历每个字符 16进制每个字符4bit，两个字符代表十进制的一个字母
            str1 += chr(i^int(j,16))   #str1为异或后字符串
        str2 = "".join(str1)           #str2连接
        num=0
        num=len(re.findall(r'[a-zA-Z ]',str2))#一定注意不要落下空格 [...]用来表示一组字符,单独列出 这里指a-z,A-Z和空格 查找字符串中a-z,A-Z和空格个数
        if num>score:
            score=num #更新判断
            str3=str2 #替换
            c=k
            key=chr(i) 
print c         #被加密字符串
print key       #加密字符
print str3      #明文