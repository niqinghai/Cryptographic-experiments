import re
str1=re.findall('.{2}',"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal".encode('hex'))
str2=re.findall('.{2}',("ICE"*50).encode('hex'))
str3=[]
for i in range(0,len(str1)):
    str3 +=[(chr(int(str1[i],16)^int(str2[i],16)))]
print "".join(str3).encode('hex')