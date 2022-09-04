def password_encryption(password):
    for password in password:
        password.capitalize()
        password.swapcase()
        cipher = ord(password) - len(password)
        if 0 < cipher < 129:
            cipher += (17 * 7)
        return chr(cipher)
