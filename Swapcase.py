def swap_case(s):
    final = ''
    for i in s :
        if i.isspace == True :
            final+=i
        elif i.isupper() == True:
            final+=(i.lower())
        elif i.islower() == True:
            final+=(i.upper())
        else : 
            final+=i
    return final
  
