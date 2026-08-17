'''
class Revers_String:
    @staticmethod
    def reverse(string):
        reversed = ""
        for char in string:
            reversed = char + reversed
        return reversed
print(Revers_String.reverse("shubham"))
'''

name = "Rutuja"
reversed = name [:: -1]
print(reversed)