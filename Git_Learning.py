class prime_number:
    def is_Prime(self,number):
        if number <=1:
            return False
        for i in range(2,int(number ** 0.5) +1):
            if number % i ==0:
                return False
        return True
        
num = int(input("Enter the Number: "))
obj = prime_number()

if obj.is_Prime(num):
    print("Prime Number")
else:
    print("Not Prime")

