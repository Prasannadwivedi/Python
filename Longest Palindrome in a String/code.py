tt = int(input())
while tt>0:
    s = input()
    #print(s)
    cache = ''
    ans = ''
    s1 = ''
    s2=''
    lis = []
    temp=''
    if(s == s[::-1]):
        lis.append(s)
    
    for k in range(0,len(s)+1):
        for l in range(0,len(s)+1):
            cache = (s[k:l])
            #print(cache)
            if(cache == cache[::-1]):
                if(cache != ''):
                    lis.append(cache)
    #print(lis)
    lis = lis[::-1]
    for i in range((len(lis)-1)):
        s1=lis[i]
        s2=lis[i-1]
        #print("s1: ",s1," ",len(s1),",  s2: ",s2," ",len(s2))
        if len(s1) >= len(s2):
            if len(temp) <= len(s1):
                if len(s1) == 1:
                    temp=lis[len(lis)-1]
                else:
                    temp=s1
    
    print(temp)
    tt=tt-1
