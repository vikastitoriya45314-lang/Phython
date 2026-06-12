class AccountLockedError(Exception):
    pass


class LoginSystem:
    __password = "python@123"

    def __init__(self):
        self.__attempts = 3

    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account Locked!")

            if password == LoginSystem.__password:
                print("Login successful!")

            else:
                self.__attempts -= 1
                print("Wrong Password!")
                print("Remaining Attempts:", self.__attempts)

                if self.__attempts == 0:
                    raise AccountLockedError("Account Locked!")

        except AccountLockedError as e:
            print(e)

        finally:
            print("Finally block executed")

object = LoginSystem()

object.login("abc123")
object.login("test123")
object.login("wrongpass")
object.login("python@123")