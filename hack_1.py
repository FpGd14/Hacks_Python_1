"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    result = "fooziman"
    result = result.upper ()
    return result  
r1 = fn_hack_1()
print(r1)