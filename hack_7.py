"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result1 = []
    result = 6
    
    while result >= 1:
        result -= 1
        result1.append(result)

    return result1
      
r7 = fn_hack_7()
print(r7)