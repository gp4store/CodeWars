# DESCRIPTION:
# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):

    s = s.lower()
    count1 = s.count('x')
    count2 = s.count('o')

    if count1 == count2:
        return print(True)
    elif count1 and count2 == 0:
        return print(True)
    else:
        return print(False)

xo("ooxx")#True
xo("xooxx")#False
xo("ooxXm")#True  
xo("zpzpzpp")#True 
xo("zzoo")#False
xo("oxOx")#True
xo("")#True