#https://github.com/Wolframm74/codewars-repo
#https://www.codewars.com/kata/persistent-bugger

# persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.

#  persistence(4) => 0   # Because 4 is already a one-digit number.
#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit

#  persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
#                   # 1*2*6=12, and finally 1*2=2

#  persistence(4) # returns 0, because 4 is already a one-digit number

class persistence_helper():
    persistence_number=0
    n_len=0
    num_multiplications=0
    current_n=[]
    len_current=0
    def __init__(self, n):
        print(n)
        self.find_persistence_number(n)

    def find_persistence_number(self, n):
        self.n_len=len(n)

        self.current_n=n

        while (len(self.current_n)!=1):
            self.current_n=self.find_persistence_number_recurse(self.current_n)

    def find_persistence_number_recurse(self, current_n):

        product=1

        for i in range(0, len(current_n)):
            product=product*current_n[i]

        self.num_multiplications+=1

        new_n=map(int, str(product))

        return new_n

def persistence(n):

    n_array=map(int, str(n))

    print(n_array)

    if not (len(n_array)==1):
        instance=persistence_helper(n_array)
        return instance.num_multiplications
    if len(n_array)==1:
        return 0

if __name__=="__main__":
    x=persistence(39)
    print("x equals", x)

    y=persistence(4)
    print("y equals", y)

    z=persistence(25)
    print("z equals", z)