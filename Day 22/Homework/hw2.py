print('-------------------------------')
print('Hello user')
choose = input('You Want to register or login: ')




if choose == 'register':
    gmail = input('Enter Your Gmail: ')
    username = input('Enter Your username: ')
    password = input('Enter Your password: ')
    reenter_pass = input('reenter Your password: ')

elif choose == "login":
    log_user = input('Enter your username: ')
    log_pass = input('Enter Your Password: ')
    print('----------------------------')
    print('You Succsesfuly Loged in')
    print('-----------------------------')

else:
    print('----------------------------')
    print('You succesfuly registered in')
    print('----------------------------')

