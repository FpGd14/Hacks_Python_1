"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"

    for p  in result.split():
        result = p[:7].lower()  + p[-1:].upper()
    return result

r4= fn_hack_4()
print(r4)

# ----------------------------------------------------------------------------
                    # OTRO METODO SERIA :
    #def fn_hack_4():
        #result = "fooziman"
        # result0 =  result[:7].lower()
        # result1 =  result[-1:].upper()
        # result = result0 + result1

    #r4= fn_hack_4()
    #print(r4)
# ----------------------------------------------------------------------------