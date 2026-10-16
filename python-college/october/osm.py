import re

def  check_username(username):
    pattern = r'^\w{3,10}$'
    if re.match(pattern, username):
         return True
    else:
        return False



username = input('Enter your username: ')
if check_username(username):
    print('Welcome ' + username + '!')
else:
    print('Sorry, that username isnt valid!')



string = list(input('Enter a string with years: ').split())

pattern = r'\d{4}$'
for year in string:
    if re.match(pattern, year):
        print(year)