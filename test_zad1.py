
def fizzbuzz(num):
    if ((num % 15) == 0):
        return "FizzBuzz"
    elif ((num % 3) == 0):
        return "Fizz"
    elif ((num % 5) == 0):
        return "Buzz"

    else:
        raise Exception("Error in FizzBuzz")

def addWithDocString(self,x, y):
    """Takes two integers and adds them together to produce the result
    # >>> c = Calculate()
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(30)
    'FizzBuzz'
    >>> fizzbuzz(4509)
    'Fizz'
    >>> fizzbuzz(15505)
    'Buzz'
    >>> fizzbuzz(35505)
    'FizzBuzz'
    >>> fizzbuzz(11)
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.addWithDocString[3]>", line 1, in <module>
        fizzbuzz(11)
      File "C:/Users/wpluzek/PycharmProjects/doctest/main.py", line 11, in fizzbuzz
        raise Exception("Error in FizzBuzz")
    Exception: Error in FizzBuzz
    >>> fizzbuzz("abc")
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.addWithDocString[8]>", line 1, in <module>
        fizzbuzz("abc")
      File "C:/Users/wpluzek/PycharmProjects/doctest/main.py", line 3, in fizzbuzz
        if ((num % 15) == 0):
    TypeError: not all arguments converted during string formatting
    >>> fizzbuzz(None)
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.addWithDocString[9]>", line 1, in <module>
        fizzbuzz(None)
      File "C:/Users/wpluzek/PycharmProjects/doctest/main.py", line 3, in fizzbuzz
        if ((num % 15) == 0):
    TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
    >>> fizzbuzz(12.5)
    Traceback (most recent call last):
      File "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2021.2.2\plugins\python-ce\helpers\pycharm\docrunner.py", line 138, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest main.addWithDocString[10]>", line 1, in <module>
        fizzbuzz(12.5)
      File "C:/Users/wpluzek/PycharmProjects/doctest/main.py", line 11, in fizzbuzz
        raise Exception("Error in FizzBuzz")
    Exception: Error in FizzBuzz
    >>> fizzbuzz(-3)
    'Fizz'

    """



if __name__ == "__main__":
    import doctest
    doctest.testmod()
