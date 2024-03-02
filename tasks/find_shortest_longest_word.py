__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    text+=' '
    mn = None
    mx = None
    a=[]
    chek=""
    if len(text)==0:
        return (mn,mx)
    for i in range(len(text)):
        if text[i]!= '\n' and text[i] != '\t' and text[i]!=' ':
           chek+=str(text[i])
        else:
            if chek!="":
                a.append(chek)
                chek=""

    if len(a)!=0:
        a1=[]
        for i in range(len(a)):
            a1.append(len(a[i]))
        mn=a[a1.index(min(a1))]
        mx=a[a1.index(max(a1))]
    return mn,mx

