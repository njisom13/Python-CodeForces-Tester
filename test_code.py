def balanced_bitstring(bs,n,k):
    s=list(bs)
    #print(s)
    for i in range(k):
           # print(i,s[i])
        if s[i]=='?':
            for j in range(i+k,n,k):
                if s[j]!='?':
                    s[i]=s[j]
                    break
        #print(s)
    for i in range(k):
        if s[i]!='?':
            for j in range(i+k,n,k):
                if s[j]=='?':
                    s[j]=s[i]
                elif s[j]!=s[i]:
                    return "NO"
    ones,zeroes=s[0:k].count('1'),s[0:k].count('0')
    if ones<=k/2 and zeroes<=k/2:
        return "YES"
    return "NO"
 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split(' '))
        s=str(input())
        print(balanced_bitstring(s,n,k))