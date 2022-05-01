def add(a=0,b=0):
    add = a+b
    return(add)

def odd_even(a=0):
    if a % 2 == 0:
        return('given number is even')
    else:
        return('given number is odd')
def len_name(name):
    if type(name) != str:
        return('please provide string input')
    else:
        return(len(name))