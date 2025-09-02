import time

FLOATCONST = 1.23456789
STRINGCONST = "Python"
INTCONST = 123456789


float_var = 1.23456789
string_var = "hello"
int_var = 123456789

selected_line1 = False
selected_line2 = None

class Class():
    def __init__(self, arg):

        super().__init__()
        self.arg = arg # comment
    
        for i in range(self.arg):
            print(i)
    
    def function(arg):
        """
        multi-line
        function doc string
        """
        while True:
            if arg > 10:
                arg -= 1
                pass
            else:
                print(time.time())

                """ 
                multi line 
                comment
                print(time.time() - novar) # ignore novar
                """

                break

fstring = f"float: {FLOATCONST:.4f}, int: {INTCONST}"

array = [1, 2, 3]
dict = {"key": "value"}
