 # coding=utf-8 
import base64
str1="1c0111001f010100061a024b53535009181c".decode('hex')
str2="686974207468652062756c6c277320657965".decode('hex')
def xor(a,b):  #按照短的来，其他部分的不需要了
    if len(a)>len(b):
          return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(a[:len(b)],b)])
    else:
          return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(a,b[:len(a)])])
str3=xor(str1,str2)
print str3.encode('hex')
		  
#chr(） 返回值是当前整数对应的 ASCII 字符。
#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
#zip()传入的参数是两个切片得到的list
#L[: -1]，原应写作L[0: -1]，意为从第一个元素开始索引到最后一个元素为止（不包括最后一个元素）
#L[1:]，意为从第二个元素开始（第一个元素下标记为0），索引完整个列表（包括最后一个元素）