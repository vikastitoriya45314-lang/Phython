class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


class AgeVerification:
    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")

            elif age < 18:
                raise UnderAgeError("Under Age")

            elif age > 100:
                raise InvalidAgeError("Invalid Age")

            else:
                print("Valid age!")

        except ValueError as e:
            print("ValueError:", e)

        except UnderAgeError as e:
            print("UnderAgeError:", e)

        except InvalidAgeError as e:
            print("InvalidAgeError:", e)

        finally:
            print("Finally block executed")

object1 = AgeVerification()
object1.set_age(15)

object2 = AgeVerification()
object2.set_age(25)

object3 = AgeVerification()
object3.set_age(120)

object4 = AgeVerification()
object4.set_age(-5)