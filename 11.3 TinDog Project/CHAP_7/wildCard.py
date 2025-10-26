import re
# object=re.compile(r'first name:.* last name:.*')
# mo=object.findall(' hii i am hungry my  identity is first name: anant last name:raj singh')
# print(mo)

object=re.compile(r'first name:(.) last name:(.)')
mo=object.search(' hii i am hungry my  identity is first name:anant  hello last name:raj singh what about you ')
print(mo.group())

