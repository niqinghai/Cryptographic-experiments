 #coding=utf-8
import base64
str="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d".decode("hex") #以 encoding 指定的编码格式解码字符串。默认编码为字符串编码,此处为16进制hex
str1=base64.b64encode(str) #base64加密
print str1