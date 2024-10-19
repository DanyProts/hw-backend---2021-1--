__all__ = ("seconds_to_str",)
def seconds_to_str(n):
    secstr = int(n)
    data = ''
    s1 = secstr // 864000
    secstr = secstr - s1 * 864000
    s2 = secstr // 86400
    secstr = secstr - s2 * 86400
    if str(s1)+str(s2)!='00':
        data+=str(s1)+str(s2)+'d'
    s1 = secstr // 36000
    secstr = secstr - s1 * 36000
    s2 = secstr // 3600
    secstr = secstr - s2 * 3600
    if str(s1)+str(s2)!='00':
        data += str(s1) + str(s2) + 'h'
    elif data != '':
        data += str(s1) + str(s2) + 'h'
    s1 = secstr // 600
    secstr = secstr - s1 * 600
    s2 = secstr // 60
    secstr = secstr - s2 * 60
    if str(s1)+str(s2)!='00':
        data += str(s1) + str(s2) + 'm'
    elif data != '':
        data += str(s1) + str(s2) + 'm'
    s1 = secstr // 10
    secstr = secstr - s1 * 10
    s2 = secstr % 10
    secstr = secstr - s2
    data+=str(s1)+str(s2)+'s'
    return data
print(seconds_to_str(180))
