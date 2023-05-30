
def bisiesto(year):
    if year <=0: return False
    if year % 4 != 0: return False
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if (year % 4 == 0) and (year>0):
        return True
    else:
        return False


