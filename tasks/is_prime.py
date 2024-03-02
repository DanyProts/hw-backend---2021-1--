def is_prime(n):
    a=[]
    if n==0 or n==1:
        return False
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    if (len(a)>1):
        return False
    else:
        return True

