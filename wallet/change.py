'''    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "wei"   
        else:
            return x, "wei"         
    x /= 1000
    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "kwei"   
        else:
            return x, "kwei"        
    x /= 1000
    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "mwei"   
        else:
            return x, "mwei"        
    x /= 1000
    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "gwei"   
        else:
            return x, "gwei"        
    x /= 1000
    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "szabo"   
        else:
            return x, "szabo"        
    x /= 1000
    if x / 1000 < 1:
        if x % 1 == 0:
            return int(x), "finney"   
        else:
            return x, "finney"
    x /= 1000
    if x % 1 == 0:
        return int(x), "ether"   
    else:
        return x, "ether"    

print(perevod(175000005))

#assert perevod(175000005) == (175.000005, 'mwei')'''

def perevod(x):
    if len(x) < 4:
        return x, 'wei'
    if len(x) < 7:
        return x, 'kwei'
    if len(x) < 10:
        return x, 'mwei'
    if len(x) < 13:
        return x, 'gwei'
    if len(x) < 16:
        return x, 'szabo'
    if len(x) < 19:
        return x, 'funney'
    if len(x) >= 19:
        return x, 'eth'
print(perevod('1000'))

        
    