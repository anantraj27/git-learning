# TEXT={
#     'agree':""" yes,I agree .That sound fine to me """,
#     'busy':""" sorry ,can we do this later this week or next week ? """,
#     'upsell':"""would you consider making this a monthly donation ?"""
# }
# import sys ,pyperclip
# if len(sys.argv)<2:
#     print('usage: python mcclip.py[keyphrase]-copy phrase text')
#     sys.exit()
# keyphrase=sys.argv[1]    
# if keyphrase in  TEXT:
#    pyperclip.copy(TEXT[keyphrase])
#    print('TEXT for '+keyphrase + 'copied to clipboard')
# else:
#     print('there is no text for' +keyphrase)  
    
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
def manager(account):
   
    # dictionary in which keys are account 
    # name and values are their passwords
    passwords ={ "email" : "Ayushi123", 
                "facebook" : "shubham456",
                "instagram" : "Ayushi789",
                "geeksforgeeks" : "Ninja1" 
               }

    if account in passwords:
        
        # copies password to clipboard
        pyperclip.copy(passwords[account])

        print("Password :", passwords[account],
              ", for", account,
             "account", 
              "has been copied to the clipboard")
    else :
        print("No such account record exits")
        

# Driver function
if __name__ == "__main__":

    # command line argument that is name of 
    # account passed to program through cmd
    account = sys.argv[1]

    # calling manager function
    manager(account)

# This article has been contributed by
# Shubham Singh Chauhan