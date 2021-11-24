import unittest

alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
specialchars = "!.,/?@!#$%^&*()_-+='<>|"


class PasswordVerify:
    def ValidPassword(password):
        big = False
        special = False
        if type(password) != str:
            raise Exception("Password must be a string")
        if (len(password) >= 8):
            for i in password:
                if i in alphabet:
                    big = True
                if i in specialchars:
                    special = True

        if (big and special):
            return True
        else:
            return False


class testWithUnitPassword(unittest.TestCase):
    def test_too_short(self):
        self.assertEqual(PasswordVerify.ValidPassword("abc"), False)

    def test_no_upper(self):
        self.assertEqual(PasswordVerify.ValidPassword("abcdefgh!@"), False)

    def test_no_special(self):
        self.assertEqual(PasswordVerify.ValidPassword("ABCDEFGHIJK"), False)

    def test_good(self):
        self.assertEqual(PasswordVerify.ValidPassword("SilneHaslo@!"), True)

    def test_good_numbers(self):
        self.assertEqual(PasswordVerify.ValidPassword("12345678A!"), True)

    def test_none(self):
        self.assertRaises(Exception, PasswordVerify.ValidPassword, None)

    def test_empty_array(self):
        self.assertRaises(Exception, PasswordVerify.ValidPassword, [])

    def test_only_number(self):
        self.assertRaises(Exception, PasswordVerify.ValidPassword, 123456789)


def testWithDocPassword():
    """Takes two integers and adds them together to produce the result
    # >>> c = Calculate()
    >>> PasswordVerify.ValidPassword("abc")
    False
    >>> PasswordVerify.ValidPassword("SuperHaslo!")
    True
    >>> PasswordVerify.ValidPassword("1234567A!")
    True
    >>> PasswordVerify.ValidPassword("1234567AB")
    False
    >>> PasswordVerify.ValidPassword("1234567@!!")
    False
    >>> PasswordVerify.ValidPassword(12345678)
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.testWithDocPassword[3]>", line 1, in <module>
        PasswordVerify.ValidPassword(12345678)
      File "C:/Users/wpluzek/PycharmProjects/lab7/main.py", line 12, in ValidPassword
        raise Exception("Password must be a string")
    Exception: Password must be a string
    >>> PasswordVerify.ValidPassword(["Abcdefgh!"])
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.testWithDocPassword[4]>", line 1, in <module>
        PasswordVerify.ValidPassword(["Abcdefgh!"])
      File "C:/Users/wpluzek/PycharmProjects/lab7/main.py", line 12, in ValidPassword
        raise Exception("Password must be a string")
    Exception: Password must be a string
    >>> PasswordVerify.ValidPassword([])
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.testWithDocPassword[5]>", line 1, in <module>
        PasswordVerify.ValidPassword([])
      File "C:/Users/wpluzek/PycharmProjects/lab7/main.py", line 12, in ValidPassword
        raise Exception("Password must be a string")
    Exception: Password must be a string
    >>> PasswordVerify.ValidPassword(None)
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.testWithDocPassword[6]>", line 1, in <module>
        PasswordVerify.ValidPassword(None)
      File "C:/Users/wpluzek/PycharmProjects/lab7/main.py", line 12, in ValidPassword
        raise Exception("Password must be a string")
    Exception: Password must be a string
    >>> PasswordVerify.ValidPassword({})
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.testWithDocPassword[7]>", line 1, in <module>
        PasswordVerify.ValidPassword({})
      File "C:/Users/wpluzek/PycharmProjects/lab7/main.py", line 12, in ValidPassword
        raise Exception("Password must be a string")
    Exception: Password must be a string
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
