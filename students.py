# Accepts a GPA
# Returns a string (character)
# but prints happy friday first
import math

def gpa(gpa_input):
    #4.0 = A
    #3.0 - 3.9 = B
    floored = math.floor(gpa_input)
    look_up = {
        '4': 'A',
        '3': 'B',
        '2': 'C',
        '1': 'D',
        '0': 'F'
    }
    ans = look_up[str(floored)]
    if ans == 'C':
        ans = 'Happy Friday! ' + ans
    return ans
print(gpa(2.4))