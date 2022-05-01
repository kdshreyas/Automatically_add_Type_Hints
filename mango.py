def add(a: int=0,b: int=0) -> int:
    add = a+b
    return(add)

def odd_even(a: int=0) -> str:
    if a % 2 == 0:
        return('given number is even')
    else:
        return('given number is odd')
def len_name(name: int) -> str:
    if type(name) != str:
        return('please provide string input')
    else:
        return(len(name))