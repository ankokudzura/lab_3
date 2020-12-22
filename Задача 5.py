def check(a,b):
    t=[]
    ta=0
    D=False
    for y in range(len(a)):
        f=False
        tb = 0
        e = ''
        for i in range(ta, len(a)):
            for j in range(tb, len(b)):
                if a[i] == b[j]:
                    e+=a[i]
                    tb=j+1
                    break
        ta+=1
        t+=[e]
    max=0
    M=''
    for i in t:
        if len(i)>max:
            max=len(i)
            M=i
    return(M)
    
def task5(str1,str2,str3):
    print (check(check(str1,str2),str3))


str1 = "abcd1e2"
str2 = "bc12ea"
str3 = "bd1ea"
task5(str1,str2,str3)
print("__________________________________________")
str1 = "acgtacgtacgt"
str2 = "acgtacgt"
str3 = "acgt"
task5(str1,str2,str3)
