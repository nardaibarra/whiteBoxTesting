#GCF
def calculate_GCF(x:int, y:int):
    if x < 0 or y < 0 :
        print("Numbers should not be negative")
        return -1
    elif x == 1 or y == 1 :
        return 1
    else:
        while x!=y:
            if x > y:
                x = x - y
            else:
                y = y - x
    return x 


#Greatest num
def greatest_num(x:int, y:int):
    return -1 