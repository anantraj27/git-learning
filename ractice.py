
# def table(item,leftwidth,rightwidth):
#   print('Table'.center(leftwidth+rightwidth,'-'))
#   for k, v in item.items():
#      print(k.ljust(leftwidth ,'.') ,end='' )
#      print(v)
# college="lnjpit chhapra"
# dict={}

# for i in college :
#     dict.setdefault(i,0)
#     dict[i]+=1
    
# # pprint.pprint(dict)
# table(dict,12,4)
    
# name='anant raj'
# print(name.title().istitle())
# print(name.isspace())
# print(name.upper())
# print(name.isalpha)
# print(name.isdecimal())
# print(id(name))
# print(id(name.isalpha()))
# # print(college.upper().center(20,"#").isupper())
# # print(''' hii tumhe kya lagta hai?
#         #   you know I really start to think about you what you think 
#                                         # I LOVE YOU \U0001F495''')
#copy content on clipboard 
# collection={
#     'happy':'''yeh,i am very happy with my work''',
#     'sad':'''yeh,sometime i feel lonely but i am not sad at all''',
#     'life':'''i belive letting go is the life '''
# }
# import pyperclip ,sys 
# if len(sys.argv)<2:
#     print('can print ')
#     sys.exit()
# keyphrase=sys.argv[1]
# if keyphrase in collection:
#     print('the value of '+keyphrase+'is copied')
# else:
#     print('there is no text for this keyphrase ')    
import sys, pyperclip

# function to copy account passwords
# to clipboard
# def manager(account):
   
#     # dictionary in which keys are account 
#     # name and values are their passwords
#     passwords ={ "email" : "Ayushi123", 
#                 "facebook" : "shubham456",
#                 "instagram" : "Ayushi789",
#                 "geeksforgeeks" : "Ninja1" 
#                }

#     if account in passwords:
        
#         # copies password to clipboard
#         pyperclip.copy(passwords[account])

#         print("Password :", passwords[account],
#               ", for", account,
#              "account", 
#               "has been copied to the clipboard")
#     else :
#         print("No such account record exits")
        

# # Driver function
# if __name__ == "__main__":

#     # command line argument that is name of 
#     # account passed to program through cmd
#     account = sys.argv[1]

#     # calling manager function
#     manager(account)

# # This article has been contributed by
# # Shubham Singh Chauhan
