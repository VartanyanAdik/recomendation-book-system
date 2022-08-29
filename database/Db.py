from entity.user import User

database_set = set()
test_user_one = User("Arkadi", "Vartanyan", "Gevorkovich", "adik508", "ad123")
test_user_two = User("Ivan", "Ivanov", "Ivanovich", "ivan508", "ivan123")
test_user_three = User("Artem", "Artemov", "Artemovich", "artem508", "artem123")
test_user_four = User("Vasili", "Vasilev", "Vasilevich", "vasili508", "vasili123")


def save_database(user):
    database_set.add(user)
    print("Пользователь успешно сохранен!")


save_database(test_user_one)
