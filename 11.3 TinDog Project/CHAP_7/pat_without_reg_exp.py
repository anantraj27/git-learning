# fininding 
#check whether phone no or not
#ex..456-789-342 
def isphone_no(text):
    if len(text) !=11:
        return False
    if not text[0:3].isdecimal():
        return False
    if text[3] !='-':
        return False
    if not text[4:7].isdecimal():
        return False
    if text[7] !='-':
        return False
    if not text[8:11].isdecimal():
        return False
    return True
text=input("enter text here\n")
for i in range(len(text)):
    chunk=text[i:i+11]
    if isphone_no(chunk):
        print("phone no found it is "+chunk)
   
