
import random #To randomize the alphabets, numbers and special characters

#function to add numbers
def addnum(password,n):
    passlistwn = list(password) #string to list
    while n>0: #limiting number of the numeric characters
        inumb=random.randint(0, len(password) - 1)
        if passlistwn[inumb].isnumeric()==0:
            passlistwn[inumb]=random.choice(num)#randomly adding numbers to the password
            n -= 1
    password = "".join(passlistwn) #list to string
    return password


#function to add special characters
def addspchar(password,scn):
    passlistwn = list(password)
    while scn>0: #limiting number of the special characters

        ispc=random.randint(0, len(password) - 1)
        if passlistwn[ispc].isnumeric()==0:
            passlistwn[ispc] = random.choice(spchar)
            scn -= 1
    password = "".join(passlistwn)
    return password

#user inputs
print('\n\n\n')
print('*************************************************************************')

### Program warns user if the alphabets entered contains the user's name###
name=input('--> Enter name of the user: ')
letters=input('--> enter the albhabets you want to include in your password: ')
num='0123456789'
spchar='!@#$%^&*()_'
password=''

if name.lower() in letters.lower():
    cont = input('### Warning!! The alphabets you entered contains your name. Do you want to continue? (yes/no):  ')
else:
    cont='yes'

if cont.lower()=='yes':

    passlength = int(input('--> enter length of the password: '))
    numflag = input('--> do you want to include numbers?(yes/no): ')
    spcharflag = input('--> do you want to include special characters?(yes/no): ')

    #Random password generation using letters only
    for index in range(passlength):
        password=password+random.choice(letters)

    #checking if user wants to include numbers in the password
    if numflag.lower()=='yes':
        n=int(input('--> How many numbers (<length of password)  do you want? '))
        if n<passlength:
            password=addnum(password,n)
        else:
            print('### Invalid input for most recent question. No numbers will be included in password!!!  ')

    #checking if user wants to include special characters in the password
    if spcharflag.lower()=='yes':
        scn = int(input('--> How many special characters (<length of password) do you want? '))
        if scn<passlength:
            password=addspchar(password,scn)
        else:
            print('### Invalid input for most recent question. No special characters will be included in the password ')


    print('--> Randomly generated password is: '+password)
    print('*************************************************************************')

else:
    print('#### Process Aborted by User!!!')