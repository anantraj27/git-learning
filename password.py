#print('anant',end='@')
# print('27042004')
# y='hii'

# print("#".join(y))
username = "Admin"
def storeUsername(name):
    username = name
    checkAccess()
def checkAccess(resource):
    if username == 'Admin':
        print("access guranted")
    else:
      print('not gurranted')
storeUsername(username)      