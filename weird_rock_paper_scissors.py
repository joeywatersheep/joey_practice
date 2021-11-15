from random import randint
c = ['r', 'p', 's']
def a(_1, _2):
    return 'L' if (((_1 != 0 and _2 != 0) and _1 > _2) | (_1 == 0
        and _2 == 2) | (_2 == 0 and _1 == 1)) else ('W' if (((_2 != 0 and _1 != 0)
        and _2 > _1) | (_1 == 0 and _2 == 1) | (_1 == 2 and _2 == 0)) else '-')
print(a(randint(0, 2), c.index(input(':')))) 
#I have no idea about why I did this
#normally people (beginners like me)
#doing this rock paper scissors thing bu using
#multiple if operators
#I may use something like that too
#but I decided to do this piece of art work
