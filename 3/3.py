#coding=utf-8
import re
str="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score=0
for i in range(0,127,1):
      str2=[]
      for j in re.findall(".{2}",str):#任意两个字符的字符串 16进制每个字符4bit  两个字符代表十进制的一个字母
         str2 += chr(i^int(j,16))     #str2为str1与i（ASCII遍历）异或后字符串 int(j,16)将j转换为16进制
      str3 = "".join(str2)            #str3为连接后的字符串
      num=0
      for j in range(0,len(str3)):
         if str3[j]>='a'and str3[j]<='z':
             num+=1
      if num>score:
         score=num #更新判断
         str4=str3 #str4不断更新str3 当num最大，则为密文确定 
         key=chr(i) 
print key       #加密字符
print str4      #明文

#一个字节，8位二进制
#十六进制，一个十六进制可以表示4位二进制
#所以一个字节需要2个十六进制‘字符’来表示