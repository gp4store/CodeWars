# Given a string made up of letters a, b, and/or c, switch the position of letters a and b 
# (change a to b and vice versa). Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):

    newstring = []
    list_s = list(s)

    for char in list_s:
        if char == 'a':
            newstring.append('b')
        elif char == 'b':
            newstring.append('a')
        elif char == 'c':
            newstring.append(char)
    
    swap_str = "".join(newstring)
    return print(swap_str)


switcheroo("abc")
switcheroo('aaabcccbaaa') 
switcheroo('ccccc')
switcheroo('abababababababab')
switcheroo('aaaaa')