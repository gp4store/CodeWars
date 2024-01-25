# DESCRIPTION
# Complete the solution so that it returns a formatted string. 
# The return value should equal "Value is VALUE" where value is a 5 digit padded number.

# Example:

# solution(5) should return "Value is 00005"

def solution(value):

    len_val = str(value)
    fill_num = "0"
    lenght = 5

    return print(f'Value is {len_val.rjust(lenght, fill_num)}')

solution(0)
solution(5)
solution(109)
solution(1204)