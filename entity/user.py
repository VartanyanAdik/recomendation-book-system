class User():
    def __init__(self, firstname, lastname, patronymic, login, password):
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.login = login
        self.password = password

    def __str__(self):
        return f"User(firstname={self.firstname}, lastname={self.lastname}, patronymic={self.patronymic}, " \
               f"login={self.login}, password={self.password})"
