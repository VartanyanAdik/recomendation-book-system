def password_encryption(password):
    lst = ''
    for password in password:
        password.capitalize().swapcase()
        cipher = ord(password) - len(password)
        if 0 < cipher < 129:
            cipher += (17 * 7)
        lst += chr(cipher)
    return lst
