from datetime import datetime


def getString(msg):
    while True:
        try:
            inpt = input(f'  Enter {msg}: ').upper()
            if inpt != '' and inpt.isspace() == False and inpt.isalpha() == True:
                return inpt.strip()
            else:
                raise Exception
        except:
            print('  ----Invalid Input----')


def getDateTime(msg, frmt):
    while True:
        try:
            return datetime.strptime(input(f'  Enter {msg}: '), frmt)

        except:
            print(f'  ----Invalid {msg} Format----')


def getStringContact(msg):
    while True:
        try:
            inpt = input(f'  Enter {msg}: ')
            if inpt != '' and inpt.isspace() == False and inpt.isdigit() == True and len(inpt) == 11:
                return inpt.strip()
            else:
                raise Exception
        except:
            print(f'  ----Invalid {msg} Format----')
            
def getInt(msg):
    while True:
        try:
            inpt = int(input(f'  Enter {msg}: '))
            if inpt > 0:
                return inpt
            else:
                raise Exception
        except:
            print(f'  ----Invalid {msg} Format----')

def getInt(msg,primary):
    while True:
        try:
            inpt = int(input(f'  Enter {msg}: {primary}'))
            if inpt > 0:
                return inpt
            else:
                raise Exception
        except:
            print(f'  ----Invalid {msg} Format----')



def getEmail(msg):
    while True:
        try:
            inpt = input(f'  Enter {msg}: ')
            if inpt != '' and inpt.isspace() == False and len(inpt) > 5 and '@' in inpt and '.com' in inpt:
                return inpt.strip()

            else:
                raise Exception
        except:
            print(f'  ----Invalid {msg} Format----')