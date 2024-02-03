"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    num = 6
    result = []    
    i = 0  

    for i in range(num):
        
        result.append(i)
        
    return result

r6 = fn_hack_6()
print(r6)
  