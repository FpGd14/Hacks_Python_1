"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    ls = []
    for i in result:
        ls.append(i)
        ls.append('@')

    return ls  

r9 = fn_hack_9()
print(r9)