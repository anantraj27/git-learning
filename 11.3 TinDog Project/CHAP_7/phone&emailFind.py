import pyperclip ,re
name=pyperclip.paste()
print(name)
findRegix=re.compile(r'''[+]\d+\s\d+\s\d+ | \d+[-]\d+[-]\d+ |\d+[-]\d+
      
                     
                     ''',re.VERBOSE)
findexRegix1=re.compile(r'\w+[.]?\w+')
mo=findRegix.findall(name)
print(mo)
