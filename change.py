def oneperevod(x):
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
        return x, 'finney'
    if len(x) >= 19:
        return x, 'eth'
x = str(1000000001)
this = oneperevod(x)
def perevod(this):
    if this[1] == 'kwei':
        return this[0][:-3] + ','+ this[0][-3:] , 'kwei'
    if this[1] == 'mwei':
        return this[0][:-6] + ','+ this[0][-6:] , 'mwei'
    if this[1] == 'gwei':
        return this[0][:-9] + ','+ this[0][-9:] , 'gwei'
    if this[1] == 'szabo':
        return this[0][:-12] + ','+ this[0][-12:] , 'szabo'
    if this[1] == 'finney':
        return this[0][:-15] + ','+ this[0][-15:] , 'finney'
    if this[1] == 'eth':
        return this[0][:-18] + ','+ this[0][-18:] , 'eth'
print(perevod(this))



    

        
    