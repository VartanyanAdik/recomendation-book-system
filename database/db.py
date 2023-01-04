from crypto.cipher import password_encryption
from entity.user import User

database_dict = dict()#мето где будут хранится пользователи
test_user_one = User("Arkadi", "Vartanyan", "Gevorkovich", "adik508", "ad123")
test_user_two = User("Ivan", "Ivanov", "Ivanovich", "ivan508", "ivan123")
test_user_three = User("Artem", "Artemov", "Artemovich", "artem508", "artem123")
test_user_four = User("Vasili", "Vasilev", "Vasilevich", "vasili508", "vasili123")


def save_database(user):#сохранение пользователей
    database_dict[user.login] = user
    print("Пользователь успешно сохранен!")
    print(f"Пользователь {user.login} успешно добавлен!")


save_database(test_user_one)
save_database(test_user_two)
save_database(test_user_three)
save_database(test_user_four)

def check_user(login, password):
    return login in database_dict and database_dict[login].password == password_encryption(password)
