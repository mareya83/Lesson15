
class User:

    @staticmethod
    def sey_hello():
        return "Hello world"


class Admin(User):

    @staticmethod
    def mend_something():
        return "01101101"


class Developer(Admin):

    @staticmethod
    def write_code():
        return [0, 1, 0, 0, 1, 0]