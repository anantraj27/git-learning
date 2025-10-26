import re
phonenoRgex=re.compile(r'\*')
mo=phonenoRgex.search('my phone number is \*')
print('phone no found :'+mo.group())
