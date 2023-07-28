uname = 'admin'
pwd = 'admin123'
attempt = 0

while True:
    attempt += 1
    print (f'attempt {attempt} of 3')
    username = input('enter username : ')
    password = input('enter password : ')
    if attempt ==3:
        print ('too many attempts')
        break 
    if username != uname:
        print('invalid username')
    if password != pwd:
        print('invalid password')
    if username == uname and password == pwd :
        print ('Login Successful')
        break

