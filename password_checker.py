username = input('What\'s Your name?: ').capitalize()
  
password = input('What\'s Your password?: ')

password_length = len(password)

hidden_password = "*" * password_length

print(f'Hey {username}, your password - {hidden_password} is {password_length} letters long')

