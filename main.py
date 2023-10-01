from replit import db
import os, time, random

def menu():
  os.system('clear')
  time.sleep(1)
  a = '\033[4mWelcome to Replit\033[0m'
  print(f'\033[1;33m{a:^50}')
  time.sleep(1)
  print()
  ask = input (f'''Select any of the following:
1. Add New User
2. Login Existing User
  >> ''')
  return ask

def add():
  os.system('clear')
  time.sleep(0.5)
  a = '\033[4mCreate Your account here\033[0m'
  print(f'\033[1;33m{a:^50}')
  time.sleep(1)
  print()
  username = input('Enter your Username: ')
  password = input('Enter your password: ')
  salt = random.randint(1000, 9999)
  password = hash(f'{password}{salt}')
  db[username] = {'password': password, 'salt':salt}
  time.sleep(1)
  print ()
  print ('\033[32mAccount created successfully😎')
  time.sleep(2)
  

def login():
  os.system('clear')
  time.sleep(0.5)
  a = '\033[4mEnter your username and password to login\033[0m'
  print(f'\033[1;33m{a:^40}')
  print()
  time.sleep(1)
  user_name = input('Enter your Username: ')
  pass_word = input ('Enter your password: ')
  a = list(db.keys())
  print ()
  if user_name in a:
    b = db[user_name]['salt']
    c = hash(f'{pass_word}{b}')
    if c == db[user_name]['password']:
      print ('\033[32mLOGIN SUCCESSFUL 🎊')
    else:
      print ('\033[31mINCORRECT PASSWORD!😡')

  else:
    print('\033[31mINCORRECT USERNAME!😡')
  time.sleep(2)

while True:
  e = menu ()
  if e == '1':
    add()
  elif e == '2':
    login()
  else:
    print()
    print ('Please select either 1 or 2 to proceed!')
    time.sleep(2)
    os.system('clear')
    continue 
