"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    ls = []
    
    result = result.upper ()
    result1 = result.replace("O", "0")
    result2 = result1.replace("I", "1")
    result3 = result2.replace("A", "@")

    ls.append(result3)
    ls=list(ls[0])
    
    return ls

r10 = fn_hack_10()
print(r10) 